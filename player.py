"""Module representing the player character"""

import pygame
from circleshape import CircleShape
from constants import PLAYER_ACCELERATION, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_STARTING_LIVES, SCREEN_WIDTH
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS
from shot import Shot

class Player(CircleShape):
    """Class for the player character"""
    def __init__(self, x, y, radius, lives=PLAYER_STARTING_LIVES):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_cooldown = 0
        self.lives = lives
        self.speed = 0

    def triangle(self):
        """Method for triangle representing character"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Method to draw the player"""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        """Method to rotate the player model"""
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        """Method to move the player forwards"""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * abs(dt)

    def shoot(self):
        """Method to shoot a shot"""
        if self.shot_cooldown <= 0:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0,1)
            new_shot.velocity = new_shot.velocity.rotate(self.rotation)
            new_shot.velocity.scale_to_length(PLAYER_SHOOT_SPEED)
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def accelerate(self, acceleration=PLAYER_ACCELERATION):
        """Method to accelerate the player"""
        if acceleration > 0:
            self.speed = min(PLAYER_SPEED, self.speed + acceleration)
        elif acceleration < 0:
            self.speed = max(-1 * PLAYER_SPEED, self.speed + acceleration)
        print(f"Speed: {self.speed}")

    def update(self, dt):
        """Method to interact with character model"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.accelerate(PLAYER_ACCELERATION)
            #self.move(dt)
        if keys[pygame.K_s]:
            self.accelerate(PLAYER_ACCELERATION * -1)
            #self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.move(dt)

        self.shot_cooldown = max(0, self.shot_cooldown - dt)

    def respawn(self, x, y):
        """Method to kill and respawn the player"""
        self.kill()
        return Player(x, y, self.radius, self.lives - 1)
    
    def write(self, screen):
        """Writes score on screen"""
        text_lives = '\u0394 ' * self.lives
        text = f"Remaining lives: {text_lives}"
        game_font = pygame.freetype.Font(None, 24)
        game_font.render_to(screen, (SCREEN_WIDTH - 275, 10), text, "yellow")
