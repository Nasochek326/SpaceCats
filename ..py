import pygame
okno = pygame.display.set_mode([1000, 800])
people1 = pygame.rect.Rect(50, 380, 10, 100)
people2 = pygame.rect.Rect(950, 380, 10, 100)
stop = True
while stop is True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            stop = False


okno.fill([250, 0, 0])
pygame.draw.rect(okno, [250, 250, 250], people1)
pygame.draw.rect(okno, [250, 250, 250], people2)
pygame.display.update()































