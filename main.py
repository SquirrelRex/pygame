# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
import circleshape
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    tt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    plr = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        dt = clock.tick(60)/1000
        tt += dt
        plr.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Mission complete! You survived {tt:.2f} seconds")
                return
            
        screen.fill("black")
        plr.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
