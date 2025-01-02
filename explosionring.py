"""Module to animate explosion"""

import random
import pygame
from circleshape import CircleShape

class ExplosionRing(CircleShape):
    """Class representing the explosion from an asteroid"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__color_index = 0
        self.__clock = 0

    EXPLOSION_COLORS = ["firebrick4", "firebrick1", "chocolate1", "darkorange", "darkgoldenrod1"]

    def update(self, dt):
        """Method to update explosion"""
        self.radius *= random.uniform(.5, 1.25)
        self.__clock += 1
        self.__color_index = (self.__color_index + 1) % len(ExplosionRing.EXPLOSION_COLORS)

    def draw(self, screen):
        """Method to draw explosion rings"""
        pygame.draw.circle(
            screen,
            ExplosionRing.EXPLOSION_COLORS[self.__color_index],
            self.position,
            self.radius
        )

    def get_decompose_clock(self):
        """Returns an update value on how long the explosion has lived"""
        return self.__clock
