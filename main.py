# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from scorecard import ScoreCard
from shot import Shot
from sys import exit

def main():
    """Function: Main game loop for asteroids game."""
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add all Player objects to both groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    #asteroid = Asteroid(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score_card = ScoreCard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        # Loop through groups
        for update_obj in updateable:
            update_obj.update(dt)

        for asteroid_obj in asteroids:
            if player.check_for_collision(asteroid_obj):
                print("Game over!")
                exit()

        for asteroid_obj in asteroids:
            for shot_obj in shots:
                if asteroid_obj.check_for_collision(shot_obj):
                    result = asteroid_obj.split()
                    score_card.increase(result)
                    shot_obj.kill()
                    #print(f"Score Card: result {result}, current score {score_card.score}, high score {score_card.high_score}")


        for draw_obj in drawable:
            draw_obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
