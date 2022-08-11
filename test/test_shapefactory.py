import unittest
import pygame
from pygame_gridcalculator.gridcalculator import GridCalculator
from pygame_gridcalculator.shapefactory import ShapeFactory


class TestShapeFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.test_surface = pygame.Surface((100, 100))
        self.test_grid = GridCalculator(100, 100, 4, 4)
        self.test_shape_factory = ShapeFactory(self.test_grid)

    def test_init(self) -> None:
        """Test initialising ShapeFactory with a grid."""
        result = ShapeFactory(GridCalculator(10, 10, 5, 5))
        self.assertIsInstance(result, ShapeFactory)

    def test_Rect(self) -> None:
        """Test getting a Rect from the test ShapeFactory."""
        result = self.test_shape_factory.Rect(1, 1, 20, 30)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 25)
        self.assertEqual(result.top, 25)
        self.assertEqual(result.width, 20)
        self.assertEqual(result.height, 30)

    def test_draw_line(self) -> None:
        """Test getting a pygame.draw.line from the test ShapeFactory"""
        result = self.test_shape_factory.draw_line(self.test_surface,
                                                   (255, 0, 0), (1, 1), (2, 2),
                                                   1)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 25)
        self.assertEqual(result.top, 25)
        self.assertEqual(result.width, 26)
        self.assertEqual(result.height, 26)

    def test_draw_lines(self) -> None:
        """Test getting a pygame.draw.lines from the test ShapeFactory"""
        result = self.test_shape_factory.draw_lines(self.test_surface,
                                                    (255, 0, 0), False,
                                                    [(1, 1), (2, 2), (3, 1)],
                                                    1)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 25)
        self.assertEqual(result.top, 25)
        self.assertEqual(result.width, 51)
        self.assertEqual(result.height, 26)

    def test_draw_aaline(self) -> None:
        """Test getting a pygame.draw.aaline from the test ShapeFactory"""
        result = self.test_shape_factory.draw_aaline(self.test_surface,
                                                     (255, 0, 0), (2, 2),
                                                     (3, 3), 1)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 50)
        self.assertEqual(result.top, 50)
        self.assertEqual(result.width, 26)
        self.assertEqual(result.height, 26)

    def test_draw_aalines(self) -> None:
        """Test getting a pygame.draw.aalines from the test ShapeFactory"""
        result = self.test_shape_factory.draw_aalines(self.test_surface,
                                                      (255, 0, 0), False,
                                                      [(1, 3), (2, 2), (3, 1)],
                                                      1)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 25)
        self.assertEqual(result.top, 25)
        self.assertEqual(result.width, 51)
        self.assertEqual(result.height, 51)

    def test_draw_polygon(self) -> None:
        """Test getting a pygame.draw.polygon from the test ShapeFactory"""
        result = self.test_shape_factory.draw_polygon(self.test_surface,
                                                      (255, 0, 0),
                                                      [(2, 2), (3, 3), (4, 3),
                                                       (4, 2)], 1)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 50)
        self.assertEqual(result.top, 50)
        self.assertEqual(result.width, 50)
        self.assertEqual(result.height, 26)

    def test_draw_circle(self) -> None:
        """Test getting a pygame.draw.polygon from the test ShapeFactory"""
        result = self.test_shape_factory.draw_circle(self.test_surface,
                                                     (255, 0, 0), (2, 2), 5)
        self.assertIsInstance(result, pygame.Rect)
        self.assertEqual(result.left, 45)
        self.assertEqual(result.top, 45)
        self.assertEqual(result.width, 10)
        self.assertEqual(result.height, 10)
