"""This example file shows some basic usage of the ShapeFactory.
It's not a particularly glamorous example, it just puts some shapes on the
surface for demonstration purposes."""

import pygame
import pygame.gfxdraw
from src.pygame_gridcalculator import GridCalculator, ShapeFactory

pygame.init()


def start_shapes_example():
    """This just shows the new draw grid to surface function"""
    running = True
    display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    display_height, display_width = display.get_height(), display.get_width()
    grid_width = 5
    grid_height = 5

    def calculate_grid() -> GridCalculator:
        """This just recalculates the grid"""
        return GridCalculator(display_width, display_height,
                              grid_width, grid_height)

    grid = calculate_grid()

    while running:
        display.fill((255, 255, 255))
        shape_factory = ShapeFactory(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.VIDEORESIZE:
                display_height = event.h
                display_width = event.w
                grid = calculate_grid()

        # Rect using ShapeFactory to place
        pygame.draw.rect(display, (255, 0, 0),
                         shape_factory.Rect(1, 2, 50, 50), 1)
        # Line using ShapeFactory
        shape_factory.draw_line(display, (255, 0, 255), (0, 0), (1, 1), 3)
        # Anti-aliased line using ShapeFactory
        shape_factory.draw_aaline(display, (255, 0, 255), (1, 0), (2, 1), 1)
        # Polygon using ShapeFactory
        shape_factory.draw_polygon(display, (255, 255, 0),
                                   [(2, 1), (3, 2), (4, 2), (4, 1)], 5)
        # Circles using ShapeFactory
        shape_factory.draw_circle(display, (255, 0, 255), (1, 4), 15, 3,
                                  False, True, False, True)
        shape_factory.draw_circle(display, (0, 255, 255), (1, 4), 15, 3,
                                  True, False, True, False)
        # Lines using ShapeFactory
        shape_factory.draw_lines(display, (100, 200, 100), False,
                                 [(1, 4), (2, 3), (3, 4), (4, 4)], 3)
        # Anti-aliased line using ShapeFactory
        shape_factory.draw_aalines(display, (200, 200, 100), False,
                                   [(1, 5), (2, 4), (3, 3), (4, 4)], 3)

        pygame.display.update()


if __name__ == "__main__":
    start_shapes_example()
