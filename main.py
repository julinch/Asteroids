import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        for updatable_obj in updatable:
            updatable_obj.update(dt)
        
        for asteroid in asteroids :
            if asteroid.is_colliding(player):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if (shot.is_colliding(asteroid)):
                    shot.kill()
                    asteroid.split()
        
        screen.fill((0,0,0))

        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
