import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((336, 700))
clock = pygame.time.Clock()
running = True


floor = pygame.image.load('assets/base.png')
x1 = 0
x2 = 336
while running:
    screen.fill("black")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(floor, (x1, 600))
    screen.blit(floor, (x2, 600))

    if x1 == -336:
        x1 += 672

    if x2 == -336:
        x2 += 672

    x1 -= 1
    x2 -= 1

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
