import pygame,sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((HEIGHT,WIDTH))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level = Level()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()