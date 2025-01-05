"""Module to power up player"""

import pygame
from circleshape import CircleShape
from constants import *

class SpeedPowerUp(CircleShape):
    """Class to power up the player"""

    def draw(self, screen):
        """Method to draw the powerup"""
        pygame.draw.circle(
            screen,
            "purple",
            self.position,
            self.radius,
            2
        )

    def power_up(self, player):
        """Power up the player"""
        player.gain_speed_boost()
