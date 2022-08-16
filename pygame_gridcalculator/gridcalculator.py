from pygame import Surface, draw


class GridCalculatorException(Exception):
    """An exception used for GridCalculator-based exceptions."""
    pass


class GridCalculator:
    """Create a GridCalculator to map the available pixels on the screen
       against a grid of the users specified size.

    Parameters:
        surface_width (int): The width of the surface to base the grid on in
                            pixels.
        surface_height (int): The height of the surface to base the grid on in
                             pixels.
        grid_width_max (int): The max width point of the grid (right border).
        grid_height_max (int): The max height point of the grid (bottom
                               border).
    """

    def __init__(self, surface_width: int, surface_height: int,
                 grid_width_max: int, grid_height_max: int,
                 pixel_start_left: int = 0, pixel_start_top: int = 0):
        # Create and calculate grid
        self._check_value_links_are_valid(surface_width, surface_height,
                                          grid_width_max, grid_height_max)
        self._surface_width = surface_width
        self._surface_height = surface_height
        self._grid_width_max = grid_width_max
        self._grid_height_max = grid_height_max
        self._pixel_start_left = pixel_start_left
        self._pixel_start_top = pixel_start_top
        self._calculate_grid()

    @staticmethod
    def _check_value_links_are_valid(surface_width: int, surface_height: int,
                                     grid_width_max: int,
                                     grid_height_max: int) -> None:
        """Checks values which are inherently linked are valid before trying to
         set them.

        Parameters:
            surface_width (int): The width of the surface to base the grid on
                                 in pixels.
            surface_height (int): The height of the surface to base the grid on
                                  in pixels.
            grid_width_max (int): The max width point of the grid (right
                                  border).
            grid_height_max (int): The max height point of the grid (bottom
                                   border).
        """
        if surface_width < grid_width_max:
            raise GridCalculatorException("The grid width ({}) cannot be "
                                          "greater than the surface width "
                                          "({})".format(grid_width_max,
                                                        surface_width))
        if surface_height < grid_height_max:
            raise GridCalculatorException("The grid height ({}) cannot be "
                                          "greater than the surface height "
                                          "({})".format(grid_height_max,
                                                        surface_height))

    def _calculate_grid(self) -> None:
        """Calculate the grid used for other methods"""
        self._width_points, self._height_points = {0: 0}, {0: 0}
        w, h = 1, 1
        # Width point calculation
        while w <= self._grid_width_max:
            self._width_points[w] = \
                int((self._surface_width / self._grid_width_max) * w)
            w += 1
        # Height point calculation
        while h <= self._grid_height_max:
            self._height_points[h] = \
                int((self._surface_height / self._grid_height_max) * h)
            h += 1

    def width_points(self, point_needed: float) -> int:
        width = (self._surface_width - self._pixel_start_left) / \
                self._grid_width_max
        return int(width * point_needed)

    def __repr__(self):
        return "GridCalculator(pixel: width={}, height={};  grid: width={}, " \
               "height={})".format(
                    self._width_points.get(max(self._width_points)),
                    self._height_points.get(max(self._height_points)),
                    max(self._width_points.keys()),
                    max(self._height_points.keys()))

    def __sizeof__(self):
        return self.size

    @property
    def _surface_width(self) -> int:
        """Get surface width."""
        return self._s_width

    @_surface_width.setter
    def _surface_width(self, width: int) -> None:
        """Set surface width."""
        if width < 1:
            raise GridCalculatorException("Surface width must be greater than "
                                          "1")
        self._s_width = width

    @property
    def _surface_height(self) -> int:
        """Get surface height."""
        return self._s_height

    @_surface_height.setter
    def _surface_height(self, height: int) -> None:
        """Set surface height."""
        if height < 1:
            raise GridCalculatorException("Surface height must be greater than"
                                          " 1")
        self._s_height = height

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
        if pixel_start_left > self._surface_width:
            raise GridCalculatorException("The pixel start left position ({}) "
                                          "cannot be greater than the surface "
                                          "width ({})".format(
                                              pixel_start_left,
                                              self._surface_width))
        self._pix_start_left = pixel_start_left

    @property
    def _pixel_start_top(self) -> int:
        """Get pixel start top position."""
        return self._pix_start_top

    @_pixel_start_top.setter
    def _pixel_start_top(self, pixel_start_top: int) -> None:
        """Set pixel start top position."""
        if pixel_start_top > self._surface_height:
            raise GridCalculatorException("The pixel start top position ({}) "
                                          "cannot be greater than the surface "
                                          "height ({})".format(
                                              pixel_start_top,
                                              self._surface_height))
        self._pix_start_top = pixel_start_top

    def _error_check_left(self, left_point: int) -> None:
        """Left point error checking, checks left_point is in grid."""
        if left_point not in self._width_points:
            raise GridCalculatorException(
                "The left point provided ({}) isn't in the grid "
                "(0 - {})".format(left_point, max(self._width_points.keys())))

    def _error_check_top(self, top_point: int) -> None:
        """Top point error checking, checks top_point is in grid"""
        if top_point not in self._height_points:
            raise GridCalculatorException(
                "The top point provided ({}) isn't in the grid "
                "(0 - {})".format(top_point, max(self._height_points.keys())))

    def update_grid(self, grid_width_max: int, grid_height_max: int) -> None:
        """Recalculates the grid based on the provided width and height.

        Parameters:
            grid_width_max (int): The max width point of the grid (right
                                  border).
            grid_height_max (int): The max height point of the grid (bottom
                                   border)."""
        self._check_value_links_are_valid(self._surface_width,
                                          self._surface_height,
                                          grid_width_max, grid_height_max)
        self._grid_width_max = grid_width_max
        self._grid_height_max = grid_height_max
        self._calculate_grid()

    def update_surface(self, surface_width: int, surface_height: int) -> None:
        """Recalculates the surface size the grid is based on.

        Parameters:
            surface_width (int): The width of the surface to base the grid on
                                 in pixels.
            surface_height (int): The height of the surface to base the grid on
                                  in pixels."""
        self._check_value_links_are_valid(surface_width, surface_height,
                                          self._grid_width_max,
                                          self._grid_height_max)
        self._surface_width = surface_width
        self._surface_height = surface_height
        self._calculate_grid()

    @property
    def size(self) -> tuple:
        """Returns the size of the grid.

        Returns:
            tuple: The actual size of the grid (width, height)"""
        return len(self._width_points), len(self._height_points)

    @property
    def max_points(self) -> tuple:
        """Returns the max points of the grid.

        Returns:
            tuple: The max points of the grid (width, height)."""
        return max(self._width_points), max(self._height_points)

    def top_point(self, point: int) -> int:
        """Returns the pixel position of the top point specified.

        Parameters:
            point (int): The grid point required from the top of the grid.

        Returns:
            int: The pixel value represented by the top grid point."""
        self._error_check_top(point)
        return self._height_points.get(point)

    def left_point(self, point: int) -> int:
        """Returns the pixel position of the left point specified.

        Parameters:
            point (int): The grid point required from the left of the grid.

        Returns:
            int: The pixel value represented by the left grid point."""
        self._error_check_left(point)
        return self._width_points.get(point)

    def position(self, left_point: int, top_point: int) -> tuple:
        """Returns the pixel positions in the grid of the specified points in
        the format.

        Parameters:
            left_point(int): The grid point required from the left of the grid
            top_point (int): The grid point required from the top of the grid

        Returns:
            tuple: The pixel values represented by the grid points (left, top)
        """
        self._error_check_left(left_point)
        self._error_check_top(top_point)
        return self.left_point(left_point), self.top_point(top_point)

    def height_gap(self, top_point1: int, top_point2: int) -> int:
        """Returns the pixel gap between two specified top points.

        Parameters:
            top_point1 (int): The first top grid point to measure from.
            top_point2 (int): The second top grid point to measure to.

        Returns:
            int: The number of pixels between the two top points."""
        self._error_check_top(top_point1)
        self._error_check_top(top_point2)
        if top_point1 > top_point2:
            raise GridCalculatorException("top_point1 is greater than "
                                          "top_point2")

        return self.top_point(top_point2) - self.top_point(top_point1)

    def width_gap(self, left_point1: int, left_point2: int) -> int:
        """Returns the pixel gap between two specified left points.

        Parameters:
            left_point1 (int): The first left grid point to measure from.
            left_point2 (int): The second left grid point to measure to.

        Returns:
            int: The number of pixels between the two left points."""
        self._error_check_left(left_point1)
        self._error_check_left(left_point2)
        if left_point1 > left_point2:
            raise GridCalculatorException("left_point1 is greater than "
                                          "left_point2")

        return self.left_point(left_point2) - self.left_point(left_point1)

    def square(self, left_start: int, top_start: int, left_end: int,
               top_end: int) -> tuple:
        """Returns the total size of a square in pixels based on the top left
        point provided and bottom right point provided.

        Parameters:
            left_start (int): The left grid point for the top left of the
                              square
            top_start (int): The top grid point for the top left of the square
            left_end (int): The left grid point for the bottom right of the
                            square
            top_end (int): The top grid point for the bottom right of the
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

    def points_from_left(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the left border.

        Parameters:
            points (int): The number of grid points from the left border

        Returns:
            int: The left pixel value represented by the grid point."""
        self._error_check_left(points)
        return self.left_point(points)

    def points_from_top(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the top border.

        Parameters:
            points (int): The number of grid points from the left border

        Returns:
            int: The top pixel value represented by the grid point."""
        self._error_check_top(points)
        return self.top_point(points)

    def points_from_right(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the right border.

        Parameters:
            points (int): The number of grid points from the right border

        Returns:
            int: The left pixel value represented by the grid point."""
        self._error_check_left(max(self._width_points.keys()) - points)
        return self.left_point(max(self._width_points.keys()) - points)

    def points_from_bottom(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the bottom border.

        Parameters:
            points (int): The number of grid points from the bottom border

        Returns:
            int: The top pixel value represented by the grid point."""
        self._error_check_top(max(self._height_points.keys()) - points)
        return self.top_point(max(self._height_points.keys()) - points)

    def draw_grid_to_surface(self, surface: Surface) -> None:
        """Draws the grid to the pygame surface provided.

        Parameters:
            surface (pygame.Surface): The surface you want to show the grid
                                      on."""
        # Draw lines from left to right
        for left_point in self._width_points.keys():
            draw.line(surface, (0, 0, 0),
                      (self.left_point(left_point), self.top_point(0)),
                      (self.left_point(left_point),
                       self.top_point(max(self._height_points.keys()))))
        # Draw lines from top to bottom
        for top_point in self._height_points.keys():
            draw.line(surface, (0, 0, 0),
                      (self.left_point(0), self.top_point(top_point)),
                      (self.left_point(max(self._width_points.keys())),
                       self.top_point(top_point)))
