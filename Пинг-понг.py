import pygame
import random
import pygame.freetype
pygame.init()

ob = pygame.freetype.Font('res/Softie Cyr.ttf', 45)




proverka = 1
people1 = 0
people2 = 0
pong = pygame.mixer.Sound('res/pong.wav')
pong.set_volume(0.05)
randomcolor1 = random.randint(0, 250)
randomcolor2 = random.randint(0, 250)
randomcolor3 = random.randint(0, 250)
speedX = 1
speedY = 1
okno = pygame.display.set_mode([1000, 800])
ball = pygame.rect.Rect(500, 400, 50, 50)
raket1 = pygame.rect.Rect(50, 380, 10, 100)
raket2 = pygame.rect.Rect(950, 380, 10, 100)
stop = True
while stop is True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            stop = False
        elif proverka == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    proverka = 1
                    ball = pygame.rect.Rect(500, 400, 50, 50)
                    people1 = 0
                    people2 = 0

    if proverka == 1:
        listklava = pygame.key.get_pressed()
        if listklava[pygame.K_w] is True:
            raket1.y = raket1.y - 1
        elif listklava[pygame.K_s] is True:
            raket1.y = raket1.y + 1
    # =-=-=-=-=-=-=-=-=-=-=
        if speedX > 0:
            if speedY > 0 and raket2.y < ball.y:
                raket2.y = raket2.y + 1
            if speedY < 0 and raket2.y > ball.y:
                raket2.y = raket2.y - 1
        # =-=-=-=-=-=-=-=-=-=-=
        ball.x = ball.x + speedX
        ball.y = ball.y + speedY
        if ball.right > 1000:
            speedX = -1
            randomcolor1 = random.randint(0, 250)
            randomcolor2 = random.randint(0, 250)
            randomcolor3 = random.randint(0, 250)
            people1 = people1 + 1
            ball = pygame.rect.Rect(500, 400, 50, 50)
            raket2 = pygame.rect.Rect(950, 380, 10, 100)
            print(str(people1) + ':' + str(people2))
        elif ball.left < 0:
            speedX = 1
            randomcolor1 = random.randint(0, 250)
            randomcolor2 = random.randint(0, 250)
            randomcolor3 = random.randint(0, 250)
            people2 = people2 + 1
            ball = pygame.rect.Rect(500, 400, 50, 50)
            print(str(people1) + ':' + str(people2))
        if ball.bottom > 800:
            speedY = -1
            randomcolor1 = random.randint(0, 250)
            randomcolor2 = random.randint(0, 250)
            randomcolor3 = random.randint(0, 250)
            speedX = random.randint(1, 3)
            pong.play()
        elif ball.top < 0:
            speedY = 1
            randomcolor1 = random.randint(0, 250)
            randomcolor2 = random.randint(0, 250)
            randomcolor3 = random.randint(0, 250)
            speedX = random.randint(-3, -1)
            pong.play()

        if raket1.colliderect(ball):
            speedX = 1
        elif raket2.colliderect(ball):
            speedX = -1

        if people1 > 4:
            print('Выйграл people1')
            proverka = 0
        elif people2 > 4:
            print('Выйграл people2')
            proverka = 0


    okno.fill([100, 100, 100])
    pygame.draw.rect(okno, [250, 250, 250], raket1)
    pygame.draw.rect(okno, [250, 250, 250], raket2)
    pygame.draw.ellipse(okno, [randomcolor1, randomcolor2, randomcolor3], ball)
    if proverka == 0:
        ob.render_to(okno, [400, 400], 'Restart')
        if people2 > 4:
            ob.render_to(okno, [400, 300], 'People 2')
        elif people1 > 4:
            ob.render_to(okno, [400, 300], 'People 2')

    pygame.display.update()

