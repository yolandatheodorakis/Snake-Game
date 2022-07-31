# File name: Food.py
# Author: Yolanda Theodorakis
# Description: Food class

import random
import pygame as pg

class Food:
    # Initialize the states
    def __init__(self):
        self.x_position = 700 / 2
        self.y_position = 700 / 4
        self.width = 10
        self.height = 10
        self.color = pg.Color(255, 153, 255)

    # Makes the food visible
    def draw_food(self, surface):
        self.food = pg.Rect(self.x_position, self.y_position, self.width, self.height)
        pg.draw.rect(surface, self.color, self.food)

    # Is the food eaten ie. do the food and snake's head collide
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Returns a new position for the food
    def new_position(self):
        self.x_position = random.randint(0, 700 - self.width)
        self.y_position = random.randint(0, 700 - self.height)
