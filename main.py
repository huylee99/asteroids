import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  # this loc is adding player to groups
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updatable, drawable)

  dt = 0
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for obj in updatable: 
      obj.update(dt)

    for asteroid in asteroids:
      if asteroid.is_collide(player):
        print("Game over")
        exit()

      for bullet in shots:
        if asteroid.is_collide(bullet):
          asteroid.split()
          bullet.kill()

    pygame.Surface.fill(screen, "black")

    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()
    
    tick = clock.tick(60)
    dt = tick / 1000

if __name__ == "__main__":
  main()
