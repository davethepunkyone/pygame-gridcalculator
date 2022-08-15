"""This example file shows some usage of the grid update_grid and
update_surface methods, resizing the grid every second and shrinking the
surface size when the grid grows in size."""

import pygame
import pygame.time
from pygame_gridcalculator import GridCalculator, ShapeFactory

FPS = 60

pygame.init()
clock = pygame.time.Clock()


def grid_resize_example():
    """This draws a grid and triangle and shrinks/grows the grid"""
    running = True
    display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    display_height, display_width = display.get_height(), display.get_width()
    grid_width = 6
    grid_height = 5
    countdown = FPS
    increase_grid = True
    grid = GridCalculator(display_width, display_height, grid_width,
                          grid_height)

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
                grid.update_surface(display_width, display_height)

        # Draw the grid to display
        grid.draw_grid_to_surface(display)
        shape_factory.draw_polygon(display, (255, 0, 0),
                                   [(1, 4), (3, 1), (5, 4)], 3)

        if countdown == 0:
            countdown = FPS
            if increase_grid:
                grid_width += 1
                grid_height += 1
                if display_width > 100 and display_height > 100:
                    grid.update_surface(display_width - 100,
                                        display_height - 100)
                if grid_width > 15:
                    increase_grid = False
            else:
                grid_width -= 1
                grid_height -= 1
                grid.update_surface(display_width, display_height)
                if grid_width < 6:
                    increase_grid = True
            grid.update_grid(grid_width, grid_height)

        else:
            countdown -= 1

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    grid_resize_example()
