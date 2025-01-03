"""Module for creating weapons"""

# Base class for weapons
class Weapon():
    """Class representing a generic weapon"""
    def __init__(self, cooldown_timer, bullet_speed, bullet_radius):
        self.cooldown_timer = cooldown_timer
        self.cooldown = 0
        self.bullet_speed = bullet_speed
        self.bullet_radius = bullet_radius

    def shoot(self, position, rotation):
        """Module to shoot, intended to be overridden"""

    def update(self,dt):
        """Cooldown the shot"""
        self.cooldown = max(0, self.cooldown - dt)
