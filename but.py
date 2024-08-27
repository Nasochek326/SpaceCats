import pygame
import pygame.freetype
pygame.init()
class Button:
    def __init__(self, x, y, image, text):
        self.image = image
        self.x = x
        self.y = y
        self.text = text
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([x, y], rasmer)
        self.ob = pygame.freetype.Font('res/Softie Cyr.ttf', 45)
        self.render = self.ob.render(text)
        self.text_image = self.render[0]
        self.xitboks_text = self.render[1]
        self.xitboks_text.center = self.xitboks.center

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)
        okno.blit(self.text_image, self.xitboks_text)