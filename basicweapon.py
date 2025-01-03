"""Define the basic weapon"""

import pygame
from weapons import Weapon
from shot import Shot

class BasicWeapon(Weapon):
    """Class representing the basic weapon"""

    def shoot(self, position, rotation):
        """Class to shoot"""
        if self.cooldown <= 0:
            new_shot = Shot(position.x, position.y, self.bullet_radius)
            new_shot.velocity = pygame.Vector2(0,1)
            new_shot.velocity = new_shot.velocity.rotate(rotation)
            new_shot.velocity.scale_to_length(self.bullet_speed)
            self.cooldown = self.cooldown_timer
