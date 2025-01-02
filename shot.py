"""Module for creating bullets for our game"""

import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    """Class for bullets"""
    def draw(self, screen):
        """Method to draw bullet"""
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt, screen=None):
        """Method to update position of shot"""
        self.position += (self.velocity * dt)
