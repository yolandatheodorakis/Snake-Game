# File name: Game.py
# Author: Yolanda Theodorakis
# Description: Snake game

import pygame as pg
import time
import Snake as snake
import Food as food

# Variable for the game display
window = pg.display.set_mode((700, 700))

# Colors
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)

# Variables for scrores
score, high_score = (0, 0)


# Displays the score on the screen
def show_score(surface):
    global high_score
    font_name = pg.font.match_font('arial')

    # Update the highest score
    if score > high_score:
        high_score = score

    # Writing the score
    font = pg.font.Font(font_name, 18)
    text1_surface = font.render('Score: {}'.format(score), True, white)
    text1_rect = text1_surface.get_rect()
    text1_rect.midtop = (350, 10)
    surface.blit(text1_surface, text1_rect)
    text2_surface = font.render('High Score: {}'.format(high_score), True, white)
    text2_rect = text2_surface.get_rect()
    text2_rect.midtop = (350, 30)
    surface.blit(text2_surface, text2_rect)


# What to do when the game is over
def game_over():
    global score

    # Write 'game over' to the screen
    game_over_font = pg.font.Font('freesansbold.ttf', 24)
    game_over_surface = game_over_font.render('Game Over :(', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (350, 300)
    window.blit(game_over_surface, game_over_rect)

    # Reset score
    score = 0
    pg.display.flip()
    time.sleep(3)

    # Re-initialize game
    run = True
    fd = food.Food()
    s = snake.Snake()
    play_game(fd, s)


# The game
def play_game(food_object, snake_object):
    global score
    run = True
    while run:
        # FPS
        clock = pg.time.Clock()
        clock.tick(30)

        # Catches all the events that have happened since the game started
        for event in pg.event.get():
            # When you press the 'close window' button
            if event.type == pg.QUIT:
                run = False

        # Display the score, snake, and food
        window.fill(black)
        food_object.draw_food(window)
        snake_object.draw_snake(window)
        show_score(window)

        # User input
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]:
            snake_object.change_direction('up')
        if pressed[pg.K_LEFT]:
            snake_object.change_direction('left')
        if pressed[pg.K_DOWN]:
            snake_object.change_direction('down')
        if pressed[pg.K_RIGHT]:
            snake_object.change_direction('right')

        # Move the snake
        snake_object.move()

        # Eat
        if food_object.is_eaten(snake_object.head):
            food_object.new_position()
            snake_object.increase_length()
            score += 10
        # Check for collisions
        if snake_object.is_collision():
            run = False
            game_over()

        # Update the game display
        pg.display.update()


# The main function
def main():
    # Initialize pygame
    pg.init()

    pg.display.set_caption('A game of Snake')
    fd = food.Food()
    s = snake.Snake()
    play_game(fd, s)

    # Exits pygame
    pg.quit()

main()
