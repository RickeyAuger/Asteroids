import pygame
from constants import *
from player import *
from circleshape import *


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
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000
        
        updatable.update(dt)
        
        screen.fill((0, 0 ,0))
        
        for drawables in drawable:
            drawables.draw(screen)
        
        pygame.display.flip()
       


if __name__ =="__main__":
    main()