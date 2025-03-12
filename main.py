import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
   
    print(f"Screen width: {SCREEN_WIDTH}")
    
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    running = True
    
    updatable = pygame.sprite.Group()
    
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_for_collisions(player) == True:
                print("game over")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_for_collisions(shot) == True:
                    asteroid.kill()
                    shot.kill()
        
        screen.fill((0, 0 ,0))
        
        for drawables in drawable:
            drawables.draw(screen)
        
        pygame.display.flip()
       


if __name__ =="__main__":
    main()