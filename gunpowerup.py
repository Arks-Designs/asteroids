"""Module to power up player"""

import pygame
from circleshape import CircleShape
from constants import *
from shotgun import ShotGun

class GunPowerUp(CircleShape):
    """Class to power up the player"""

    def draw(self, screen):
        """Method to draw the powerup"""
        pygame.draw.circle(
            screen,
            "orange",
            self.position,
            self.radius,
            2
        )

    def power_up(self, player):
        """Power up the player"""
        player.weapon = ShotGun(PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, SHOT_RADIUS)
