# File name: Snake.py
# Author: Yolanda Theodorakis
# Description: Snake class

import pygame as pg

class Snake:
    # Initialize the states
    def __init__(self):
        self.x_position = 700 / 2
        self.y_position = 700 / 2
        self.width = 10
        self.height = 10
        self.direction = 'stop'
        self.speed = 10
        self.body = []
        self.head_color = pg.Color(153, 204, 255)
        self.body_color = pg.Color(204, 229, 255)

    # Makes the snake visible
    def draw_snake(self, surface):
        self.segments = []
        self.head = pg.Rect(self.x_position, self.y_position, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:
            for unit in self.body:
                new_segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, new_segment)
                self.segments.append(new_segment)

    # Moves the snake in the direction of head
    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            x = self.body[index - 1][0]
            y = self.body[index - 1][1]
            self.body[index] = [x, y]
        if len(self.body) > 0:
            self.body[0] = [self.x_position, self.y_position]
        if self.direction == 'up':
            self.y_position -= self.speed
        if self.direction == 'down':
            self.y_position += self.speed
        if self.direction == 'left':
            self.x_position -= self.speed
        if self.direction == 'right':
            self.x_position += self.speed

    # Increases the length of the snake
    def increase_length(self):
        if len(self.body) != 0:
            index = len(self.body) - 1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x, y])
        else:
            self.body.append([1000, 1000])

    # Changes direction of the head
    def change_direction(self, direction):
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        if self.direction != 'right' and direction == 'left':
            self.direction = 'left'
        if self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        if self.direction != 'left' and direction == 'right':
            self.direction = 'right'

    # Check for collisions
    def is_collision(self):
        # Collision with itself
        for segment in self.segments:
            if self.head.colliderect(segment):
                return True
        # Collision with the screen's boundaries
        if (self.y_position < 0 or self.y_position > 700 - self.height
           or self.x_position < 0 or self.x_position > 700 - self.width):
           return True
