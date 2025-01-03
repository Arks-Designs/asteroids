"""Module representing asteroid object"""

import random
from math import cos, sin, radians
import pygame
from circleshape import CircleShape
from constants import ASTEROID_KILL_SCORE, ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SCORE

class Asteroid(CircleShape):
    """Class for the asteroid object"""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.look = self.generate_boundary()

    def generate_boundary(self):
        """Generate random points on the boundary"""
        angles = range(0, 360, 6)
        xs = [self.radius * sin(radians(angle)) + random.random() * (self.radius * .3) for angle in angles]
        ys = [self.radius * cos(radians(angle)) + random.random() * (self.radius * .3) for angle in angles]
        points = list(zip(xs, ys))
        points.append(points[0])
        return points

    def generate_position(self, boundary):
        """Given a boundary and a position returns the object"""
        return [(x + self.position.x, y + self.position.y) for x,y in boundary]

    def draw(self, screen):
        """Method draws the asteroid object"""
        # pygame.draw.circle(
        #     screen,
        #     "white",
        #     self.position,
        #     self.radius,
        #     2
        # )
        pygame.draw.polygon(
            screen,
            "white", 
            self.generate_position(self.look),
            2
        )

    def update(self, dt, screen=None):
        """Method to update the position of the asteroid"""
        self.position += (self.velocity * dt)
        if screen:
            self.position = self.wrap_position(screen)

    def split(self):
        """Method to split the asteroid"""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ASTEROID_KILL_SCORE
        angle = random.uniform(20,50)
        new_velo_1 = self.velocity.rotate(angle)
        new_velo_2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velo_1 * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velo_2 * 1.2
        return ASTEROID_SPLIT_SCORE
