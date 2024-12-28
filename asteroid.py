"""Module representing asteroid object"""

import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    """Class for the asteroid object"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Method draws the asteroid object"""
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        """Method to update the position of the asteroid"""
        self.position += (self.velocity * dt)
