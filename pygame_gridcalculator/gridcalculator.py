from pygame import Surface, draw


class GridCalculatorException(Exception):
    """An exception used for GridCalculator-based exceptions."""
    pass


class GridCalculator:
    """Create a GridCalculator to map the available pixels on the screen
       against a grid of the users specified size.

    Parameters:
        pixel_end_left (int): The right pixel point for use by the grid.
        pixel_end_top (int): The bottom pixel point for use by the grid.
        grid_width_max (int): The max width point of the grid (right border).
        grid_height_max (int): The max height point of the grid (bottom
                               border).
        pixel_start_left (int): (Optional) The left pixel point for use by the
                                grid (default = 0).
        pixel_start_top (int): (Optional) The top pixel point for use by the
                               grid (default = 0).
    """

    def __init__(self, pixel_end_left: int, pixel_end_top: int,
                 grid_width_max: int, grid_height_max: int,
                 pixel_start_left: int = 0, pixel_start_top: int = 0):
        # Create and calculate grid
        self._check_value_links_are_valid(pixel_end_left, pixel_end_top,
                                          grid_width_max, grid_height_max,
                                          pixel_start_left, pixel_start_top)
        self._pixel_end_left = pixel_end_left
        self._pixel_end_top = pixel_end_top
        self._grid_width_max = grid_width_max
        self._grid_height_max = grid_height_max
        self._pixel_start_left = pixel_start_left
        self._pixel_start_top = pixel_start_top

    @staticmethod
    def _check_value_links_are_valid(pixel_end_left: int, pixel_end_top: int,
                                     grid_width_max: int, grid_height_max: int,
                                     pixel_start_left: int,
                                     pixel_start_top: int) -> None:
        """ Checks values which are inherently linked are valid before trying
        to set them.

        Parameters:
            pixel_end_left (int): The far right point to base the grid on
                                 in pixels.
            pixel_end_top (int): The bottom to base the grid on in pixels.
            grid_width_max (int): The max width point of the grid (right
                                  border).
            grid_height_max (int): The max height point of the grid (bottom
                                   border).
            pixel_start_left (int): The left pixel point for use by the grid.
            pixel_start_top (int): The top pixel point for use by the grid.
        """
        if (pixel_end_left - pixel_start_left) < grid_width_max:
            raise GridCalculatorException("The grid width ({}) cannot be "
                                          "greater than the pixel end left "
                                          "({})".format(grid_width_max,
                                                        (pixel_end_left -
                                                         pixel_start_left)))
        if (pixel_end_top - pixel_start_top) < grid_height_max:
            raise GridCalculatorException("The grid height ({}) cannot be "
                                          "greater than the pixel end top "
                                          "({})".format(grid_height_max,
                                                        (pixel_end_top -
                                                         pixel_start_top)))

    def __repr__(self):
        return "GridCalculator(pixel range: left={}-{}, top={}-{};  " \
               "grid: width={}, height={})".format(
                    self._pixel_start_left, self._pixel_end_left,
                    self._pixel_start_top, self._pixel_end_top,
                    self._grid_width_max, self._grid_height_max)

    def _get_width_pixels(self, point_needed: float) -> int:
        """Calculate the width point based on the value provided."""
        width = (self._pixel_end_left -
                 self._pixel_start_left) / self._grid_width_max
        return self._pixel_start_left + int(width * point_needed)

    def _get_height_pixels(self, point_needed: float) -> int:
        """Calculate the height point based on the value provided."""
        width = (self._pixel_end_top -
                 self._pixel_start_top) / self._grid_height_max
        return self._pixel_start_top + int(width * point_needed)

    @property
    def _pixel_end_left(self) -> int:
        """Get pixel end left point for grid."""
        return self._pix_end_left

    @_pixel_end_left.setter
    def _pixel_end_left(self, pixel_end_left: int) -> None:
        """Set pixel end left point for grid."""
        if pixel_end_left < 1:
            raise GridCalculatorException("Pixel end left must be greater "
                                          "than 1")
        self._pix_end_left = pixel_end_left

    @property
    def _pixel_end_top(self) -> int:
        """Get pixel end top point for grid."""
        return self._pix_end_top

    @_pixel_end_top.setter
    def _pixel_end_top(self, pixel_end_top: int) -> None:
        """Set pixel end top point for grid."""
        if pixel_end_top < 1:
            raise GridCalculatorException("Pixel end top must be greater "
                                          "than 1")
        self._pix_end_top = pixel_end_top

    @property
    def _grid_width_max(self) -> int:
        """Get grid width."""
        return self._g_width

    @_grid_width_max.setter
    def _grid_width_max(self, grid_width_max: int) -> None:
        """Set grid width."""
        if grid_width_max < 1:
            raise GridCalculatorException("Grid width must be greater than 1")
        self._g_width = grid_width_max

    @property
    def _grid_height_max(self) -> int:
        """Get grid height."""
        return self._g_height

    @_grid_height_max.setter
    def _grid_height_max(self, grid_height_max: int) -> None:
        """Set grid height."""
        if grid_height_max < 1:
            raise GridCalculatorException("Grid height must be greater than 1")
        self._g_height = grid_height_max

    @property
    def _pixel_start_left(self) -> int:
        """Get pixel start left position."""
        return self._pix_start_left

    @_pixel_start_left.setter
    def _pixel_start_left(self, pixel_start_left: int) -> None:
        """Set pixel start left position."""
        if pixel_start_left > self._pixel_end_left:
            raise GridCalculatorException("The pixel start left position ({}) "
                                          "cannot be greater than pixel end "
                                          "left position ({})".format(
                                            pixel_start_left,
                                            self._pixel_end_left))
        elif pixel_start_left < 0:
            raise GridCalculatorException("The pixel start left position ({}) "
                                          "cannot be less than 0".format(
                                            pixel_start_left))
        self._pix_start_left = pixel_start_left

    @property
    def _pixel_start_top(self) -> int:
        """Get pixel start top position."""
        return self._pix_start_top

    @_pixel_start_top.setter
    def _pixel_start_top(self, pixel_start_top: int) -> None:
        """Set pixel start top position."""
        if pixel_start_top > self._pixel_end_top:
            raise GridCalculatorException("The pixel start top position ({}) "
                                          "cannot be greater than the pixel "
                                          "end top position ({})".format(
                                            pixel_start_top,
                                            self._pixel_end_top))
        elif pixel_start_top < 0:
            raise GridCalculatorException("The pixel start top position ({}) "
                                          "cannot be less than 0".format(
                                            pixel_start_top))
        self._pix_start_top = pixel_start_top

    @property
    def size(self) -> tuple:
        """Returns the size of the grid.

        Returns:
            tuple: The actual size of the grid (width, height)"""
        return self._grid_width_max, self._grid_height_max

    @property
    def pixel_size(self) -> tuple:
        """Returns the pixel size of the grid.

        Returns:
            tuple: The size of the grid in pixels (width, height)"""
        return (self._pixel_end_left - self._pixel_start_left), \
               (self._pixel_end_top - self._pixel_start_top)

    def _error_check_left(self, left_point: float) -> None:
        """Left point error checking, checks left_point is in grid."""
        if 0 > left_point or left_point > self._grid_width_max:
            raise GridCalculatorException(
                "The left point provided ({}) isn't in the grid "
                "(0 - {})".format(left_point, self._grid_width_max))

    def _error_check_top(self, top_point: float) -> None:
        """Top point error checking, checks top_point is in grid"""
        if 0 > top_point or top_point > self._grid_height_max:
            raise GridCalculatorException(
                "The top point provided ({}) isn't in the grid "
                "(0 - {})".format(top_point, self._grid_height_max))

    def update_grid(self, grid_width_max: int, grid_height_max: int) -> None:
        """Recalculates the grid based on the provided width and height.

        Parameters:
            grid_width_max (int): The max width point of the grid (right
                                  border).
            grid_height_max (int): The max height point of the grid (bottom
                                   border)."""
        self._check_value_links_are_valid(self._pixel_end_left,
                                          self._pixel_end_top,
                                          grid_width_max, grid_height_max,
                                          self._pixel_start_left,
                                          self._pixel_start_top)
        self._grid_width_max = grid_width_max
        self._grid_height_max = grid_height_max

    def update_pixel_positions(self, pixel_end_left: int, pixel_end_top: int,
                               pixel_start_left: int = 0,
                               pixel_start_top: int = 0) -> None:
        """Recalculates the pixel positions the grid is based on.

        Parameters:
            pixel_end_left (int): The right pixel point for use by the grid.
            pixel_end_top (int): The bottom pixel point for use by the grid.
            pixel_start_left (int): (Optional) The left pixel point for use by
                                    the grid (default = 0).
            pixel_start_top (int): (Optional) The top pixel point for use by
                                   the grid (default = 0)."""
        self._check_value_links_are_valid(pixel_end_left, pixel_end_top,
                                          self._grid_width_max,
                                          self._grid_height_max,
                                          pixel_start_left, pixel_start_top)
        self._pixel_end_left = pixel_end_left
        self._pixel_end_top = pixel_end_top
        self._pixel_start_left = pixel_start_left
        self._pixel_start_top = pixel_start_top

    def top_point(self, point: float) -> int:
        """Returns the pixel position of the top point specified.

        Parameters:
            point (float): The grid point required from the top of the grid.

        Returns:
            int: The pixel value represented by the top grid point."""
        self._error_check_top(point)
        return self._get_height_pixels(point)

    def left_point(self, point: float) -> int:
        """Returns the pixel position of the left point specified.

        Parameters:
            point (float): The grid point required from the left of the grid.

        Returns:
            int: The pixel value represented by the left grid point."""
        self._error_check_left(point)
        return self._get_width_pixels(point)

    def position(self, left_point: float, top_point: float) -> tuple:
        """Returns the pixel positions in the grid of the specified points in
        the format.

        Parameters:
            left_point(float): The grid point required from the left of the
                               grid
            top_point (float): The grid point required from the top of the grid

        Returns:
            tuple: The pixel values represented by the grid points (left, top)
        """
        self._error_check_left(left_point)
        self._error_check_top(top_point)
        return self.left_point(left_point), self.top_point(top_point)

    def height_gap(self, top_point1: float, top_point2: float) -> int:
        """Returns the pixel gap between two specified grid top points.

        Parameters:
            top_point1 (float): The first top grid point to measure from.
            top_point2 (float): The second top grid point to measure to.

        Returns:
            int: The number of pixels between the two top points."""
        self._error_check_top(top_point1)
        self._error_check_top(top_point2)
        if top_point1 > top_point2:
            raise GridCalculatorException("top_point1 is greater than "
                                          "top_point2")

        return self.top_point(top_point2) - self.top_point(top_point1)

    def width_gap(self, left_point1: float, left_point2: float) -> int:
        """Returns the pixel gap between two specified left points.

        Parameters:
            left_point1 (float): The first left grid point to measure from.
            left_point2 (float): The second left grid point to measure to.

        Returns:
            int: The number of pixels between the two left points."""
        self._error_check_left(left_point1)
        self._error_check_left(left_point2)
        if left_point1 > left_point2:
            raise GridCalculatorException("left_point1 is greater than "
                                          "left_point2")

        return self.left_point(left_point2) - self.left_point(left_point1)

    def square(self, left_start: float, top_start: float, left_end: float,
               top_end: float) -> tuple:
        """Returns the total size of a square in pixels based on the top left
        point provided and bottom right point provided.

        Parameters:
            left_start (float): The left grid point for the top left of the
                              square
            top_start (float): The top grid point for the top left of the
                               square
            left_end (float): The left grid point for the bottom right of the
                            square
            top_end (float): The top grid point for the bottom right of the
                           square

        Returns:
            tuple: The pixel width and height of the square outlined
                   (width, height)"""
        self._error_check_left(left_start)
        self._error_check_top(top_start)
        self._error_check_left(left_end)
        self._error_check_top(top_end)
        if left_start > left_end:
            raise GridCalculatorException("left_start is greater than "
                                          "left_end")
        if top_start > top_end:
            raise GridCalculatorException("top_start is greater than top_end")

        return self.width_gap(left_start, left_end), self.height_gap(top_start,
                                                                     top_end)

    def points_from_left(self, points: float) -> int:
        """Returns the pixel position from the specified number of points from
        the left border.

        Parameters:
            points (float): The number of grid points from the left border

        Returns:
            int: The left pixel value represented by the grid point."""
        self._error_check_left(points)
        return self.left_point(points)

    def points_from_top(self, points: float) -> int:
        """Returns the pixel position from the specified number of points from
        the top border.

        Parameters:
            points (float): The number of grid points from the left border

        Returns:
            int: The top pixel value represented by the grid point."""
        self._error_check_top(points)
        return self.top_point(points)

    def points_from_right(self, points: float) -> int:
        """Returns the pixel position from the specified number of points from
        the right border.

        Parameters:
            points (float): The number of grid points from the right border

        Returns:
            int: The left pixel value represented by the grid point."""
        self._error_check_left(self._grid_width_max - points)
        return self.left_point(self._grid_width_max - points)

    def points_from_bottom(self, points: float) -> int:
        """Returns the pixel position from the specified number of points from
        the bottom border.

        Parameters:
            points (float): The number of grid points from the bottom border

        Returns:
            int: The top pixel value represented by the grid point."""
        self._error_check_top(self._grid_height_max - points)
        return self.top_point(self._grid_height_max - points)

    def draw_grid_to_surface(self, surface: Surface,
                             color: tuple = (0, 0, 0)) -> None:
        """Draws the grid to the pygame surface provided.

        Parameters:
            surface (pygame.Surface): The surface you want to show the grid
                                      on.
            color (tuple): (Optional) Set the color of the grid
                           (default = black (0, 0, 0))."""
        # Draw lines from left to right
        l_point, t_point = 0, 0
        while l_point <= self._grid_width_max:
            draw.line(surface, color,
                      (self.left_point(l_point), self.points_from_top(0)),
                      (self.left_point(l_point), self.points_from_bottom(0)))
            l_point += 1
        # Draw lines from top to bottom
        while t_point <= self._grid_height_max:
            draw.line(surface, color,
                      (self.points_from_left(0), self.top_point(t_point)),
                      (self.points_from_right(0), self.top_point(t_point)))
            t_point += 1
