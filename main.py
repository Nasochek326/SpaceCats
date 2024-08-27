
import setting
import sprits
import Buttons
import pygame.freetype
import save
pygame.init()


def stolknov_lasers():
    for w in lasers:
        for w2 in asteroids:
            if w.xitboks.colliderect(w2.xitboks):
                asteroids.remove(w2)
                lasers.remove(w)
                koradl.potast += 1


def stolknov_lasers_vs(l, lasers, xp2):
    for w in lasers:
        for w2 in l:
            if w.xitboks.colliderect(w2.xitboks):
                xp2 -= 1
                koradl.xp = xp2




def stolknov():
    for w in asteroids:
        if koradl.xitboks.colliderect(w.xitboks):
            asteroids.remove(w)
            koradl.xp = koradl.xp - 1
            povreg.play()
        elif koradl.xp == 0:
            ynich.play()


def stolknov_lasers_korvs():
    for w in lasers:
        if w.xitboks.colliderect(koradlvs.xitboks):
            lasers.remove(w)
            koradlvs.xp = koradlvs.xp - 1
            povreg.play()


def stolknov_xp():
    for w in xps:
        if koradl.xitboks.colliderect(w.xitboks):
            koradl.xp = koradl.xp + 1
            xps.remove(w)


def stolknov_money():
    for w in moneys:
        if koradl.xitboks.colliderect(w.xitboks):
            save.money = save.money + 1
            moneys.remove(w)


