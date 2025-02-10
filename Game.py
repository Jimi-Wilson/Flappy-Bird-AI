import pygame
from Base import Base


class Game:
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 800
    BG_IMG = pygame.image.load("assets/bg.png") # todo: need to scale bg image.

    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.base = Base(700)




    def draw_background(self):
        self.screen.blit(self.BG_IMG, (0, 0))


    def draw(self):
        self.draw_background()
        self.base.draw(self.screen)


    def run(self):


        while self.running:
            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.base.move_base()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()