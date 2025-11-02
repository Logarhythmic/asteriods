import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collide_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
        for asteroid in asteroids:
            for shot in updatable:
                if isinstance(shot, Shot) and shot.collide_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    break

        for sprite in drawable:
            sprite.draw(screen)
        

        #always last
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
