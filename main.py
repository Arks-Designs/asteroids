# this allows us to use code from
# the open-source pygame library
# throughout this file
from sys import exit
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from scorecard import ScoreCard
from explosionring import ExplosionRing
from shot import Shot

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
    explosions = pygame.sprite.Group()

    # Add all Player objects to both groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    ExplosionRing.containers = (explosions, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    background = pygame.image.load(BACKGROUND_PATH)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    #lives = PLAYER_STARTING_LIVES
    #asteroid = Asteroid(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    score_card = ScoreCard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        screen.blit(background, (0,0))

        # Loop through groups
        for update_obj in updateable:
            update_obj.update(dt, screen)

        for asteroid_obj in asteroids:
            if player.check_for_collision(asteroid_obj):
                if player.lives > 0:
                    player = player.respawn(x, y)
                    for asteroid_obj in asteroids:
                        asteroid_obj.kill()
                    break
                print("Game over!")
                if score_card.get_high_score() < score_card.get_score():
                    score_card.save_high_score()
                    print(f"New high score: {score_card.get_high_score()}!!")
                exit()

        for asteroid_obj in asteroids:
            for shot_obj in shots:
                if asteroid_obj.check_for_collision(shot_obj):
                    explosion = ExplosionRing(
                        asteroid_obj.position.x,
                        asteroid_obj.position.y,
                        asteroid_obj.radius
                    )
                    result = asteroid_obj.split()
                    score_card.increase(result)
                    shot_obj.kill()
                    #print(f"Score Card: result {result}, current score {score_card.score}, high score {score_card.high_score}")

        for draw_obj in drawable:
            draw_obj.draw(screen)

        for explosion_obj in explosions:
            if explosion_obj.get_decompose_clock() >= 30:
                explosion_obj.kill()

        score_card.write(screen)
        player.write(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
