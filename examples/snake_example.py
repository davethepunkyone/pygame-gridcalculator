import random

import pygame
import pygame.time
from pygame_gridcalculator import GridCalculator, ShapeFactory

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
    snake_direction = 3
    snake_body = [{"left": snake_head_left, "top": snake_head_top}]
    fruit_left, fruit_top = 2, 2
    fps = 3
    pause_menu = False

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
                if event.key == pygame.K_UP and snake_direction != 3:
                    snake_direction = 1
                elif event.key == pygame.K_RIGHT and snake_direction != 4:
                    snake_direction = 2
                elif event.key == pygame.K_DOWN and snake_direction != 1:
                    snake_direction = 3
                elif event.key == pygame.K_LEFT and snake_direction != 2:
                    snake_direction = 4

        # Draw border
        border = shape_factory.Rect(0, 0, grid.width_gap(0, 10),
                                    grid.height_gap(0, 10))
        pygame.draw.rect(display, (255, 255, 255), border)

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

        fruit_rect = shape_factory.Rect(fruit_left, fruit_top,
                                        grid.width_gap(fruit_left,
                                                       fruit_left + 1),
                                        grid.height_gap(fruit_top,
                                                        fruit_top + 1))

        if {"left": snake_head_left, "top": snake_head_top} in snake_body:
            running = False

        snake_body.append({"left": snake_head_left, "top": snake_head_top})
        snake_body.remove(snake_body[0])

        if (snake_head_left, snake_head_top) == (fruit_left, fruit_top):
            # Snake head is on fruit, move fruit and extend snake
            snake_extend = True
            move_fruit = True
            while move_fruit:
                new_fruit_left = random.randint(0, 9)
                new_fruit_top = random.randint(0, 9)
                if not {"left": new_fruit_left, "top": new_fruit_top} in \
                        snake_body:
                    move_fruit = False
                    fruit_left, fruit_top = new_fruit_left, new_fruit_top
            fps += 0.5
            snake_body.append({"left": snake_head_left, "top": snake_head_top})

        for body_part in snake_body:
            # Draw the snake body parts
            pygame.draw.rect(display, (100, 200, 100),
                             shape_factory.Rect(body_part["left"],
                                                body_part["top"],
                                                grid.width_gap(
                                                    body_part["left"],
                                                    body_part["left"] + 1),
                                                grid.height_gap(
                                                    body_part["top"],
                                                    body_part["top"] + 1)))

        # Draw the fruit and head on the screen
        pygame.draw.rect(display, (200, 50, 50), fruit_rect)
        pygame.draw.rect(display, (100, 255, 100), head_rect)

        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    start_snake_example()
