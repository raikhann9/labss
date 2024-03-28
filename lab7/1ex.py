import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((1280, 960))
done = False
bgd = pygame.image.load("images/clock/clock.png")
secnd = pygame.image.load("images/clock/lar.png")
minutes = pygame.image.load("images/clock/rar.png")
rect = bgd.get_rect(center=(640,480))

while not done:
    screen.blit(bgd, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    nsec_img = pygame.transform.rotate(secnd, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(minutes, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()

