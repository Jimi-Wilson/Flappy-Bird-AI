import pygame


class Bird:
    BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load('assets/bird1.png')),
                 pygame.transform.scale2x(pygame.image.load('assets/bird1.png')),
                 pygame.transform.scale2x(pygame.image.load('assets/bird1.png'))]



    def __init__(self, y):
        self.y = y
        self.vel = -4

    def move(self):
        if self.vel > -4:
            self.vel -= 0.1

        self.y -= self.vel

    def up(self):
        self.vel = 4

    def draw(self, screen):
        screen.blit(self.BIRD_IMGS[0], (283, self.y))