kolmeteor = 0
lasers = []
lasers_vs = []
asteroids = []
xps = []
moneys = []
korabl_list = []
ob = pygame.freetype.Font('media/texts/space cats/Softie Cyr.ttf', 45)
proverka = 0
proverka_lvl = 0
ynich = pygame.mixer.Sound('media/sounds/space cats/Звук уничтожения коробля.mp3')
povreg = pygame.mixer.Sound('media/sounds/space cats/Звук повреждения.mp3')
buttonzvuk = pygame.mixer.Sound('media/sounds/space cats/Звук нажатие.mp3')
health_image = pygame.image.load('media/image/space cats/сердце.png')
health_image = pygame.transform.scale(health_image, [60, 60])
fon_mus = pygame.mixer.Sound('media/sounds/space cats/фон.музыка.wav')
las_mus = pygame.mixer.Sound('media/sounds/space cats/звук лазера.wav')
okno = pygame.display.set_mode([setting.SHIRINA, setting.VISOTA])
pausa = pygame.image.load('media/image/space cats/Menu.jpg')
fonmenu = pygame.image.load('media/image/space cats/Menu.jpg')
fonmenu = pygame.transform.scale(fonmenu, [setting.SHIRINA, setting.VISOTA])
static = pygame.image.load('media/image/space cats/Статистика.jpg')
static = pygame.transform.scale(static, [setting.SHIRINA, setting.VISOTA])
kampani = pygame.image.load('media/image/space cats/Кампания.jpg')
kampani = pygame.transform.scale(kampani, [setting.SHIRINA, setting.VISOTA])
kampani2 = pygame.image.load('media/image/space cats/Кампания.jpg')
kampani2 = pygame.transform.scale(kampani2, [setting.SHIRINA, setting.VISOTA])
fon = pygame.image.load('media/image/space cats/фон.png')
fon = pygame.transform.scale(fon, [setting.SHIRINA, setting.VISOTA])
koradl = sprits.Korabl()
koradlvs = sprits.Korabl_Boss()
koradlvs2 = sprits.Korabl_Boss()
spaw_money = pygame.USEREVENT
pygame.time.set_timer(spaw_money, 1500)
spaw_xp = pygame.USEREVENT + 1
pygame.time.set_timer(spaw_xp, 10000)
spaw_nasteroids = pygame.USEREVENT + 2
pygame.time.set_timer(spaw_nasteroids, 1000)
las_mus.set_volume(0.05)
fon_mus.set_volume(0.05)
povreg.set_volume(0.05)
ynich.set_volume(0.05)
fon_mus.play(-1)
stop = True
while stop is True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            stop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Hello')
            elif event.key == pygame.K_ESCAPE:
                proverka = 2
        if event.type == spaw_nasteroids and proverka == 1:
            fon_mus.set_volume(0.02)
            asteroid = sprits.Astroids()
            asteroids.append(asteroid)
            stolknov()
        if event.type == spaw_xp and koradl.xp == 1 and proverka == 1:
            xp = sprits.Xp()
            xps.append(xp)
        if event.type == spaw_money and proverka == 1:
            money = sprits.Money()
            moneys.append(money)
            if proverka_lvl == 5 and koradlvs.xp > 0:
                laser_vs = sprits.Lasers_vs(koradlvs.xitboks.centerx, koradlvs.xitboks.centery)
                lasers_vs.append(laser_vs)
                las_mus.play()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if proverka == 1:
                laser = sprits.Lasers(koradl.xitboks.centerx, koradl.xitboks.centery)
                lasers.append(laser)
                las_mus.play()
            elif proverka == 0:
                if Buttons.button1.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 4
                elif Buttons.button2.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    stop = False
                elif Buttons.button_settings.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 9
                elif Buttons.button_shop.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 6
                    okno.blit(kampani, [0, 0])
            elif proverka == 2:
                if Buttons.button_Continue.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 1
                if Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
                    proverka_lvl = 0
            elif proverka == 3:
                if Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
            elif proverka == 4:
                if Buttons.button_infinity.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 1
                    koradl.xp = 5
                    asteroids.clear()
                    lasers.clear()
                    if proverka_lvl == 5:
                        lasers_vs.clear()
                elif Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
                elif Buttons.button_kampani.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 5
            elif proverka == 5:
                if Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
                if save.proverka_lvls > 0:
                    if Buttons.button_lvl1.xitboks.collidepoint(event.pos) == True:
                        proverka = 7
                        proverka_lvl = 1
                        asteroids.clear()
                        lasers.clear()
                if save.proverka_lvls > 1:
                    if Buttons.button_lvl2.xitboks.collidepoint(event.pos) == True:
                        proverka = 7
                        proverka_lvl = 2
                        asteroids.clear()
                        lasers.clear()
                if save.proverka_lvls > 2:
                    if Buttons.button_lvl3.xitboks.collidepoint(event.pos) == True:
                        proverka = 7
                        proverka_lvl = 3
                        asteroids.clear()
                        lasers.clear()
                if save.proverka_lvls > 4:
                    if Buttons.button_lvl5.xitboks.collidepoint(event.pos) == True:
                        proverka = 7
                        proverka_lvl = 5
                        asteroids.clear()
                        lasers.clear()
                        # koradlvs.risovka(okno)
            elif proverka == 6:
                if Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
                elif Buttons.button_enemyBlack1.xitboks.collidepoint(event.pos) == True:
                    if save.money > save.button_enemyBlack1:
                        buttonzvuk.play()
                        save.money -= save.button_enemyBlack1
                        koradl.image = pygame.image.load('media/image/space cats/enemyBlack1.png')
                        save.button_enemyBlack1 = 0
                elif Buttons.button_enemyBlack2.xitboks.collidepoint(event.pos) == True:
                    if save.money > save.button_enemyBlack2:
                        buttonzvuk.play()
                        save.money -= save.button_enemyBlack1
                        koradl.image = pygame.image.load('media/image/space cats/enemyBlack2.jpg')
                        save.button_enemyBlack1 = 0
            elif proverka == 7:
                if Buttons.button_ok.xitboks.collidepoint(event.pos) == True:
                    proverka = 1
            elif proverka == 8:
                if Buttons.button_ok.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
            elif proverka == 9:
                if Buttons.button_exitmenu.xitboks.collidepoint(event.pos) == True:
                    buttonzvuk.play()
                    proverka = 0
            # elif proverka_lvl == 1:
            #     print('w')
            #     for w in asteroids:
            #         if w.xitboks.x == setting.SHIRINA:
            #             kolmeteor += 1
            #             print(kolmeteor)
            #         if kolmeteor > 9:
            #             proverka = 3



    if proverka == 1:
        if proverka_lvl == 1:
            for w in asteroids:
                if w.xitboks.x == setting.SHIRINA:
                    kolmeteor += 1
                if kolmeteor > 9:
                    kolmeteor = 0
                    proverka = 8
        elif proverka_lvl == 2:
            for w in asteroids:
                if w.xitboks.x == setting.SHIRINA:
                    kolmeteor += 1
                if kolmeteor > 29:
                    kolmeteor = 0
                    proverka = 8
        elif proverka_lvl == 3:
            for w in asteroids:
                if w.xitboks.x == setting.SHIRINA:
                    kolmeteor += 1
                if kolmeteor > 100:
                    kolmeteor = 0
                    proverka = 8
        # elif proverka_lvl == 5:
        #     if koradlvs.xp > 0:
        #         # koradl.uprawlenie()
        #         koradlvs.risovka(okno)
        #         koradlvs.uprawlenie()
        #         korabl_list.append(koradl)
        #     elif koradlvs.xp < 0:
        #         ynich.play()
            # koradlvs2.uprawlenie()

        koradl.uprawlenie()
        # koradlvs.uprawlenie()
        for w in asteroids:
            w.dwigenie()
        for w in lasers:
            w.dwigenie()
        if proverka_lvl == 5 and koradlvs.xp > 0:
            for w in lasers_vs:
                w.dwigenie()
        for w in xps:
            w.dwigenie()
        for w in moneys:
            w.dwigenie()
        xp2 = koradl.xp

        stolknov()
        stolknov_lasers_vs(korabl_list, lasers_vs, xp2)
        stolknov_lasers()
        stolknov_lasers_korvs()
        stolknov_xp()
        stolknov_money()

        okno.blit(fon, [0, 0])
        koradl.risovka(okno)
        if proverka_lvl == 5 and koradlvs.xp > 0:
            koradlvs.risovka(okno)
            koradlvs.uprawlenie()
            korabl_list.append(koradl)
        x = 200
        y = 100
        for w in range(0, xp2):
            okno.blit(health_image, [x, y])
            x = x + 60

        for w in asteroids:
            w.risovka(okno)
        for w in lasers:
            w.risovka(okno)
        if proverka_lvl == 5 and koradlvs.xp > 0:
            for w in lasers_vs:
                w.risovka(okno)
        for w in xps:
            w.risovka(okno)
        for w in moneys:
            w.risovka(okno)
        if koradl.xp == 0:
            proverka = 3

    elif proverka == 0:
        okno.blit(fonmenu, [0, 0])
        Buttons.button1.risovka(okno)
        Buttons.button2.risovka(okno)
        Buttons.button_shop.risovka(okno)
        Buttons.button_settings.risovka(okno)
        ob.render_to(okno, [setting.SHIRINA / 8, setting.VISOTA / 8], 'Money' + ' : ' + str(save.money), [250, 250, 250])
    elif proverka == 2:
        okno.blit(pausa, [0, 0])
        Buttons.button_Continue.risovka(okno)
        Buttons.button_exitmenu.risovka(okno)
        Buttons.pausa_text.risovka(okno)
    elif proverka == 3:
        okno.blit(static, [0, 0])
        Buttons.button_exitmenu.risovka(okno)
        ob.render_to(okno, [200, 250], 'Asteroids' + ' ' + str(koradl.potast))
        ob.render_to(okno, [200, 300], 'Money' + ' ' + str(save.money))
    elif proverka == 4:
        okno.blit(kampani, [0, 0])
        Buttons.button_kampani.risovka(okno)
        Buttons.button_exitmenu.risovka(okno)
        Buttons.button_infinity.risovka(okno)
    elif proverka == 5:
        okno.blit(kampani2, [0, 0])
        Buttons.button_lvl1.risovka(okno)
        Buttons.button_lvl2.risovka(okno)
        Buttons.button_lvl3.risovka(okno)
        Buttons.button_lvl5.risovka(okno)
        Buttons.button_exitmenu.risovka(okno)
    elif proverka == 6:
        Buttons.button_exitmenu.risovka(okno)
        Buttons.button_enemyBlack1.risovka(okno)
        Buttons.button_enemyBlack2.risovka(okno)
    elif proverka == 7 and proverka_lvl == 1:
        okno.blit(kampani2, [0, 0])
        ob.render_to(okno, [setting.SHIRINA / 2 - 450, setting.VISOTA / 2], 'Your task is to dodge the 10 coming at you.', [250, 250, 250])
        Buttons.button_ok.risovka(okno)
    elif proverka == 7 and proverka_lvl == 2:
        okno.blit(kampani2, [0, 0])
        ob.render_to(okno, [setting.SHIRINA / 2 - 450, setting.VISOTA / 2], 'Your task is to dodge the 30 coming at you.', [250, 250, 250])
        Buttons.button_ok.risovka(okno)
    elif proverka == 7 and proverka_lvl == 3:
        okno.blit(kampani2, [0, 0])
        ob.render_to(okno, [setting.SHIRINA / 2 - 450, setting.VISOTA / 2], 'Your task is to dodge the 100 coming at you.', [250, 250, 250])
        Buttons.button_ok.risovka(okno)
    elif proverka == 8:
        okno.blit(kampani2, [0, 0])
        ob.render_to(okno, [setting.SHIRINA / 2 - 100, setting.VISOTA / 2], 'You winer!', [250, 250, 250])
        Buttons.button_ok.risovka(okno)
        save.proverka_lvls += 1
    elif proverka == 9:
        okno.blit(kampani2, [0, 0])
        Buttons.button_exitmenu.risovka(okno)
    pygame.display.update()
