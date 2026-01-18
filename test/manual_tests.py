"""This specifically covers tests that are visual in nature and can't be
   tested nicely using unittest."""

import pygame
from pygame_gridcalculator.gridcalculator import GridCalculator


def test_draw_grid_to_screen() -> None:
    """Test drawing the grid to the screen works correctly.
    TEST = All black lines should be evenly placed within green zones."""
    pygame.init()
    screen = pygame.display.set_mode((301, 301))

    # Draw visual gridlines for checking
    line_coords: list[dict] = [
        {"start": (0.0, 0.0), "end": (0.0, 300.0), "width": 5},
        {"start": (150.0, 0.0), "end": (150.0, 300.0), "width": 5},
        {"start": (300.0, 0.0), "end": (300.0, 300.0), "width": 5},
        {"start": (0.0, 0.0), "end": (300.0, 0.0), "width": 5},
        {"start": (0.0, 150.0), "end": (300.0, 150.0), "width": 5},
        {"start": (0.0, 300.0), "end": (300.0, 300.0), "width": 5}
    ]
    running = True
    while running:
        screen.fill((255, 255, 255))  # Just for local viewing

        for line in line_coords:
            start_pos: tuple[float, float] = line["start"]
            end_pos: tuple[float, float] = line["end"]
            width: int = line["width"]
            pygame.draw.line(screen, (153, 255, 204), start_pos,
                             end_pos, width)

        grid = GridCalculator(300, 300, 2, 2)
        # What is actually under test
        grid.draw_grid_to_surface(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pygame.display.update()


if __name__ == '__main__':
    test_draw_grid_to_screen()
