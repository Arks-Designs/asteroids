"""Module representing the player character"""

import pygame
from circleshape import CircleShape

class Player(CircleShape):
    """Class for the player character"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self):
        """Function for triangle representing character"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Function to draw the player"""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
