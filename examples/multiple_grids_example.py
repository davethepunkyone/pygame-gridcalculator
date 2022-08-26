"""This example file shows how multiple grids can be used on the same display,
and how grids can be placed within grids."""

import pygame
import pygame.time
from src.pygame_gridcalculator import GridCalculator, ShapeFactory

pygame.init()


def multiple_grids_example():
    """This draws a grid and triangle and shrinks/grows the grid"""
    running = True
    display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    display_height, display_width = display.get_height(), display.get_width()
    grid_width = 6
    grid_height = 5
    grid = GridCalculator(display_width, display_height, grid_width,
                          grid_height, 100, 100)
    grid2 = GridCalculator(100, 100, grid_width, grid_height)
    grid3 = GridCalculator(display_width, 100, 3, 3, pixel_start_left=100)
    grid4 = GridCalculator(100, display_height, 2, 7, pixel_start_top=100)
    grid_in_grid = GridCalculator(grid.left_point(5), grid.top_point(2), 3, 3,
                                  grid.left_point(4), grid.top_point(1))

    while running:
        shape_factory = ShapeFactory(grid)
        display.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.VIDEORESIZE:
                display_height = event.h
                display_width = event.w
                if display_height < 105 or display_width < 105:
                    pygame.display.set_mode((200, 200), pygame.RESIZABLE)
                grid.update_pixel_positions(display_width, display_height, 100,
                                            100)
                grid3.update_pixel_positions(display_width, 100,
                                             pixel_start_left=100)
                grid4.update_pixel_positions(100, display_height,
                                             pixel_start_top=100)
                grid_in_grid.update_pixel_positions(grid.left_point(5),
                                                    grid.top_point(2),
                                                    grid.left_point(4),
                                                    grid.top_point(1))

        # Draw the grid to display
        grid.draw_grid_to_surface(display)
        grid2.draw_grid_to_surface(display, (0, 255, 0))
        grid3.draw_grid_to_surface(display, (255, 0, 100))
        grid4.draw_grid_to_surface(display, (100, 200, 50))
        grid_in_grid.draw_grid_to_surface(display, (50, 50, 255))
        shape_factory.draw_polygon(display, (255, 0, 0),
                                   [(1, 4), (3, 1), (5, 4)], 3)
        pygame.draw.line(display, (0, 255, 0), (grid.left_point(0.5),
                                                grid.top_point(0.5)),
                         (grid.left_point(3), grid.top_point(3)), 3)
        pygame.draw.line(display, (0, 0, 255), (grid.left_point(1),
                                                grid.top_point(1)),
                         (grid.left_point(3), grid.top_point(3)), 3)

        pygame.display.update()


if __name__ == "__main__":
    multiple_grids_example()
