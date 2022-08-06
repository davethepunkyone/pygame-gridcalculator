import pygame
from gridcalculator import GridCalculator


class ShapeFactory:
    def __init__(self, grid_calc: GridCalculator):
        self.grid = grid_calc

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

    def _convert_grid_tuple(self, grid_tuple: tuple) -> tuple:
        """Takes the grid tuple and returns a pixel tuple."""
        left_grid, top_grid = grid_tuple
        return self.grid.left_point(left_grid), self.grid.top_point(top_grid)

    def draw_line(self, surface: pygame.Surface, color: tuple,
                  grid_start_pos: tuple, grid_end_pos: tuple,
                  width: int) -> pygame.draw.line:
        """Returns a pygame.draw.line based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            grid_start_pos (tuple): The start point in grid positions
                                    (grid_left, grid_top).
            grid_end_pos (tuple): The start point in grid positions
                                  (grid_left, grid_top).
            width (float): The width of the line in pixels.

        Returns:
            pygame.draw.line: A pygame.draw.line object."""
        return pygame.draw.line(surface, color,
                                self._convert_grid_tuple(grid_start_pos),
                                self._convert_grid_tuple(grid_end_pos), width)

    def draw_aaline(self, surface: pygame.Surface, color: tuple,
                    grid_start_pos: tuple, grid_end_pos: tuple,
                    blend: int) -> pygame.draw.aaline:
        """Returns a pygame.draw.aaline based on grid left and top points.

        Parameters:
            surface (pygame.Surface): The surface to draw the line on to.
            color (tuple): The color value for the line.
            grid_start_pos (tuple): The start point in grid positions
                                    (grid_left, grid_top).
            grid_end_pos (tuple): The start point in grid positions
                                  (grid_left, grid_top).
            blend (int): The blend of the line.

        Returns:
            pygame.draw.line: A pygame.draw.line object."""
        return pygame.draw.aaline(surface, color,
                                  self._convert_grid_tuple(grid_start_pos),
                                  self._convert_grid_tuple(grid_end_pos),
                                  blend)
