import pygame


class Base:
    BASE_IMG = pygame.transform.scale2x(pygame.image.load('assets/base.png'))
    WIDTH = BASE_IMG.get_width()
    VEL = 5

    def __init__(self, y):
        self.y = y

        self.x1 = 0
        self.x2 = self.WIDTH

    def move_base(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.WIDTH + self.x2

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.WIDTH + self.x1

    def draw(self, screen):
        screen.blit(self.BASE_IMG, (self.x1, self.y))
        screen.blit(self.BASE_IMG, (self.x2, self.y))

