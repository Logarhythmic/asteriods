import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    
    #print(f'Screen width: {SCREEN_WIDTH}')
    #print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #print(f'Asteroid min radius: {ASTEROID_MIN_RADIUS}')
    #print(f'Asteroid kinds: {ASTEROID_KINDS}')
    #print(f'Asteroid spawn rate: {ASTEROID_SPAWN_RATE}')
    #print(f'Asteroid max radius: {ASTEROID_MAX_RADIUS}')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        #always last
        pygame.display.flip()


if __name__ == "__main__":
    main()
