"""This example file is a very basic version of the classic game Snake, using
the GridCalculator and the ShapeFactory to place objects on the screen in a
scalable way."""

import random
from enum import Enum

import pygame
import pygame.time
from pygame_gridcalculator import GridCalculator, ShapeFactory

pygame.init()
clock = pygame.time.Clock()


class Direction(Enum):
    # Enum for handling snake directions
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def determine_snake_direction(event: pygame.event, snake_direction: Direction) -> Direction:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and \
                snake_direction != Direction.DOWN:
            return Direction.UP
        elif event.key == pygame.K_RIGHT and \
                snake_direction != Direction.LEFT:
            return Direction.RIGHT
        elif event.key == pygame.K_DOWN and \
                snake_direction != Direction.UP:
            return Direction.DOWN
        elif event.key == pygame.K_LEFT and \
                snake_direction != Direction.RIGHT:
            return Direction.LEFT

    return snake_direction


def determine_snake_position(snake_direction: Direction, snake_head_top: int, snake_head_left: int) -> tuple:
    if snake_direction == Direction.UP:
        snake_head_top -= 1
        if snake_head_top == -1:
            snake_head_top = 9
    elif snake_direction == Direction.RIGHT:
        snake_head_left += 1
        if snake_head_left == 10:
            snake_head_left = 0
    elif snake_direction == Direction.DOWN:
        snake_head_top += 1
        if snake_head_top == 10:
            snake_head_top = 0
    elif snake_direction == Direction.LEFT:
        snake_head_left -= 1
        if snake_head_left == -1:
            snake_head_left = 9

    return snake_head_top, snake_head_left


def keep_game_running(event: pygame.event) -> bool:
    running = True

    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        # Keyboard button presses
        if event.key == pygame.K_ESCAPE:
            running = False

    return running


def start_snake_example() -> None:
    running = True
    display = pygame.display.set_mode((300, 300), pygame.RESIZABLE)
    display_height, display_width = display.get_height(), display.get_width()
    # Creates a grid for the whole screen, primarily for creating a border
    full_screen = GridCalculator(display_width, display_height, 12, 12)
    # Creates a second internal grid for the actual game to take place
    grid = GridCalculator(full_screen.points_from_right(1),
                          full_screen.points_from_bottom(1), 10, 10,
                          full_screen.points_from_left(1),
                          full_screen.points_from_top(1))
    # Game variables
    snake_head_left, snake_head_top = 5, 5
    snake_direction = Direction.DOWN
    snake_body = [{"left": snake_head_left, "top": snake_head_top}]
    fruit_left, fruit_top = 2, 2
    fps = 3

    while running:
        # Create a ShapeFactory for the internal grid
        shape_factory = ShapeFactory(grid)
        display.fill((0, 0, 0))

        for event in pygame.event.get():
            running = keep_game_running(event)
            if event.type == pygame.VIDEORESIZE:
                # On window resize, adjust grids accordingly
                display_height = event.h
                display_width = event.w
                full_screen.update_pixel_positions(display_width,
                                                   display_height)
                grid.update_pixel_positions(full_screen.points_from_right(1),
                                            full_screen.points_from_bottom(1),
                                            full_screen.points_from_left(1),
                                            full_screen.points_from_top(1))

            snake_direction = determine_snake_direction(event, snake_direction)

        # Draw border
        border = shape_factory.Rect(0, 0, grid.width_gap(0, 10),
                                    grid.height_gap(0, 10))
        pygame.draw.rect(display, (255, 255, 255), border)

        # Draw snake position
        get_positions = determine_snake_position(snake_direction, snake_head_top, snake_head_left)
        snake_head_top, snake_head_left = get_positions

        # Create the snake head
        head_rect = shape_factory.Rect(snake_head_left, snake_head_top,
                                       grid.width_gap(snake_head_left,
                                                      snake_head_left + 1),
                                       grid.height_gap(snake_head_top,
                                                       snake_head_top + 1))

        # Create the fruit
        fruit_rect = shape_factory.Rect(fruit_left, fruit_top,
                                        grid.width_gap(fruit_left,
                                                       fruit_left + 1),
                                        grid.height_gap(fruit_top,
                                                        fruit_top + 1))

        # If snake collides with its body, kill the game
        if {"left": snake_head_left, "top": snake_head_top} in snake_body:
            running = False

        # Updates the body based on movement
        snake_body.append({"left": snake_head_left, "top": snake_head_top})
        snake_body.remove(snake_body[0])

        # If snake head lands on fruit location
        if (snake_head_left, snake_head_top) == (fruit_left, fruit_top):
            # Snake head is on fruit, move fruit and extend snake
            move_fruit = True
            while move_fruit:
                # Make sure to pick a location not already occupied
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

        # Update display and tick clock
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    start_snake_example()
