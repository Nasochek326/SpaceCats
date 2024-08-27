import pygame
import sprits
import setting
pygame.init()

button1image = pygame.image.load('res/assets/PNG/Ui/buttonYellow.png')
button1 = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2, button1image, 'Play')
button2image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button2 = sprits.Button(setting.SHIRINA / 2 + 500, setting.VISOTA / 2 + 350, button2image, 'Exit')
button_Continue_image = pygame.image.load('res/assets/PNG/Ui/buttonGreen.png')
button_Continue = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2, button1image, 'Continue')
pausa_text_image = pygame.image.load('res/assets/PNG/Ui/buttonYellow.png')
pausa_text = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2 - 400, button1image, 'Pause')
button_exit_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_exitmenu = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2 + 350, button2image, 'Exit menu')
button_kampani_image = pygame.image.load('res/assets/PNG/Ui/buttonYellow.png')
button_kampani = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2, button1image, 'Campaign')
button_infinity_image = pygame.image.load('res/assets/PNG/Ui/buttonYellow.png')
button_infinity = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2 - 100, button_infinity_image, 'Infinity')
button_exitmenu_play_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_shop_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_shop = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2 + 350, button_exitmenu_play_image, 'Shop')
button_ok_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_ok = sprits.Button(setting.SHIRINA / 2 - 100, setting.VISOTA / 2 + 350, button_exitmenu_play_image, 'Ok')
button_settings_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_settings = sprits.Button(setting.SHIRINA / 2 + 500, setting.VISOTA / 4 - 140, button_settings_image, 'settings')
#=-=-=-=-=-=
button_lvl1_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_lvl1 = sprits.Button(setting.SHIRINA / 2 + 500, setting.VISOTA / 2 - 250, button_lvl1_image, 'lvl 1')
button_lvl2_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_lvl2 = sprits.Button(setting.SHIRINA / 2 + 150, setting.VISOTA / 2 - 300, button_lvl2_image, 'lvl 2')
button_lvl3_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_lvl3 = sprits.Button(setting.SHIRINA / 2, setting.VISOTA / 2, button_lvl3_image, 'lvl 3')
button_lvl4_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_lvl4 = sprits.Button(setting.SHIRINA / 2 + 150, setting.VISOTA / 2 - 300, button_lvl4_image, 'lvl 4')
button_lvl5_image = pygame.image.load('res/assets/PNG/Ui/buttonBlue.png')
button_lvl5 = sprits.Button(setting.SHIRINA / 2 - 550, setting.VISOTA / 2 + 150, button_lvl5_image, 'lvl 5')
#=-=-=-=-=-=
button_enemyBlack1_image = pygame.image.load('media/image/space cats/enemyBlack1.png')
button_enemyBlack1 = sprits.Button(setting.SHIRINA / 2 - 700, setting.VISOTA / 2 - 350, button_enemyBlack1_image, str(150))
button_enemyBlack2_image = pygame.image.load('media/image/space cats/enemyBlack2.jpg')
button_enemyBlack2 = sprits.Button(setting.SHIRINA / 2 - 700, setting.VISOTA / 2 - 200, button_enemyBlack2_image, str(250))












