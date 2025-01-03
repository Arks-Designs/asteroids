"""Define the shotgun weapon"""

import pygame
from weapons import Weapon
from shot import Shot

class ShotGun(Weapon):
    """Class representing the basic weapon"""

    def shoot(self, position, rotation):
        """Class to shoot"""
        if self.cooldown <= 0:
            new_shot1 = Shot(position.x, position.y, self.bullet_radius)
            new_shot1.velocity = pygame.Vector2(0,1)
            new_shot1.velocity = new_shot1.velocity.rotate(rotation)
            new_shot1.velocity.scale_to_length(self.bullet_speed)

            new_shot2 = Shot(position.x, position.y, self.bullet_radius)
            new_shot2.velocity = pygame.Vector2(0,1)
            new_shot2.velocity = new_shot2.velocity.rotate(rotation-15)
            new_shot2.velocity.scale_to_length(self.bullet_speed)

            new_shot3 = Shot(position.x, position.y, self.bullet_radius)
            new_shot3.velocity = pygame.Vector2(0,1)
            new_shot3.velocity = new_shot3.velocity.rotate(rotation+15)
            new_shot3.velocity.scale_to_length(self.bullet_speed)
            self.cooldown = self.cooldown_timer
