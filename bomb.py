"""Module to create a bomb"""

import pygame
from circleshape import CircleShape

class Bomb(CircleShape):
    """Class to create a bomb"""

    def draw(self, screen):
        """Method to draw the bomb"""
        pygame.draw.circle(
            screen,
            "red",
            self.position,
            self.radius,
            5
        )
