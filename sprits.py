import pygame
import setting
import random
import pygame.freetype


class Korabl:
    def __init__(self):
        self.speed = 2.5
        self.image = None
        if self.image is None:
            self.image = pygame.image.load('media/image/space cats/Корабль пов.png')
        rasmer = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [rasmer[0] / 7, rasmer[1] / 7])
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([250, setting.VISOTA / 2], [rasmer[0], rasmer[1]])
        self.xp = 5
        self.potast = 0
        self.kol_las = 15

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)

    def uprawlenie(self):
        listklava = pygame.key.get_pressed()
        if listklava[pygame.K_w] is True:
            self.xitboks.y = self.xitboks.y - self.speed
        elif listklava[pygame.K_s] is True:
            self.xitboks.y = self.xitboks.y + self.speed
        if listklava[pygame.K_a] is True:
            self.speed = 5
        else:
            self.speed = 2.5


#=-=-=-=-=-=-=


s = []
for w in range(0, 15):
    image = pygame.image.load('media/image/space cats/Метеорит.png')
    rasmer = image.get_size()
    rando = random.randint(5, 10)
    image = pygame.transform.scale(image, [rasmer[0] / rando, rasmer[1] / rando])
    s.append(image)
class Astroids:
    def __init__(self):
        self.speedX = random.randint(-5, -1)
        self.speedY = random.randint(-1, 1)
        self.image = s[random.randint(0, len(s) - 1)]
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([setting.SHIRINA, random.randint(0, setting.VISOTA)], [rasmer[0], rasmer[1]])
        self.proverka = 0
    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)


    def dwigenie(self):
        self.xitboks.y = self.xitboks.y + self.speedY
        self.xitboks.x = self.xitboks.x + self.speedX

#=-=-=-=-=-=
class Lasers:
    image = pygame.image.load('media/image/space cats/лазер.png')
    image = pygame.transform.rotate(image, -90)
    rasmer = image.get_size()
    image = pygame.transform.scale(image, [rasmer[0] / 4, rasmer[1] / 4])
    rasmer = image.get_size()

    def __init__(self, x, y):
        self.xitboks = pygame.rect.Rect([x, y - 50], [Lasers.rasmer[0], Lasers.rasmer[1]])
        self.speed = 5
        self.ob = Korabl()
        self.proverka = 0
        # self.kol = 15

    def risovka(self, okno):
        if self.ob.kol_las != 0:
            okno.blit(Lasers.image, self.xitboks)
            # self.ob.kol_las -= 1

    def dwigenie(self):
        if self.ob.kol_las != 0:
            self.xitboks.x = self.xitboks.x + self.speed


#=-=-=-=-=-=-=
class Button:
    def __init__(self, x, y, image, text):
        self.image = image
        self.x = x
        self.y = y
        self.text = text
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([x, y], rasmer)
        self.ob = pygame.freetype.Font('media/texts/space cats/Softie Cyr.ttf', 40)
        self.render = self.ob.render(text)
        self.text_image = self.render[0]
        self.xitboks_text = self.render[1]
        self.xitboks_text.center = self.xitboks.center

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)
        okno.blit(self.text_image, self.xitboks_text)
#=-=-=-=-=-=-=-=


class Xp:
    def __init__(self):
        self.speedX = random.randint(-2, -1)
        self.speedY = random.randint(0, 0)
        self.image = pygame.image.load('media/image/space cats/сердце.png')
        rasmer = self.image.get_size()
        self.random = random.randint(2, 5)
        self.image = pygame.transform.scale(self.image, [rasmer[0] / self.random, rasmer[1] / self.random])
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([setting.SHIRINA, random.randint(0, setting.VISOTA)], [rasmer[0], rasmer[1]])
        self.kol = 5

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)

    def dwigenie(self):
        self.xitboks.y = self.xitboks.y + self.speedY
        self.xitboks.x = self.xitboks.x + self.speedX


class Money:
    def __init__(self):
        self.speedX = random.randint(-2, -1)
        self.speedY = random.randint(0, 0)
        self.image = pygame.image.load('media/image/space cats/10243319.png')
        rasmer = self.image.get_size()
        self.random = random.randint(30, 30)
        self.image = pygame.transform.scale(self.image, [rasmer[0] / self.random, rasmer[1] / self.random])
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([setting.SHIRINA, random.randint(0, setting.VISOTA)], [rasmer[0], rasmer[1]])
        self.proverka = 0

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)

    def dwigenie(self):
        self.xitboks.y = self.xitboks.y + self.speedY
        self.xitboks.x = self.xitboks.x + self.speedX


class Korabl_Boss:
    def __init__(self):
        self.speed = 0.5
        self.image = pygame.image.load('media/image/space cats/enemyBlack2.jpg')
        rasmer = self.image.get_size()
        self.image = pygame.transform.scale(self.image, [rasmer[0], rasmer[1]])
        rasmer = self.image.get_size()
        self.xitboks = pygame.rect.Rect([1300, setting.VISOTA / 2], [rasmer[0], rasmer[1]])
        self.xp = 5
        self.proverka = 0
        self.kol_las = 20

    def risovka(self, okno):
        okno.blit(self.image, self.xitboks)

    def uprawlenie(self):
        self.xitboks.y += self.speed
        if self.xitboks.y > setting.VISOTA:
            self.xitboks.y -= setting.VISOTA


class Lasers_vs:
    image = pygame.image.load('media/image/space cats/лазер.png')
    image = pygame.transform.rotate(image, 180)
    rasmer = image.get_size()
    image = pygame.transform.scale(image, [rasmer[0] / 4, rasmer[1] / 4])
    rasmer = image.get_size()

    def __init__(self, x, y):
        self.xitboks = pygame.rect.Rect([x, y - 50], [Lasers.rasmer[0], Lasers.rasmer[1]])
        self.speed = 5
        self.ob = Korabl_Boss()
        self.proverka = 0
        # self.kol = 15

    def risovka(self, okno):
        if self.ob.kol_las != 0:
            okno.blit(Lasers.image, self.xitboks)
            # self.ob.kol_las -= 1

    def dwigenie(self):
        if self.ob.kol_las != 0:
            self.xitboks.x = self.xitboks.x - self.speed

