from src.exceptions import GridCalculatorException


class GridCalculator:
    """Create a GridCalculator to map the available pixels on the screen
       against a grid of the users size.

    Parameters:
        window_width (int): The width of the window to base the grid on
        window_height (int): The height of the window to base the grid on
        grid_width_max (int): The max width point of the grid
        grid_height_max (int): The max height point of the grid"""

    def __init__(self, window_width: int, window_height: int,
                 grid_width_max: int, grid_height_max: int):
        self._width_points = {}
        self._height_points = {}
        # Width point calculation
        self._width_points[0] = 0
        w, h = 1, 1
        while w <= grid_width_max:
            self._width_points[w] = int((window_width / grid_width_max) * w)
            w += 1
        # Height point calculation
        self._height_points[0] = 0
        while h <= grid_height_max:
            self._height_points[h] = int((window_height / grid_height_max) * h)
            h += 1

    def __repr__(self):
        return "GridCalculator(pixel: width={}, height={}; " \
               "grid: width={}, height={})".format(
                   self._width_points.get(max(self._width_points)),
                   self._height_points.get(max(self._height_points)),
                   max(self._width_points.keys()),
                   max(self._height_points.keys()))

    def __sizeof__(self):
        return self.size

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

        return self._height_points.get(point)

    def left_point(self, point: int) -> int:
        """Returns the pixel position of the left point specified.

        Parameters:
            point (int): The grid point required from the left of the grid.

        Returns:
            int: The pixel value represented by the left grid point."""

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

        return self.left_point(left_point), self.top_point(top_point)

    def height_gap(self, top_point1: int, top_point2: int) -> int:
        """Returns the pixel gap between two specified top points.

        Parameters:
            top_point1 (int): The first top grid point to measure from.
            top_point2 (int): The second top grid point to measure to.

        Returns:
            int: The number of pixels between the two top points."""
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
        if left_start > left_end:
            raise GridCalculatorException("left_start is greater than "
                                          "left_end")
        if top_start > top_end:
            raise GridCalculatorException("top_start is greater than top_end")

        return self.width_gap(left_start, left_end), \
            self.height_gap(top_start, top_end)

    def points_from_left(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the left border.

        Parameters:
            points (int): The number of grid points from the left border

        Returns:
            int: The left pixel value represented by the grid point."""

        return self.left_point(points)

    def points_from_top(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the top border.

        Parameters:
            points (int): The number of grid points from the left border

        Returns:
            int: The top pixel value represented by the grid point."""

        return self.top_point(points)

    def points_from_right(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the right border.

        Parameters:
            points (int): The number of grid points from the right border

        Returns:
            int: The left pixel value represented by the grid point."""

        return self.left_point(max(self._width_points.keys()) - points)

    def points_from_bottom(self, points: int) -> int:
        """Returns the pixel position from the specified number of points from
        the bottom border.

        Parameters:
            points (int): The number of grid points from the bottom border

        Returns:
            int: The top pixel value represented by the grid point."""

        return self.top_point(max(self._height_points.keys()) - points)
