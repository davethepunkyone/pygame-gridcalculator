import pygame
from .gridcalculator import GridCalculator


class ShapeFactory:
    def __init__(self, grid_calculator: GridCalculator):
        self.grid = grid_calculator

    def _convert_grid_tuple(self, grid_tuple: tuple) -> tuple:
        """Takes the grid tuple and returns a pixel tuple."""
        left_grid, top_grid = grid_tuple
        return self.grid.left_point(left_grid), self.grid.top_point(top_grid)

    def _convert_grid_list(self, grid_list: list) -> list:
        """Takes a list of grid tuples and returns a list of pixel tuples."""
        points = []
        for grid_point in grid_list:
            points.append(self._convert_grid_tuple(grid_point))
        return points

    # pygame.Rect shapes

    def Rect(self, grid_left: int, grid_top: int, width: float,
             height: float) -> pygame.Rect:
        """Returns a Rect based on grid left and top points.

        Parameters:
            grid_left (int): The left grid point to use.
            grid_top (int): The top grid point to use.
            width (float): The width in pixels.
            height (float): The height in pixels.

        Returns:
            pygame.Rect: A pygame Rect object."""
        return pygame.Rect(self.grid.left_point(grid_left),
                           self.grid.top_point(grid_top),
                           width, height)

    # pygame.draw shapes

    def draw_line(self, surface: pygame.Surface, color: tuple,
                  grid_start_pos: tuple, grid_end_pos: tuple,
                  width: int = 1) -> pygame.Rect:
        """Calls pygame.draw.line based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            grid_start_pos (tuple): The start point in grid positions
                                    (grid_left, grid_top).
            grid_end_pos (tuple): The start point in grid positions
                                  (grid_left, grid_top).
            width (float): (Optional) The width of the line in pixels
                           (default = 1).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.line(surface, color,
                                self._convert_grid_tuple(grid_start_pos),
                                self._convert_grid_tuple(grid_end_pos), width)

    def draw_lines(self, surface: pygame.Surface, color: tuple, closed: bool,
                   grid_points: list, width: int = 1) -> pygame.Rect:
        """Calls pygame.draw.lines based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            closed (bool): If True, a line is drawn between the first and last
                           points.
            grid_points (list): The list of points in grid positions
                                (grid_left, grid_top).
            width (int): (Optional) The width of the line (default = 1).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.lines(surface, color, closed,
                                 self._convert_grid_list(grid_points), width)

    def draw_aaline(self, surface: pygame.Surface, color: tuple,
                    grid_start_pos: tuple, grid_end_pos: tuple,
                    blend: int = 1) -> pygame.Rect:
        """Calls pygame.draw.aaline based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            grid_start_pos (tuple): The start point in grid positions
                                    (grid_left, grid_top).
            grid_end_pos (tuple): The start point in grid positions
                                  (grid_left, grid_top).
            blend (int): (Optional) The blend of the line (default = 1).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.aaline(surface, color,
                                  self._convert_grid_tuple(grid_start_pos),
                                  self._convert_grid_tuple(grid_end_pos),
                                  blend)

    def draw_aalines(self, surface: pygame.Surface, color: tuple, closed: bool,
                     grid_points: list, blend: int = 1):
        """Calls pygame.draw.aalines based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            closed (bool): If True, a line is drawn between the first and last
                           points.
            grid_points (list): The list of points in grid positions
                                (grid_left, grid_top).
            blend (int): (Optional) The blend of the line (default = 1).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.aalines(surface, color, closed,
                                   self._convert_grid_list(grid_points), blend)

    def draw_polygon(self, surface: pygame.Surface, color: tuple,
                     grid_points: list, width: int = 0) -> pygame.Rect:
        """Calls pygame.draw.polygon based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the polygon on to.
            color (tuple): The color value for the polygon.
            grid_points (list): A list of grid points in the format
                                (grid_left, grid_top).
            width (int): (Optional) The width of the line (default = 0).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.polygon(surface, color,
                                   self._convert_grid_list(grid_points), width)

    def draw_circle(self, surface: pygame.Surface, color: tuple,
                    grid_center: tuple, radius: float, width: int = 0,
                    draw_top_right: bool = True, draw_top_left: bool = True,
                    draw_bottom_left: bool = True,
                    draw_bottom_right: bool = True) -> pygame.Rect:
        """Calls pygame.draw.polygon based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the polygon on to.
            color (tuple): The color value for the polygon.
            grid_center (tuple): The center point in grid positions
                                 (grid_left, grid_top).
            radius (float): The radius of the circle.
            width (int): (Optional) The width of the line (default = 0).
            draw_top_right (bool): (Optional) Specifies if the top right of the
                                   circle should be drawn (default = True).
            draw_top_left (bool): (Optional) Specifies if the top left of the
                                  circle should be drawn (default = True).
            draw_bottom_left (bool): (Optional) Specifies if the top left of
                                     the circle should be drawn
                                     (default = True).
            draw_bottom_right (bool): (Optional) Specifies if the top right of
                                      the circle should be drawn
                                      (default = True).

        Returns:
            pygame.Rect: A pygame.Rect object."""
        return pygame.draw.circle(surface, color,
                                  self._convert_grid_tuple(grid_center),
                                  radius, width, draw_top_right, draw_top_left,
                                  draw_bottom_left, draw_bottom_right)
