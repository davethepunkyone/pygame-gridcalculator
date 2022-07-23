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
co-ordinates to the position on the screen you want to 

## Example
### Basic usage
Setting the variable and creating a new rect using a grid:

    display = pygame.display.set_mode((200, 100), pygame.RESIZABLE)
    display.fill((255, 255, 255))
    grid = GridCalculator(display.get_width(), display.get_height(), 10, 5)
    
    rect = pygame.Rect(grid.left_point(1), grid.left_point(1),
                       grid.width_gap(1, 3), grid.height_gap(1, 3))
    pygame.draw.rect(display, (255, 0, 0), rect)

So in this example, a pygame display is created of 200x100, and a grid
is created splitting this into a 10x5 grid, like so:
!(Example 1 Grid)[images/example_1_grid.png]

This creates a square on the screen like so:
!(Example 1 Image)[images/example_1_pygame.png]

### Full Scalable Example
The following creates an initial display with a rect and a grid that
can scale with the display.


