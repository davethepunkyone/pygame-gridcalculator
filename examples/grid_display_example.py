"""This example file shows some basic usage of the GridCalculator and how it
displays a grid on the screen.  Also includes putting some shapes on the screen
to show how the grid works and the ability to expand/reduce the grid to show
how shapes scale with the grid."""

import pygame
import pygame.gfxdraw
from gridcalculator import GridCalculator

pygame.init()


def grid_display_example():
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

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.VIDEORESIZE:
                display_height = event.h
                display_width = event.w
                grid = calculate_grid()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Draw the grid to display
        grid.draw_grid_to_surface(display)

        # Initialise font for buttons
        font_to_use = pygame.font.Font(pygame.font.get_default_font(),
                                       grid.height_gap(0, 1))

        # Draw squares to display
        expand_sq = pygame.draw.rect(display, (0, 255, 0),
                                     pygame.Rect(grid.left_point(0),
                                                 grid.top_point(0),
                                                 grid.width_gap(0, 1),
                                                 grid.height_gap(0, 1)))

        expand_txt = font_to_use.render("+", True, (10, 10, 10))
        expand_text_rect = expand_txt.get_rect()
        expand_text_rect.topleft = (grid.left_point(0) +
                                    ((grid.width_gap(0, 1) / 2) -
                                     (expand_text_rect.width / 2)),
                                    grid.top_point(0))
        display.blit(expand_txt, expand_text_rect)

        reduce_sq = pygame.draw.rect(display, (255, 255, 0),
                                     pygame.Rect(grid.left_point(1),
                                                 grid.top_point(0),
                                                 grid.width_gap(1, 2),
                                                 grid.height_gap(0, 1)))

        reduce_txt = font_to_use.render("-", True, (10, 10, 10))
        reduce_text_rect = expand_txt.get_rect()
        reduce_text_rect.topleft = (grid.left_point(1) +
                                    (grid.width_gap(1, 2) / 2) -
                                    (reduce_text_rect.width / 2),
                                    grid.top_point(0))
        display.blit(reduce_txt, reduce_text_rect)

        mx, my = pygame.mouse.get_pos()
        if expand_sq.collidepoint(mx, my) and click:
            grid_width += 1
            grid_height += 1
            grid = calculate_grid()
        if reduce_sq.collidepoint(mx, my) and click and \
                grid_width > 5 and grid_height > 5:
            grid_width -= 1
            grid_height -= 1
            grid = calculate_grid()

        # Draw red circle
        pygame.gfxdraw.filled_ellipse(display,
                                      grid.left_point(4), grid.top_point(4),
                                      grid.width_gap(3, 4),
                                      grid.height_gap(3, 4),
                                      (255, 0, 0))

        # Draw x with lines
        pygame.draw.line(display, (0, 255, 255),
                         (grid.left_point(1), grid.top_point(2)),
                         (grid.left_point(2), grid.top_point(3)), 2)
        pygame.draw.line(display, (0, 255, 255),
                         (grid.left_point(1), grid.top_point(3)),
                         (grid.left_point(2), grid.top_point(2)), 2)

        # Draw polygon
        polygon_points = [(grid.left_point(4), grid.top_point(0)),
                          (grid.left_point(5), grid.top_point(1)),
                          (grid.left_point(3), grid.top_point(3)),
                          (grid.left_point(3), grid.top_point(2))]
        pygame.gfxdraw.filled_polygon(display, polygon_points, (255, 100, 125))
        pygame.draw.polygon(display, (150, 230, 175), polygon_points, 3)

        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    grid_display_example()
