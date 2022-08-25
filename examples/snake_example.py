import pygame
import pygame.time
from pygame_gridcalculator import GridCalculator, ShapeFactory

FPS = 3

pygame.init()
clock = pygame.time.Clock()


def start_snake_example() -> None:
    running = True
    display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    display_height, display_width = display.get_height(), display.get_width()
    full_screen = GridCalculator(display_width, display_height, 12, 12)
    grid = GridCalculator(full_screen.points_from_right(1),
                          full_screen.points_from_bottom(1), 10, 10,
                          full_screen.points_from_left(1),
                          full_screen.points_from_top(1))
    snake_head_left, snake_head_top = 5, 5
    #snake_left, snake_down = True, True
    snake_direction = 3

    while running:
        shape_factory = ShapeFactory(grid)
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.VIDEORESIZE:
                display_height = event.h
                display_width = event.w
                full_screen.update_pixel_positions(display_width,
                                                   display_height)
                grid.update_pixel_positions(full_screen.points_from_right(1),
                                            full_screen.points_from_bottom(1),
                                            full_screen.points_from_left(1),
                                            full_screen.points_from_top(1))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_UP:
                    snake_direction = 1
                elif event.key == pygame.K_RIGHT:
                    snake_direction = 2
                elif event.key == pygame.K_DOWN:
                    snake_direction = 3
                elif event.key == pygame.K_LEFT:
                    snake_direction = 4

        # Draw border
        border = shape_factory.Rect(0, 0, grid.width_gap(0, 10),
                                    grid.height_gap(0, 10))
        pygame.draw.rect(display, (255, 255, 255), border)
        grid.draw_grid_to_surface(display)

        # Draw snake position
        if snake_direction == 1:  # Up
            snake_head_top -= 1
            if snake_head_top == -1:
                snake_head_top = 9
        elif snake_direction == 2:  # Right
            snake_head_left += 1
            if snake_head_left == 10:
                snake_head_left = 0
        elif snake_direction == 3:  # Down
            snake_head_top += 1
            if snake_head_top == 10:
                snake_head_top = 0
        elif snake_direction == 4:  # Left
            snake_head_left -= 1
            if snake_head_left == -1:
                snake_head_left = 9

        head_rect = shape_factory.Rect(snake_head_left, snake_head_top,
                                       grid.width_gap(snake_head_left,
                                                      snake_head_left + 1),
                                       grid.height_gap(snake_head_top,
                                                       snake_head_top + 1))
        pygame.draw.rect(display, (100, 255, 100), head_rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_snake_example()
