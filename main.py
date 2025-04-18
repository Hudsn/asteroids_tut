import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width: {width}".format(width=SCREEN_WIDTH))
    print("Screen height: {height}".format(height=SCREEN_HEIGHT))
    pygame.init()

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for d in drawable:
            d.draw(screen)

        updatable.update(dt)

        for a in asteroids:
            if a.is_collision(player):
                print("Game Over!")
                sys.exit()
            
            for s in shots:
                if a.is_collision(s):
                    a.split()
                    s.kill()
            
        pygame.display.flip()
        dt = clock.tick(60) / 1_000

    


if __name__ == "__main__":
    main()

