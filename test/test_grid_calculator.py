import unittest
from pygame_gridcalculator.gridcalculator import GridCalculator, \
    GridCalculatorException


class TestGridCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_grid = GridCalculator(100, 100, 5, 5)
        self.test_grid2 = GridCalculator(10, 20, 5, 10)

    def test_init_grid_window_width_too_low(self) -> None:
        """Test initialising grid with 0 sized window width errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(0, 100, 10, 10)
        self.assertEqual(str(err.exception),
                         "Window width must be greater than 1")

    def test_init_grid_window_height_too_low(self) -> None:
        """Test initialising grid with 0 sized window height errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(100, 0, 10, 10)
        self.assertEqual(str(err.exception),
                         "Window height must be greater than 1")

    def test_init_grid_grid_width_too_low(self) -> None:
        """Test initialising grid with 0 sized grid width errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(100, 100, 0, 10)
        self.assertEqual(str(err.exception),
                         "Grid width must be greater than 1")

    def test_init_grid_grid_height_too_low(self) -> None:
        """Test initialising grid with 0 sized grid height errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(100, 100, 10, 0)
        self.assertEqual(str(err.exception),
                         "Grid height must be greater than 1")

    def test_init_grid_grid_width_bigger_than_window(self) -> None:
        """Test initialising grid with a window width smaller than the grid
        width errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(100, 100, 200, 10)
        self.assertEqual(str(err.exception),
                         "The grid width cannot be greater than the window "
                         "width")

    def test_init_grid_grid_height_bigger_than_window(self) -> None:
        """Test initialising grid with a window height smaller than the grid
        height errors"""
        with self.assertRaises(GridCalculatorException) as err:
            GridCalculator(100, 100, 10, 200)
        self.assertEqual(str(err.exception),
                         "The grid height cannot be greater than the window "
                         "height")

    def test_left_error_check_too_low(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_left(-1)
        self.assertEqual(str(err.exception),
                         "The left point provided (-1) isn't in the "
                         "grid (0 - 5)")

    def test_left_error_check_too_high(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_left(6)
        self.assertEqual(str(err.exception),
                         "The left point provided (6) isn't in the "
                         "grid (0 - 5)")

    def test_top_error_check_too_low(self) -> None:
        """Test the top error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_top(-1)
        self.assertEqual(str(err.exception),
                         "The top point provided (-1) isn't in the "
                         "grid (0 - 5)")

    def test_top_error_check_too_high(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_top(6)
        self.assertEqual(str(err.exception),
                         "The top point provided (6) isn't in the "
                         "grid (0 - 5)")

    def test_get_size(self) -> None:
        """Test the size of the grid is returned correctly."""
        self.assertEqual(self.test_grid.size, (6, 6))
        self.assertEqual(self.test_grid2.size, (6, 11))

    def test_get_max_points(self) -> None:
        """Test the max points of the grid is returned correctly."""
        self.assertEqual(self.test_grid.max_points, (5, 5))
        self.assertEqual(self.test_grid2.max_points, (5, 10))

    def test_top_point(self) -> None:
        """Test getting the top point returns the right value."""
        self.assertEqual(self.test_grid.top_point(0), 0)
        self.assertEqual(self.test_grid.top_point(1), 20)
        self.assertEqual(self.test_grid.top_point(2), 40)
        self.assertEqual(self.test_grid.top_point(3), 60)
        self.assertEqual(self.test_grid.top_point(4), 80)
        self.assertEqual(self.test_grid.top_point(5), 100)

        self.assertEqual(self.test_grid2.top_point(0), 0)
        self.assertEqual(self.test_grid2.top_point(1), 2)
        self.assertEqual(self.test_grid2.top_point(2), 4)
        self.assertEqual(self.test_grid2.top_point(3), 6)
        self.assertEqual(self.test_grid2.top_point(4), 8)
        self.assertEqual(self.test_grid2.top_point(5), 10)
        self.assertEqual(self.test_grid2.top_point(6), 12)
        self.assertEqual(self.test_grid2.top_point(7), 14)
        self.assertEqual(self.test_grid2.top_point(8), 16)
        self.assertEqual(self.test_grid2.top_point(9), 18)
        self.assertEqual(self.test_grid2.top_point(10), 20)

    def test_top_point_error(self) -> None:
        """Test getting the top point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.top_point(60)
        self.assertEqual(str(err.exception),
                         "The top point provided (60) isn't in the "
                         "grid (0 - 5)")

    def test_left_point(self) -> None:
        """Test getting the left point returns the right value."""
        self.assertEqual(self.test_grid.left_point(0), 0)
        self.assertEqual(self.test_grid.left_point(1), 20)
        self.assertEqual(self.test_grid.left_point(2), 40)
        self.assertEqual(self.test_grid.left_point(3), 60)
        self.assertEqual(self.test_grid.left_point(4), 80)
        self.assertEqual(self.test_grid.left_point(5), 100)

        self.assertEqual(self.test_grid2.left_point(0), 0)
        self.assertEqual(self.test_grid2.left_point(1), 2)
        self.assertEqual(self.test_grid2.left_point(2), 4)
        self.assertEqual(self.test_grid2.left_point(3), 6)
        self.assertEqual(self.test_grid2.left_point(4), 8)
        self.assertEqual(self.test_grid2.left_point(5), 10)

    def test_left_point_error(self) -> None:
        """Test getting the left point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.left_point(33)
        self.assertEqual(str(err.exception),
                         "The left point provided (33) isn't in the "
                         "grid (0 - 5)")

    def test_position(self) -> None:
        """Test getting the position returns the right value."""
        self.assertEqual(self.test_grid.position(1, 1), (20, 20))
        self.assertEqual(self.test_grid.position(3, 2), (60, 40))
        self.assertEqual(self.test_grid.position(4, 5), (80, 100))

        self.assertEqual(self.test_grid2.position(0, 0), (0, 0))
        self.assertEqual(self.test_grid2.position(2, 1), (4, 2))
        self.assertEqual(self.test_grid2.position(4, 5), (8, 10))
        self.assertEqual(self.test_grid2.position(5, 10), (10, 20))

    def test_position_error_left_point(self) -> None:
        """Test getting the left point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.position(9, 2)
        self.assertEqual(str(err.exception),
                         "The left point provided (9) isn't in the "
                         "grid (0 - 5)")

    def test_position_error_top_point(self) -> None:
        """Test getting the top point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.position(2, 8)
        self.assertEqual(str(err.exception),
                         "The top point provided (8) isn't in the "
                         "grid (0 - 5)")

    def test_height_gap(self) -> None:
        """Test getting the height gap returns the right value."""
        self.assertEqual(self.test_grid.height_gap(1, 2), 20)
        self.assertEqual(self.test_grid.height_gap(2, 4), 40)
        self.assertEqual(self.test_grid.height_gap(0, 5), 100)

    def test_height_gap_error_top_point1(self) -> None:
        """Test getting the first top point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.height_gap(-2, 3)
        self.assertEqual(str(err.exception),
                         "The top point provided (-2) isn't in the "
                         "grid (0 - 5)")

    def test_height_gap_error_top_point2(self) -> None:
        """Test getting the second top point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.height_gap(3, 10)
        self.assertEqual(str(err.exception),
                         "The top point provided (10) isn't in the "
                         "grid (0 - 5)")

    def test_height_gap_error_point1_higher_than_point2(self) -> None:
        """Test getting the second top point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.height_gap(4, 3)
        self.assertEqual(str(err.exception),
                         "top_point1 is greater than top_point2")

    def test_width_gap(self) -> None:
        """Test getting the width gap returns the right value."""
        self.assertEqual(self.test_grid.width_gap(3, 4), 20)
        self.assertEqual(self.test_grid.width_gap(0, 3), 60)
        self.assertEqual(self.test_grid.width_gap(0, 5), 100)

    def test_width_gap_error_left_point1(self) -> None:
        """Test getting the first left point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.height_gap(-2, 4)
        self.assertEqual(str(err.exception),
                         "The top point provided (-2) isn't in the "
                         "grid (0 - 5)")

    def test_width_gap_error_left_point2(self) -> None:
        """Test getting the second left point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.height_gap(0, 6)
        self.assertEqual(str(err.exception),
                         "The top point provided (6) isn't in the "
                         "grid (0 - 5)")

    def test_square(self) -> None:
        """Test getting the square returns the right values."""
        self.assertEqual(self.test_grid.square(0, 0, 2, 2), (40, 40))
        self.assertEqual(self.test_grid.square(1, 2, 2, 5), (20, 60))

    def test_square_error_left_start_invalid(self) -> None:
        """Test getting the left start point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(-4, 1, 2, 2)
        self.assertEqual(str(err.exception),
                         "The left point provided (-4) isn't in the "
                         "grid (0 - 5)")

    def test_square_error_top_start_invalid(self) -> None:
        """Test getting the top start point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(1, -2, 7, 2)
        self.assertEqual(str(err.exception),
                         "The top point provided (-2) isn't in the "
                         "grid (0 - 5)")

    def test_square_error_left_end_invalid(self) -> None:
        """Test getting the left end point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(1, 1, 7, 2)
        self.assertEqual(str(err.exception),
                         "The left point provided (7) isn't in the "
                         "grid (0 - 5)")

    def test_square_error_top_end_invalid(self) -> None:
        """Test getting the top end point returns an error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(1, 1, 3, 8)
        self.assertEqual(str(err.exception),
                         "The top point provided (8) isn't in the "
                         "grid (0 - 5)")

    def test_square_error_left_end_greater_than_left_start(self) -> None:
        """Test providing a left end larger than left start point returns an
        error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(4, 1, 3, 4)
        self.assertEqual(str(err.exception),
                         "left_start is greater than left_end")

    def test_square_error_top_end_greater_than_top_start(self) -> None:
        """Test providing a top end larger than top start point returns an
        error when invalid."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.square(1, 3, 3, 2)
        self.assertEqual(str(err.exception),
                         "top_start is greater than top_end")

    def test_points_from_left(self) -> None:
        """Test getting the points from left returns the right value."""
        self.assertEqual(self.test_grid.points_from_left(2), 40)
        self.assertEqual(self.test_grid.points_from_left(4), 80)

    def test_points_from_left_error(self) -> None:
        """Test providing an invalid points from left value doesn't work."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.points_from_left(7)
        self.assertEqual(str(err.exception),
                         "The left point provided (7) isn't in the "
                         "grid (0 - 5)")

    def test_points_from_top(self) -> None:
        """Test getting the points from top returns the right value."""
        self.assertEqual(self.test_grid.points_from_top(3), 60)
        self.assertEqual(self.test_grid.points_from_top(5), 100)

    def test_points_from_top_error(self) -> None:
        """Test providing an invalid points from top value doesn't work."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.points_from_top(8)
        self.assertEqual(str(err.exception),
                         "The top point provided (8) isn't in the "
                         "grid (0 - 5)")

    def test_points_from_right(self) -> None:
        """Test getting the points from right returns the right value."""
        self.assertEqual(self.test_grid.points_from_right(1), 80)
        self.assertEqual(self.test_grid.points_from_right(4), 20)

    def test_points_from_right_error(self) -> None:
        """Test providing an invalid points from right value doesn't work."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.points_from_right(6)
        self.assertEqual(str(err.exception),
                         "The left point provided (-1) isn't in the "
                         "grid (0 - 5)")

    def test_points_from_bottom(self) -> None:
        """Test getting the points from right returns the right value."""
        self.assertEqual(self.test_grid.points_from_bottom(2), 60)
        self.assertEqual(self.test_grid.points_from_bottom(4), 20)

    def test_points_from_bottom_error(self) -> None:
        """Test providing an invalid points from bottom value doesn't work."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid.points_from_bottom(7)
        self.assertEqual(str(err.exception),
                         "The top point provided (-2) isn't in the "
                         "grid (0 - 5)")


if __name__ == '__main__':
    unittest.main()
