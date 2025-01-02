"""Module for creating a circle object in game"""

import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    """ Class representing a generic circle in game"""

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Method to draw object, intended to be overwritten by children"""
        # sub-classes must override
        pass

    def update(self, dt, screen=None):
        """Method to update object, intended to be overwritten"""
        # sub-classes must override
        pass

    def check_for_collision(self, other_circleshape):
        """Method to determine if two circles collide"""
        dist = self.position.distance_to(other_circleshape.position)
        combined_radius = self.radius + other_circleshape.radius
        return dist <= combined_radius

    def wrap_position(self, screen):
        """Method to wrap the object around the screen"""
        x = self.position.x % screen.get_width()
        y = self.position.y % screen.get_height()
        return pygame.Vector2(x,y)
