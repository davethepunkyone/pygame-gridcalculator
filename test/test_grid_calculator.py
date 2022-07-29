import unittest
from src.pygame_gridcalculator import GridCalculator, GridCalculatorException


class TestGridCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_grid = GridCalculator(100, 100, 5, 5)
        self.test_grid2 = GridCalculator(10, 20, 5, 10)

    def test_left_error_check_too_low(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_left(-1)
            self.assertEqual(err, "The left point provided (-1) isn't in the "
                                  "grid  (0 - 5)")

    def test_left_error_check_too_high(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_left(6)
            self.assertEqual(err, "The left point provided (6) isn't in the "
                                  "grid  (0 - 5)")

    def test_top_error_check_too_low(self) -> None:
        """Test the top error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_top(-1)
            self.assertEqual(err, "The top point provided (-1) isn't in the "
                                  "grid  (0 - 5)")

    def test_top_error_check_too_high(self) -> None:
        """Test the left error check."""
        with self.assertRaises(GridCalculatorException) as err:
            self.test_grid._error_check_top(6)
            self.assertEqual(err, "The top point provided (6) isn't in the "
                                  "grid  (0 - 5)")

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
            self.assertEqual(err, "The top point provided (60) isn't in the "
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
            self.assertEqual(err, "The left point provided (33) isn't in the "
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

    def test_height_gap(self) -> None:
        """Test getting the height gap returns the right value."""
        self.assertEqual(self.test_grid.height_gap(1, 2), 20)
        self.assertEqual(self.test_grid.height_gap(2, 4), 40)
        self.assertEqual(self.test_grid.height_gap(0, 5), 100)

    def test_width_gap(self) -> None:
        """Test getting the width gap returns the right value."""
        self.assertEqual(self.test_grid.width_gap(3, 4), 20)
        self.assertEqual(self.test_grid.width_gap(0, 3), 60)
        self.assertEqual(self.test_grid.width_gap(0, 5), 100)

    def test_square(self) -> None:
        """Test getting the square returns the right values."""
        self.assertEqual(self.test_grid.square(0, 0, 2, 2), (40, 40))
        self.assertEqual(self.test_grid.square(1, 2, 2, 5), (20, 60))

    def test_points_from_left(self) -> None:
        """Test getting the points from left returns the right value."""
        self.assertEqual(self.test_grid.points_from_left(2), 40)
        self.assertEqual(self.test_grid.points_from_left(4), 80)

    def test_points_from_top(self) -> None:
        """Test getting the points from top returns the right value."""
        self.assertEqual(self.test_grid.points_from_top(3), 60)
        self.assertEqual(self.test_grid.points_from_top(5), 100)

    def test_points_from_right(self) -> None:
        """Test getting the points from right returns the right value."""
        self.assertEqual(self.test_grid.points_from_right(1), 80)
        self.assertEqual(self.test_grid.points_from_right(4), 20)

    def test_points_from_bottom(self) -> None:
        """Test getting the points from right returns the right value."""
        self.assertEqual(self.test_grid.points_from_bottom(2), 60)
        self.assertEqual(self.test_grid.points_from_bottom(4), 20)


if __name__ == '__main__':
    unittest.main()
