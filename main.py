import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # containers defined
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # containers assigned to classes
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids,updatable, drawable)
    Player.containers=(updatable,drawable)

    # GAME OBJECTS 
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # GAME LOOP
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt= clock.tick(60)/1000
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)

        



        pygame.display.flip()



if __name__ == "__main__":
    main()
