import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        slew = random.uniform(20, 50)
        vol1 = self.velocity.rotate(slew)*1.2
        vol2 = self.velocity.rotate(-slew)*1.2
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        a1 =Asteroid(self.position.x, self.position.y, new_rad)
        a1.velocity = vol1
        a2 =Asteroid(self.position.x, self.position.y, new_rad)
        a2.velocity = vol2
        return a1, a2
