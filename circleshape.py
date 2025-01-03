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

    def check_for_collision_triangle(self, other_triangleshape):
        """Method to check for collision between a circle object and a trianglular one"""
        # Check whether a vertex is in/on circle
        vert = other_triangleshape.triangle()
        for v in vert:
            if self.position.distance_to(v) <= self.radius:
                return True

        # Test whether circle in/on edge of triangle triangle
        for points in [(vert[0], vert[1]), (vert[1], vert[2]), (vert[2], vert[0])]:
            slope = points[1].y - points[0].y
            inter = points[1].x - points[0].x
            for i in range(round(min(points[0].x, points[1].x)), round(max(points[0].x, points[1].x)), 100):
                if self.position.distance_to((i,i * slope + inter)) <= self.radius:
                    return True

        return False

    def wrap_position(self, screen):
        """Method to wrap the object around the screen"""
        x = self.position.x % screen.get_width()
        y = self.position.y % screen.get_height()
        return pygame.Vector2(x,y)
