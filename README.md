# pygame-gridcalculator
A tool that creates a custom-sized virtual grid for helping place objects 
on the screen.

## Purpose
This tool is designed to easily map positions on a pygame display without
relying on fixed pixel values.  This is done by mapping the window to a
grid, and allowing for the providing of grid co-ordinates to get the actual
pixel value on the screen.

This is designed for people getting started with pygame, or people wanting
to create uniform menu elements that scale with the display size.

## How it works
To utilise this tool, you should initialise it to a variable and pass in the
current screen size and the size of the grid you wish to use.

Once the grid has been created, you use the GridCalculator to provide
co-ordinates to the position on the screen you want to reference.

Created grids will always have a starting left and top position of 0.

## Initialize and Methods
### Import
To import the Grid Calculator use the following statement:

    from pygame_gridcalculator import GridCalculator

### Initialize Grid Calculator
To initialize a grid Calculator, use the following logic to assign to a variable:

    grid = GridCalculator(display_width, display_height, grid_width, grid_height)

The arguments to specify are as follows:
* __display_width__: _The width of the current pygame display_
* __display_height__: _The height of the current pygame display_
* __grid_width__: _The total number of points you want in your grid from left to right_
* __grid_height__: _The total number of points you want in your grid from top to bottom_

So if you want to initialize a grid that is 8x6 for your display of 800x600, the code
would look something like:

    display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    grid = Grid(display.get_width(), display.get_height(), 8, 6)

### Grid Calculator Methods
The grid calculator has the following methods and functions:

| Method                                                                           | Description                                                                                                                                     |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| __size__                                                                         | _Returns the total number of points in the grid (width, height)._                                                                               |
| __max_points__                                                                   | _Returns the max points of the grid (width, height)._                                                                                           |
| __top_point(point: _int_)__                                                      | _Returns the pixel value for the point selected from the top of the grid._                                                                      |
| __left_point(point: _int_)__                                                     | _Returns the pixel value for the point selected from the left of the grid._                                                                     |
| __position(left_point: _int_, top_point: _int_)__                                | _Returns the pixel values for the point co-ordinates selected from the grid (left, top)._                                                       |
| __height_gap(top_point1: _int_, top_point2: _int_)__                             | _Returns the pixel height between the two top grid points specified._                                                                           |
| __width_gap(left_point1: _int_, left_point2: _int_)__                            | _Returns the pixel width between the two left grid points specified._                                                                           |
| __square(left_start: _int_, top_start: _int_, left_end: _int_, top_end: _int_)__ | _Returns the pixel height and width of a square based on the grid position of the top left corner and the bottom right corner (width, height)._ |
| __points_from_left(points: _int_)__                                              | _Returns the pixel value for the amount of grid points away from the left border._                                                              |
| __points_from_top(points: _int_)__                                               | _Returns the pixel value for the amount of grid points away from the top border._                                                               |
| __points_from_right(points: _int_)__                                             | _Returns the pixel value for the amount of grid points away from the right border._                                                             |
| __points_from_bottom(points: _int_)__                                            | _Returns the pixel value for the amount of grid points away from the bottom border._                                                            |

## Example
### Basic usage
Setting the variable and creating a new rect using a grid calculator:

    display = pygame.display.set_mode((200, 100), pygame.RESIZABLE)
    display.fill((255, 255, 255))
    grid = GridCalculator(display.get_width(), display.get_height(), 10, 5)
    
    rect = pygame.Rect(grid.left_point(1), grid.top_point(1),
                       grid.width_gap(1, 3), grid.height_gap(1, 4))
    pygame.draw.rect(display, (255, 0, 0), rect)

So in this example, a pygame display is created of 200x100 pixels, and a grid
is created splitting this into a 10x5 grid, where each square is a 20x20 grid 
point, like so:

