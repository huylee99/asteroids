import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    pygame.Surface.fill(screen, "black")
    player.draw(screen)
    tick = clock.tick(60)
    dt = tick / 1000
    player.update(dt)
    
    pygame.display.flip()
    
if __name__ == "__main__":
  main()
