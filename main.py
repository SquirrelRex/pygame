import pygame
import sys
from asteroidfield import AsteroidField
from player import Player
import circleshape
from constants import *
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updateable, shots)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    field = AsteroidField()
    dt = 0
    tt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        dt = clock.tick(60)/1000
        tt += dt
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Mission complete! You survived {tt:.2f} seconds")
                return            
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
