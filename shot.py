"""Module for creating bullets for our game"""

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    """Class for bullets"""
    def draw(self, screen):
        """Method to draw bullet"""
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        """Method to update position of shot"""
        self.position += (self.velocity * dt)
