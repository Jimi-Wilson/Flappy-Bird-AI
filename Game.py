import pygame
from pygame.examples.grid import WINDOW_HEIGHT

from Base import Base
from Bird import Bird

class Game:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 800
    BG_IMG = pygame.transform.scale(pygame.image.load("assets/bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))

    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bird = Bird(WINDOW_HEIGHT/2)

        self.base = Base(700)




    def draw_background(self):
        self.screen.blit(self.BG_IMG, (0, 0))


    def draw(self):
        self.draw_background()
        self.base.draw(self.screen)
        self.bird.draw(self.screen)


    def run(self):


        while self.running:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.up()

            self.bird.move()
            self.base.move_base()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()