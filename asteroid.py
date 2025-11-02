import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Wrap around screen
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
        angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        asteroid1.velocity = 1.2 * self.velocity.rotate(angle)
        asteroid2.velocity = 1.2 * self.velocity.rotate(-angle)
        asteroid1.add(Asteroid.containers)
        asteroid2.add(Asteroid.containers)