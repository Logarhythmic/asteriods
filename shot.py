import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, -PLAYER_SHOOT_SPEED)

    def update(self, dt):
        self.position += self.velocity * dt
        if (self.position.y < 0) or (self.position.y > SCREEN_HEIGHT) or (self.position.x < 0) or (self.position.x > SCREEN_WIDTH):
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), self.position, self.radius)