![Example 1 Grid](https://raw.githubusercontent.com/davethepunkyone/pygame-gridcalculator/main/images/example_1_grid.png)

When it comes to drawing the Rect, the calculator identifies that it requires the following:
 * Left grid point 1 as the start left position, which in this scenario returns 20
   * _Logic used: (200 / 10) * 1 = 20 pixels from left_
 * Top grid point 1 as the start top position, which in this scenario also returns 20 
   * _Logic used: (100 / 5) * 1 = 20 pixels from top_
 * The gap between left grid point 1 and 3 for the width, which returns 40 
   * _Logic used:_ 
     * _Point 1 = (200 / 10) * 1 = 20 pixels from left_
     * _Point 3 = (200 / 10) * 3 = 60 pixels from left_
     * _60 - 20 = 40 pixels width_
 * The gap between top grid point 1 and 4 for the height, which returns 60
   * _Logic used:_
     * _Point 1 = (100 / 5) * 1 = 20 pixels from top_
     * _Point 3 = (100 / 5) * 4 = 80 pixels from top_
     * _80 - 20 = 60 pixels height_

Using this information creates a rectangle on the screen like so:

![Example 1 Pygame](https://raw.githubusercontent.com/davethepunkyone/pygame-gridcalculator/main/images/example_1_pygame.png)


### Full Scalable Example
The following creates an initial display with a rect and a grid that
can scale with the display.

    def example():
        running = True
        display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
        display_height, display_width = display.get_height(), display.get_width()
        grid = GridCalculator(display_width, display_height, 20, 20)
    
        pygame.init()
    
        while running:
            display.fill((200, 200, 200))
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.VIDEORESIZE:
                    display_height = event.h
                    display_width = event.w
                    grid = GridCalculator(display_width, display_height, 20, 20)
    
            # Draw face
            pygame.draw.rect(display, (255, 0, 0),
                             pygame.Rect(grid.left_point(5), grid.top_point(5),
                             grid.width_gap(5, 15), grid.height_gap(5, 15)))
            pygame.draw.rect(display, (0, 0, 255),
                             pygame.Rect(grid.left_point(7), grid.top_point(11),
                             grid.width_gap(7, 13), grid.height_gap(11, 14)))
            pygame.draw.rect(display, (0, 255, 0),
                             pygame.Rect(grid.left_point(7), grid.top_point(7),
                             grid.width_gap(7, 9), grid.height_gap(7, 9)))
            pygame.draw.rect(display, (0, 255, 0),
                             pygame.Rect(grid.left_point(7), grid.top_point(7),
                             grid.width_gap(7, 9), grid.height_gap(7, 9)))
            pygame.draw.rect(display, (0, 255, 0),
                             pygame.Rect(grid.left_point(11), grid.top_point(7),
                             grid.width_gap(11, 13), grid.height_gap(7, 9)))
    
            # Draw corner squares
            sq_width, sq_height = grid.width_gap(1, 2), grid.height_gap(1, 2)
    
            pygame.draw.rect(display, (0, 0, 0),
                             pygame.Rect(grid.points_from_left(1),
                                         grid.points_from_top(1),
                                         sq_width, sq_height))
            pygame.draw.rect(display, (0, 0, 0),
                             pygame.Rect(grid.points_from_right(2),
                                         grid.points_from_top(1),
                                         sq_width, sq_height))
            pygame.draw.rect(display, (0, 0, 0),
                             pygame.Rect(grid.points_from_left(1),
                                         grid.points_from_bottom(2),
                                         sq_width, sq_height))
            pygame.draw.rect(display, (0, 0, 0),
                             pygame.Rect(grid.points_from_right(2),
                                         grid.points_from_bottom(2),
                                         sq_width, sq_height))
            pygame.display.update()

This splits the screen into a 20x20 grid, and is able to rescale dependent
on the size of the window.  If the size is changed, the rectangles will
scale based on the new size of the window, still in a 20x20 grid.

When the window initially loads, the shapes display like so:

![Example 2 Pygame Default](https://raw.githubusercontent.com/davethepunkyone/pygame-gridcalculator/main/images/example_2_pygame_default.png)

If the window is resized, the shapes adjust with the size of the grid:

![Example 2 Pygame Default](https://raw.githubusercontent.com/davethepunkyone/pygame-gridcalculator/main/images/example_2_pygame_long.png)

![Example 2 Pygame Default](https://raw.githubusercontent.com/davethepunkyone/pygame-gridcalculator/main/images/example_2_pygame_wide.png)

Dependent on the situation, you may want to modify the grid based on 
the window size and rescale the grid appropriately.  Because the grid is
repopulated on the resize an if statement could be added if needed to
check the screen width/height and modify the grid as needed.
