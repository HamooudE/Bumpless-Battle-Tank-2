##############################################################################################
############ ██████╗ ██╗   ██╗███╗   ███╗██████╗ ██╗     ███████╗███████╗███████╗ ############
############ ██╔══██╗██║   ██║████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝██╔════╝ ############
############ ██████╔╝██║   ██║██╔████╔██║██████╔╝██║     █████╗  ███████╗███████╗ ############
############ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ╚════██║╚════██║ ############
############ ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗███████║███████║ ############
############ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚══════╝╚══════╝ ############
##############################################################################################

###########################################
############### BIBLIOTEQUE ###############
import pygame
import pandas as pd
from pygame.mixer import Sound
from classes.Game import Game
from classes.Player import Player
from classes.Projectile import Projectile
from classes.Obstacle import Obstacle
from classes.Menu import MenuCustom
from classes.TextDisplay import TextDisplay
from classes.Bdd import Bdd
from classes.Sound import MakeSound
from classes.Constante import *
import sys
############### BIBLIOTEQUE ###############
###########################################

###################################
############# Sound ###############
pygame.mixer.init()
rocket_sfx = MakeSound("assets/sounds/rocket.mp3", 0.03)
pick_sfx = MakeSound("assets/sounds/pick2.mp3", 1) #"assets/sounds/pick.mp3" a de la latence
pick2_sfx = MakeSound("assets/sounds/pick2.mp3", 1)
pick3_sfx = MakeSound("assets/sounds/pick3.mp3", 1)
############# Sound ###############
###################################


#####################################################
############### INITIALISATION DU JEU ###############
#GENERATION DE LA FENETRE
pygame.init()  # Initialisation de Pygame
pygame.display.set_caption("BUMPLESS - BATTLE TANK")
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH), pygame.FULLSCREEN)
clock = pygame.time.Clock()
game = Game(screen)
pygame.init()
bdd = Bdd()
running = True
############### INITIALISATION DU JEU ###############
#####################################################


#########################################################################################################
################################ CREATION IMAGE + BOUTON MENU/NAVIGATION ################################
### MENU ###
#IMAGE BACKGROUND PRINCIPALE
background_principale = MenuCustom(screen, "assets/img/background" + str(game.theme) + ".png", 0, 0, HEIGHT, WIDTH)
#BOUTON START
bouton_start = MenuCustom(game.screen, "assets/img/Bouton_start" + str(game.theme) + ".png", 820, 290, 300, 75)
#BOUTON SETTING
bouton_setting = MenuCustom(game.screen, "assets/img/Bouton_setting" + str(game.theme) + ".png", 820, 375, 300, 75)
#BOUTON LEADERBOARD
bouton_leaderboard = MenuCustom(game.screen, "assets/img/Bouton_leaderboard" + str(game.theme) + ".png", 820, 460, 300, 75)
#BOUTON EXIT
bouton_exit = MenuCustom(game.screen, "assets/img/Bouton_exit" + str(game.theme) + ".png", 820, 545, 300, 75)
### MODE SELECTORE ###
#IMAGE BACKGROUND MODE SELECTOR
background_mode_set = MenuCustom(screen, "assets/img/mode_set" + str(game.theme) + ".png", 0, 0, HEIGHT, WIDTH)
#IMAGE MODE1 DEMO
mode1_0 = MenuCustom(screen, "assets/img/mode1_0.png", 90, 250, 500, 275)
mode1_1 = MenuCustom(screen, "assets/img/mode1_1.png", 90, 250, 500, 275)
#IMAGE MODE2 DEMO
mode2_0 = MenuCustom(screen, "assets/img/mode2_0.png", 710, 250, 500, 275)
mode2_1 = MenuCustom(screen, "assets/img/mode2_1.png", 710, 250, 500, 275)
#IMAGE MODE3 DEMO
mode3_0 = MenuCustom(screen, "assets/img/mode3_0.png", 1330, 250, 500, 275)
mode3_1 = MenuCustom(screen, "assets/img/mode3_1.png", 1330, 250, 500, 275)
#IMAGE MODE4 DEMO
mode4_0 = MenuCustom(screen, "assets/img/mode4_0.png", 90, 600, 500, 275)
mode4_1 = MenuCustom(screen, "assets/img/mode4_1.png", 90, 600, 500, 275)
#IMAGE MODE5 DEMO
mode5_0 = MenuCustom(screen, "assets/img/mode5_0.png", 710, 600, 500, 275)
mode5_1 = MenuCustom(screen, "assets/img/mode5_1.png", 710, 600, 500, 275)
#IMAGE MODE6 DEMO
mode6_0 = MenuCustom(screen, "assets/img/mode6_0.png", 1330, 600, 500, 275)
mode6_1 = MenuCustom(screen, "assets/img/mode6_1.png", 1330, 600, 500, 275)
### SETTING ###
#IMAGE BACKGROUND SETTING
background_setting = MenuCustom(screen, "assets/img/settings" + str(game.theme) + ".png", 0, 0, HEIGHT, WIDTH)
#PREVIEW TEXTURE PLAYER_1
p1_tex_prev = MenuCustom(game.screen, "assets/img/player1_step" + str(game.p1_skin) + ".png" , 1490, 280)
#PREVIEW TEXTURE PLAYER_2
p2_tex_prev = MenuCustom(game.screen, "assets/img/player2_step" + str(game.p1_skin) + ".png" , 1490, 435)
#PREVIEW TEXTURE Theme
theme_tex_prev = MenuCustom(game.screen, "assets/img/background" + str(game.theme) + ".png" , 1475, 600, 128, 72)
#BOUTON FLECHE CHOIX DU SKIN PLAYER_1
bouton_d1_texture = MenuCustom(game.screen, "assets/img/Fleche_droite" + str(game.theme) + ".png", 1615, 280, 178, 100)
bouton_g1_texture = MenuCustom(game.screen, "assets/img/Fleche_gauche" + str(game.theme) + ".png", 1285, 280, 178, 100)
#BOUTON FLECHE CHOIX DU SKIN PLAYER_2   
bouton_d2_texture = MenuCustom(game.screen, "assets/img/Fleche_droite" + str(game.theme) + ".png", 1615, 435, 178, 100)
bouton_g2_texture = MenuCustom(game.screen, "assets/img/Fleche_gauche" + str(game.theme) + ".png", 1285, 435, 178, 100)
#BOUTON FLECHE CHOIX DU Theme
bouton_d_theme = MenuCustom(game.screen, "assets/img/Fleche_droite" + str(game.theme) + ".png", 1615, 590, 178, 100)
bouton_g_theme = MenuCustom(game.screen, "assets/img/Fleche_gauche" + str(game.theme) + ".png", 1285, 590, 178, 100)
#BOUTON Edit PLAYER_1
bouton_edit_p1 = MenuCustom(game.screen, "assets/img/Bouton_edit0.png", 150, 310)
#BOUTON set PLAYER_1
bouton_edit_p2 = MenuCustom(game.screen, "assets/img/Bouton_edit0.png", 150, 460)
#BOUTON Edit PLAYER_1
bouton_set_p1 = MenuCustom(game.screen, "assets/img/Bouton_set0.png", 300, 310)
#BOUTON set PLAYER_1
bouton_set_p2 = MenuCustom(game.screen, "assets/img/Bouton_set0.png", 300, 460)
### LEADERBOARD ###
#IMAGE BACKGROUND LEADERBOARD
background_leaderboard = MenuCustom(screen, "assets/img/leaderboard" + str(game.theme) + ".png", 0, 0, HEIGHT, WIDTH)
#IMAGE PREVIEW TOP1
top1_skin = MenuCustom(screen, "assets/img/player1_step1.png", 315, 460)
#IMAGE PREVIEW TOP2
top2_skin = MenuCustom(screen, "assets/img/player1_step2.png", 135, 550)
#IMAGE PREVIEW TOP3
top3_skin = MenuCustom(screen, "assets/img/player1_step3.png", 505, 640)
### AUTRE ###
#BACKGROUND OPTION PAUSE
background_pause = MenuCustom(game.screen, "assets/img/pause0.png", 0, 0)
#BOUTON RETOUR AU MENU
bouton_go_menu = MenuCustom(game.screen, "assets/img/Bouton_goback" + str(game.theme) + ".png", 80, 960, 200, 50)
################################ CREATION IMAGE + BOUTON MENU/NAVIGATION ################################
#########################################################################################################


##############################################################################################
################################ CREATION TEXT + ATH + OPTION ################################
### FONT ###
font0 = pygame.font.SysFont("Arial" , 20 , bold = True)
font1 = pygame.font.Font("assets/Fonts/font1.ttf" , 20)
font2 = pygame.font.Font("assets/Fonts/font2.ttf" , 20)
### COLOR ###
color = [pygame.Color(80, 180, 180), pygame.Color(100, 200, 153), pygame.Color(200, 200, 10), pygame.Color(1, 158, 153)]
### TEXT DISPLAY ###
#SETTING OPTION
#NICKNAME EDITOR
input_name_p1 = pygame.Rect(500, 310, 140, 34)
game.p1_name = "player1"
input_name_p2 = pygame.Rect(500, 460, 140, 34)
game.p2_name = "player2"
font = pygame.font.Font("assets/Fonts/font1.ttf", 50)
edit_p1name = False
edit_p2name = False
#SETTING SKIN SELECTOR
p1_skin_display = TextDisplay(game.screen, "Skin " + str(int(game.p1_skin)), "assets/Fonts/font2.ttf", color[game.theme], 10, 1090, 340)
p2_skin_display = TextDisplay(game.screen, "Skin " + str(int(game.p2_skin)), "assets/Fonts/font2.ttf", color[game.theme], 16, 1090, 490)
title_p1_skin_display = TextDisplay(game.screen, game.p1_name, "assets/Fonts/font2.ttf", color[game.theme], 43, 1040, 310)
title_p2_skin_display = TextDisplay(game.screen, game.p2_name, "assets/Fonts/font2.ttf", color[game.theme], 43, 1040, 460)
theme_display = TextDisplay(game.screen, "Theme  " + str(game.theme), "assets/Fonts/font2.ttf", color[game.theme], 43, 1040, 610)
bounce_set = TextDisplay(game.screen, "Bounce set to: " + str(game.bounce_l[game.bounce_i]), "assets/Fonts/font2.ttf", color[game.theme], 43, 130, 610)
choc_set = TextDisplay(game.screen, "Bounce set to : " + str(game.choc_l[game.choc_i]), "assets/Fonts/font2.ttf", color[game.theme], 43, 130, 760)
#TITLE
title_display = TextDisplay(game.screen, "Bumpless", "assets/Fonts/font1.ttf", color[game.theme], 72, 750, 60)
#MENU
mode_title = TextDisplay(game.screen, "Mode Set", "assets/Fonts/font2.ttf", color[game.theme], 92, 75, 65)
setting_title = TextDisplay(game.screen, "Setting", "assets/Fonts/font2.ttf", color[game.theme], 92, 100, 65)
leaderboard_title = TextDisplay(game.screen, "Leaderboard", "assets/Fonts/font2.ttf", color[game.theme], 64, 65, 80)
#IN GAME ATH
fps_display = TextDisplay(game.screen, "FPS : " + str(int(clock.get_fps())), "assets/Fonts/font1.ttf", color[game.theme], 18, 940, 5)
p1_xyz_display = TextDisplay(game.screen, "#" + game.p1_name + ": X: " + str(int(game.player1.pos[0])) + "  Y: " + str(int(game.player1.pos[1])), "assets/Fonts/font2.ttf", color[game.theme], 18, 10, 5)
p2_xyz_display = TextDisplay(game.screen, "#" + game.p2_name + ": X: " + str(int(game.player2.pos[0])) + "  Y: " + str(int(game.player2.pos[1])), "assets/Fonts/font2.ttf", color[game.theme], 18, 1595, 5)
#SCORE LEADERBOARD
Stat_display = TextDisplay(game.screen, "NickName", "assets/Fonts/font2.ttf", pygame.Color(1, 200, 153), 35, 740, 175)
ratio_victoire_display = TextDisplay(game.screen, "Win\Lose", "assets/Fonts/font2.ttf", pygame.Color(1, 200, 153), 35, 1020, 175)
ratio_degat_display = TextDisplay(game.screen, "Damage\Hit", "assets/Fonts/font2.ttf", pygame.Color(1, 200, 153), 35, 1250, 175)
win_display = TextDisplay(game.screen, "WIN", "assets/Fonts/font2.ttf", pygame.Color(1, 200, 153), 35, 1540, 175)
score_display = TextDisplay(game.screen, "Score", "assets/Fonts/font2.ttf", pygame.Color(1, 200, 153), 35, 1690, 175)

Stat1_display = TextDisplay(game.screen, str(bdd.leader_score()[0][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 235)
pod1_display = TextDisplay(game.screen, str(bdd.leader_score()[0][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 265, 380)
ratio_victoire1_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[0][1])/(int(bdd.leader_score()[0][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 235)
ratio_degat1_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[0][3])/(int(bdd.leader_score()[0][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 235)
win1_display = TextDisplay(game.screen, str(bdd.leader_score()[0][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 235)
score1_display = TextDisplay(game.screen, str(bdd.leader_score()[0][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 235)

Stat2_display = TextDisplay(game.screen, str(bdd.leader_score()[1][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 295)
pod2_display = TextDisplay(game.screen, str(bdd.leader_score()[1][0]), "assets/Fonts/font2.ttf", color[game.theme], 30, 70, 480)
ratio_victoire2_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[1][1])/(int(bdd.leader_score()[1][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 295)
ratio_degat2_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[1][3])/(int(bdd.leader_score()[1][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 295)
win2_display = TextDisplay(game.screen, str(bdd.leader_score()[1][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 295)
score2_display = TextDisplay(game.screen, str(bdd.leader_score()[1][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 295)

Stat3_display = TextDisplay(game.screen, str(bdd.leader_score()[2][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 355)
pod3_display = TextDisplay(game.screen, str(bdd.leader_score()[2][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 480, 560)
ratio_victoire3_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[2][1])/(int(bdd.leader_score()[2][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 355)
ratio_degat3_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[2][3])/(int(bdd.leader_score()[0][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 355)
win3_display = TextDisplay(game.screen, str(bdd.leader_score()[2][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 355)
score3_display = TextDisplay(game.screen, str(bdd.leader_score()[2][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 355)

Stat4_display = TextDisplay(game.screen, str(bdd.leader_score()[3][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 415)
ratio_victoire4_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[3][1])/(int(bdd.leader_score()[3][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 415)
ratio_degat4_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[3][3])/(int(bdd.leader_score()[3][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 415)
win4_display = TextDisplay(game.screen, str(bdd.leader_score()[3][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 415)
score4_display = TextDisplay(game.screen, str(bdd.leader_score()[3][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 415)

Stat5_display = TextDisplay(game.screen, str(bdd.leader_score()[4][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 475)
ratio_victoire5_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[4][1])/(int(bdd.leader_score()[4][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 475)
ratio_degat5_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[4][3])/(int(bdd.leader_score()[4][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 475)
win5_display = TextDisplay(game.screen, str(bdd.leader_score()[4][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 475)
score5_display = TextDisplay(game.screen, str(bdd.leader_score()[4][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 475)

Stat6_display = TextDisplay(game.screen, str(bdd.leader_score()[5][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 535)
ratio_victoire6_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[5][1])/(int(bdd.leader_score()[5][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 535)
ratio_degat6_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[5][3])/(int(bdd.leader_score()[5][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 535)
win6_display = TextDisplay(game.screen, str(bdd.leader_score()[5][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 535)
score6_display = TextDisplay(game.screen, str(bdd.leader_score()[5][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 535)

Stat7_display = TextDisplay(game.screen, str(bdd.leader_score()[6][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 595)
ratio_victoire7_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[6][1])/(int(bdd.leader_score()[6][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 595)
ratio_degat7_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[6][3])/(int(bdd.leader_score()[6][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 595)
win7_display = TextDisplay(game.screen, str(bdd.leader_score()[6][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 595)
score7_display = TextDisplay(game.screen, str(bdd.leader_score()[6][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 595)

Stat8_display = TextDisplay(game.screen, str(bdd.leader_score()[7][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 655)
ratio_victoire8_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[7][1])/(int(bdd.leader_score()[7][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 655)
ratio_degat8_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[7][3])/(int(bdd.leader_score()[7][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 655)
win8_display = TextDisplay(game.screen, str(bdd.leader_score()[7][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 655)
score8_display = TextDisplay(game.screen, str(bdd.leader_score()[7][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 655)

Stat9_display = TextDisplay(game.screen, str(bdd.leader_score()[8][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 715)
ratio_victoire9_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[8][1])/(int(bdd.leader_score()[8][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 715)
ratio_degat9_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[8][3])/(int(bdd.leader_score()[8][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 715)
win9_display = TextDisplay(game.screen, str(bdd.leader_score()[8][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 715)
score9_display = TextDisplay(game.screen, str(bdd.leader_score()[8][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 715)

Stat10_display = TextDisplay(game.screen, str(bdd.leader_score()[9][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 775)
ratio_victoire10_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[9][1])/(int(bdd.leader_score()[9][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 775)
ratio_degat10_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[9][3])/(int(bdd.leader_score()[9][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 775)
win10_display = TextDisplay(game.screen, str(bdd.leader_score()[9][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 775)
score10_display = TextDisplay(game.screen, str(bdd.leader_score()[9][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 775)

Stat11_display = TextDisplay(game.screen, str(bdd.leader_score()[10][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 835)
ratio_victoire11_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[10][1])/(int(bdd.leader_score()[10][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 835)
ratio_degat11_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[10][3])/(int(bdd.leader_score()[10][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 835)
win11_display = TextDisplay(game.screen, str(bdd.leader_score()[10][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 835)
score11_display = TextDisplay(game.screen, str(bdd.leader_score()[10][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 835)

Stat12_display = TextDisplay(game.screen, str(bdd.leader_score()[11][0]), "assets/Fonts/font2.ttf", color[game.theme], 35, 750, 895)
ratio_victoire12_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[11][1])/(int(bdd.leader_score()[11][2])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1100, 895)
ratio_degat12_display = TextDisplay(game.screen, str(int(int(bdd.leader_score()[11][3])/(int(bdd.leader_score()[11][4])+1))), "assets/Fonts/font2.ttf", color[game.theme], 35, 1300, 895)
win12_display = TextDisplay(game.screen, str(bdd.leader_score()[11][1]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1550, 895)
score12_display = TextDisplay(game.screen, str(bdd.leader_score()[11][5]), "assets/Fonts/font2.ttf", color[game.theme], 35, 1700, 895)
################################ CREATION TEXT + ATH + OPTION ################################
##############################################################################################


########################################################################################################
################################ UPDATE - RUNNING - FPS Q OPTIMISATION  ################################
while running :
    ###################################
    ############### FPS ###############
    clock.tick(FPS) # -1 : NO FPS CAP 
    #print("FPS :" ,clock.get_fps())
    pygame.display.update() #UPDATE
    ############### FPS ###############
    ###################################

    if game.bump1 == True:
        game.player1.bounce()
        game.player1.bounce_force -= PERTE_VITESSE_BOUNCE

        if game.player1.bounce_force <= 0: 
            game.bump1 = False

    if game.bump2 == True:
        game.player2.bounce()
        game.player2.bounce_force -= PERTE_VITESSE_BOUNCE

        if game.player2.bounce_force <= 0:
            game.bump2 = False

    if game.choc1 == True:
            game.player1.bounce(game.angle2)
            game.player1.bounce_force -= PERTE_VITESSE_CHOC
            if game.player1.bounce_force <= 0 :
                game.choc1 = False

    if game.choc2 == True:
        game.player2.bounce(game.angle1)
        game.player2.bounce_force -= PERTE_VITESSE_CHOC
        if game.player2.bounce_force <= 0 :
            game.choc2 = False

    if game.choc_ball == True:
        game.ball.bounce(game.angle_ball)
        game.ball.bounce_force -= PERTE_VITESSE_CHOC
        if game.ball.bounce_force <= 0 :
            game.choc_ball = False
    ##############################################################################################
    ################################ CONTROLE KEYBOARD & MOUSE ###################################
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            game.is_playing = False
            pygame.quit()
    ### CONTROLE KEYBOARD ###
        if event.type == pygame.KEYDOWN:
            #détécter si la touche espace (player1) est enclenchée pour attaquer tank2
            if event.key == SHOOT1 :
                rocket_sfx.play()
                if game.player1.launch_projectile():
                    game.player1.bounce_force = VITESSE_INITIAL_BOUNCE
                    game.bump1 = True
                    
            #détécter si la touche espace (player2) est enclenchée pour attaquer tank2
            if event.key == SHOOT2:
                rocket_sfx.play()
                if game.player2.launch_projectile():
                    game.player2.bounce_force = VITESSE_INITIAL_BOUNCE
                    game.bump2 = True
            if game.is_playing:
                #IN GAME PAUSE
                if event.key == pygame.K_ESCAPE:
                    if game.in_pause == True:
                        game.in_pause = False
                    else:
                        game.in_pause = True
            #PLAYER_1 NAME EDITOR INPUT
            elif game.in_setting and edit_p1name == True:
                game.player1.name = game.p1_name
                if event.key == pygame.K_BACKSPACE:
                    game.p1_name = game.p1_name[:-1]
                    pick3_sfx.play()
                elif len(game.p1_name) < 7:#MAX 7 CARACTERES
                    game.p1_name += event.unicode
                    pick3_sfx.play()
            #PLAYER_1 NAME EDITOR INPUT
            elif game.in_setting and edit_p2name == True:
                game.player2.name = game.p2_name
                if event.key == pygame.K_BACKSPACE:
                    game.p2_name = game.p2_name[:-1]
                    pick3_sfx.play()
                elif len(game.p2_name) < 7:#MAX 7 CARACTERES
                    game.p2_name += event.unicode
                    pick3_sfx.play()
        ### CONTROLE MOUSE ###
        if event.type == pygame.MOUSEBUTTONDOWN :
        ## BOUTON ##
            #BOUTON START
            if game.in_menu and bouton_start.get_rect().collidepoint(event.pos) :
                pick_sfx.play()
                game.in_mode_set = True
                game.in_menu = False
                bdd.new_pseudo(game.p1_name)
                bdd.new_pseudo(game.p2_name)
            #BOUTON SETTING
            elif game.in_menu and bouton_setting.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_menu = False
                game.in_setting =True
            #BOUTON LEADERBOARD
            elif game.in_menu and bouton_leaderboard.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_leaderboard = True
            elif game.in_leaderboard and bouton_go_menu.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_leaderboard = False
                game.in_menu = True
            #BOUTON GO BACK TO MENU FROM SETTING
            elif game.in_setting and bouton_go_menu.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_setting = False
                game.in_menu = True
            #BOUTON GO BACK TO MENU FROM PAUSE
            elif game.in_pause and bouton_go_menu.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_pause = False
                game.is_playing = False
                game.reset(None)
                game.in_menu = True
            #BOUTON EXIT
            elif game.in_menu and bouton_exit.get_rect().collidepoint(event.pos) or game.in_pause and bouton_exit.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.is_playing = False
                pygame.quit()
                print("Fermeture du jeu")
        ## MODE SELECTORE ##
            #SELECTOR MODE 1#
            elif game.in_mode_set and mode1_0.get_rect().collidepoint(event.pos):
                game.in_mode_set = False
                game.is_playing = True
                game.mode = 1
            #SELECTOR MODE 2#
            elif game.in_mode_set and mode2_0.get_rect().collidepoint(event.pos):
                game.in_mode_set = False
                game.is_playing = True
                game.mode = 2
            elif game.in_mode_set and bouton_go_menu.get_rect().collidepoint(event.pos):
                pick_sfx.play()
                game.in_mode_set = False
                game.in_menu = True
                
        ## OPTION ##
            #FLECHE SELECTOR SKIN PLAYER_1
            elif game.in_setting and bouton_d1_texture.get_rect().collidepoint(event.pos):
                if game.p1_skin > NOMBRE_DE_SKIN -2:
                    game.p1_skin = 0
                else:
                    game.p1_skin += 1
                pick2_sfx.play()
                game.player1 = Player(game, "player1", "assets/img/player1_step"+str(game.p1_skin)+".png", 50, 515, 3, -90)
                p1_tex_prev.url = "assets/img/player1_step" + str(game.p1_skin) + ".png"
                p1_skin_display.content = "Skin " + str(int(game.p1_skin))
                p1_tex_prev.image_update()
            elif game.in_setting and bouton_g1_texture.get_rect().collidepoint(event.pos):
                if game.p1_skin < 1 :
                    game.p1_skin = NOMBRE_DE_SKIN -1 
                else:
                    game.p1_skin -= 1
                pick2_sfx.play()
                game.player1 = Player(game, "player1", "assets/img/player1_step"+str(game.p1_skin)+".png", 50, 515, 3, -90)
                p1_tex_prev.url = "assets/img/player1_step" + str(game.p1_skin) + ".png"
                p1_skin_display.content = "Skin " + str(int(game.p1_skin))
                p1_tex_prev.image_update()
            #FLECHE SELECTOR SKIN PLAYER_2
            elif game.in_setting and bouton_d2_texture.get_rect().collidepoint(event.pos):
                if game.p2_skin > NOMBRE_DE_SKIN - 2 : #+nb skin en plus
                    game.p2_skin = 0
                else:
                    game.p2_skin += 1
                pick2_sfx.play()
                game.player2 = Player(game, "player2", "assets/img/player2_step"+str(game.p2_skin)+".png", 1795, 515, 3, 90)
                p2_tex_prev.url = "assets/img/player2_step" + str(game.p2_skin) + ".png"
                p2_skin_display.content = "Skin " + str(int(game.p2_skin))
                p2_tex_prev.image_update()

            elif game.in_setting and bouton_g2_texture.get_rect().collidepoint(event.pos):
                if game.p2_skin < 1 :
                    game.p2_skin = NOMBRE_DE_SKIN - 1 #+nb skin en plus
                else:
                    game.p2_skin -= 1
                pick2_sfx.play()
                game.player2 = Player(game, "player2", "assets/img/player2_step"+str(game.p2_skin)+".png", 1795, 515, 3, 90)
                p2_tex_prev.url = "assets/img/player2_step" + str(game.p2_skin) + ".png"
                p2_skin_display.content = "Skin " + str(int(game.p2_skin))
                p2_tex_prev.image_update()

            #FLECHE SELECTOR Theme
            elif game.in_setting and bouton_d_theme.get_rect().collidepoint(event.pos):
                if game.theme > NOMBRE_DE_THEME -2 :
                    game.theme = 0
                else:
                    game.theme += 1
                pick2_sfx.play()
                theme_tex_prev.url = "assets/img/background" + str(game.theme) + ".png"
                background_principale.url = "assets/img/background" + str(game.theme) + ".png"
                background_setting.url = "assets/img/settings" + str(game.theme) + ".png"
                background_leaderboard.url = "assets/img/leaderboard" + str(game.theme) + ".png"
                #background_pause.url = "assets/img/pause" + str(game.theme) + ".png"
                theme_display.content = "Theme  " + str(game.theme)
                bouton_d1_texture.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g1_texture.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_d2_texture.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g2_texture.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_d_theme.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g_theme.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_start.url = "assets/img/Bouton_start" + str(game.theme) + ".png"
                bouton_setting.url = "assets/img/Bouton_setting" + str(game.theme) + ".png"
                bouton_leaderboard.url = "assets/img/Bouton_leaderboard" + str(game.theme) + ".png"
                bouton_go_menu.url = "assets/img/Bouton_goback" + str(game.theme) + ".png"
                bouton_exit.url = "assets/img/Bouton_exit" + str(game.theme) + ".png"
                title_p1_skin_display.color = color[game.theme]
                title_p2_skin_display.color = color[game.theme]
                theme_display.color = color[game.theme]
                title_display.color = color[game.theme]
                fps_display.color = color[game.theme]
                p1_xyz_display.color = color[game.theme]
                p2_xyz_display.color = color[game.theme]
                title_display.text_update()
                title_p1_skin_display.text_update()
                title_p2_skin_display.text_update()
                theme_display.text_update()
                fps_display.text_update()
                p1_xyz_display.text_update()
                p2_xyz_display.text_update()
                bouton_start.image_update()
                bouton_setting.image_update()
                bouton_leaderboard.image_update()
                bouton_go_menu.image_update()
                bouton_exit.image_update()
                theme_display.afficher_text()
                theme_tex_prev.image_update()
                background_principale.image_update()
                background_setting.image_update()
                background_leaderboard.image_update()
                #background_pause.image_update()
                bouton_d1_texture.image_update()
                bouton_g1_texture.image_update()
                bouton_d2_texture.image_update()
                bouton_g2_texture.image_update()
                bouton_d_theme.image_update()
                bouton_g_theme.image_update()

            elif game.in_setting and bouton_g_theme.get_rect().collidepoint(event.pos):
                if game.theme < 1 :
                    game.theme = NOMBRE_DE_THEME - 1
                else:
                    game.theme -= 1
                pick2_sfx.play()
                theme_tex_prev.url = "assets/img/background" + str(game.theme) + ".png"
                background_principale.url = "assets/img/background" + str(game.theme) + ".png"
                background_setting.url = "assets/img/settings" + str(game.theme) + ".png"
                background_leaderboard.url = "assets/img/leaderboard" + str(game.theme) + ".png"
                #background_pause.url = "assets/img/pause" + str(game.theme) + ".png"
                theme_display.content = "Theme  " + str(game.theme)
                bouton_d1_texture.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g1_texture.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_d2_texture.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g2_texture.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_d_theme.url = "assets/img/Fleche_droite" + str(game.theme) + ".png"
                bouton_g_theme.url = "assets/img/Fleche_gauche" + str(game.theme) + ".png"
                bouton_start.url = "assets/img/Bouton_start" + str(game.theme) + ".png"
                bouton_setting.url = "assets/img/Bouton_setting" + str(game.theme) + ".png"
                bouton_leaderboard.url = "assets/img/Bouton_leaderboard" + str(game.theme) + ".png"
                bouton_go_menu.url = "assets/img/Bouton_goback" + str(game.theme) + ".png"
                bouton_exit.url = "assets/img/Bouton_exit" + str(game.theme) + ".png"
                title_p1_skin_display.color = color[game.theme]
                title_p2_skin_display.color = color[game.theme]
                theme_display.color = color[game.theme]
                title_display.color = color[game.theme]
                title_display.text_update
                fps_display.color = color[game.theme]
                p1_xyz_display.color = color[game.theme]
                p2_xyz_display.color = color[game.theme]
                title_p1_skin_display.text_update()
                title_p2_skin_display.text_update()
                theme_display.text_update()
                fps_display.text_update()
                p1_xyz_display.text_update()
                p2_xyz_display.text_update()
                bouton_start.image_update()
                bouton_setting.image_update()
                bouton_leaderboard.image_update()
                bouton_go_menu.image_update()
                bouton_exit.image_update()
                theme_display.afficher_text()
                theme_tex_prev.image_update()
                background_principale.image_update()
                background_setting.image_update()
                background_leaderboard.image_update()
                #background_pause.image_update()
                bouton_d1_texture.image_update()
                bouton_g1_texture.image_update()
                bouton_d2_texture.image_update()
                bouton_g2_texture.image_update()
                bouton_d_theme.image_update()
                bouton_g_theme.image_update()
            elif game.in_setting and bouton_edit_p1.get_rect().collidepoint(event.pos):
                edit_p1name = True
                edit_p2name = False
                game.p1_name = ""
                pick3_sfx.play()
            elif game.in_setting and bouton_set_p1.get_rect().collidepoint(event.pos):
                edit_p1name = False
                pick3_sfx.play()
            elif game.in_setting and bouton_edit_p2.get_rect().collidepoint(event.pos):
                edit_p1name = False
                edit_p2name = True
                game.p2_name = ""
                pick3_sfx.play()
            elif game.in_setting and bouton_set_p2.get_rect().collidepoint(event.pos):
                edit_p2name = False
                pick3_sfx.play()
    ################################ CONTROLE KEYBOARD & MOUSE ###################################
    ##############################################################################################


    ##############################################################################################
    ################################ MENU DISPLAY INFORMATION ####################################
    ### DISPLAY WITHOUT UPDATE ###
    background_principale.afficher_image()
    title_display.afficher_text()
    
    ### DISPLAY WITH UPDATE ###
    fps_display.content = "FPS : " + str(int(clock.get_fps()))
    p1_xyz_display.content = "#" + game.p1_name + ": X: " + str(int(game.player1.pos[0])) + "  Y: " + str(int(game.player1.pos[1]))
    p2_xyz_display.content = "#" + game.p2_name + ": X: " + str(int(game.player2.pos[0])) + "  Y: " + str(int(game.player2.pos[1]))
    fps_display.text_update()
    p1_xyz_display.text_update()
    p2_xyz_display.text_update()
    fps_display.afficher_text()
    p1_xyz_display.afficher_text()
    p2_xyz_display.afficher_text()
    ### DISPLAY WHEN PLAYING ###
    if game.is_playing :
        # déclencher les instructions de la partie
        game.in_menu = False
        game.update(screen)
    ### DISPLAY IN MENU ###
    elif game.in_menu:
        #afficher l'écran de bienvenue 
        bouton_start.afficher_image()
        bouton_setting.afficher_image()
        bouton_leaderboard.afficher_image()
        bouton_exit.afficher_image()
    ### DISPLAY IN MODE SELECTORE ###
    if game.in_mode_set:
        background_mode_set.afficher_image()
        mode_title.afficher_text()
        mode1_0.afficher_image()
        mode2_0.afficher_image()
        mode3_0.afficher_image()
        mode4_0.afficher_image()
        mode5_0.afficher_image()
        mode6_0.afficher_image()
        bouton_go_menu.afficher_image()
    ### DISPLAY IN SETTING ###
    if game.in_setting:
        background_setting.afficher_image()
        setting_title.afficher_text()
        fps_display.afficher_text()
        title_p1_skin_display.afficher_text()
        title_p2_skin_display.afficher_text()
        theme_display.afficher_text()
        p1_xyz_display.afficher_text()
        p2_xyz_display.afficher_text()
        p1_tex_prev.afficher_image()
        p2_tex_prev.afficher_image()
        bouton_d1_texture.afficher_image()
        bouton_g1_texture.afficher_image()
        bouton_d2_texture.afficher_image()
        bouton_g2_texture.afficher_image()
        bouton_d_theme.afficher_image()
        bouton_g_theme.afficher_image() 
        theme_tex_prev.afficher_image()
        bouton_set_p1.afficher_image()
        bouton_set_p2.afficher_image()
        bouton_edit_p1.afficher_image()
        bouton_edit_p2.afficher_image()
        bounce_set.afficher_text()
        choc_set.afficher_text()
          # ->Nothing #
        ### NAME EDITOR PLAYER_1 ###
        pygame.draw.rect(screen, pygame.Color(100, 158, 153), input_name_p1, 2)
        text_surfacep1 = font.render(game.p1_name, True, (255,255,255))
        screen.blit(text_surfacep1, (input_name_p1.x+5, input_name_p1.y+5))
        input_name_p1.w = max(100, text_surfacep1.get_width()+10)
        ### NAME EDITOR PLAYER_2 ###
        pygame.draw.rect(screen, pygame.Color(100, 158, 153), input_name_p2, 2)
        text_surfacep2 = font.render(game.p2_name, True, (255,255,255))
        screen.blit(text_surfacep2, (input_name_p2.x+5, input_name_p2.y+5))
        input_name_p2.w = max(100, text_surfacep2.get_width()+10)
        #BOUTON GO BACK TO MENU
        bouton_go_menu.afficher_image()
    ### DISPLAY IN LEADERBOARD ###
    if game.in_leaderboard:
        background_leaderboard.afficher_image()
        leaderboard_title.afficher_text()
        top1_skin.afficher_image()
        top2_skin.afficher_image()
        top3_skin.afficher_image()
        pod1_display.afficher_text()
        pod2_display.afficher_text()
        pod3_display.afficher_text()
        fps_display.afficher_text()
        p1_xyz_display.afficher_text()
        p2_xyz_display.afficher_text()
        bouton_go_menu.afficher_image()

        Stat_display.afficher_text()
        ratio_victoire_display.afficher_text()
        ratio_degat_display.afficher_text()
        win_display.afficher_text()
        score_display.afficher_text()

        Stat1_display.afficher_text()
        ratio_victoire1_display.afficher_text()
        ratio_degat1_display.afficher_text()
        win1_display.afficher_text()
        score1_display.afficher_text()

        Stat2_display.afficher_text()
        ratio_victoire2_display.afficher_text()
        ratio_degat2_display.afficher_text()
        win2_display.afficher_text()
        score2_display.afficher_text()

        Stat3_display.afficher_text()
        ratio_victoire3_display.afficher_text()
        ratio_degat3_display.afficher_text()
        win3_display.afficher_text()
        score3_display.afficher_text()

        Stat4_display.afficher_text()
        ratio_victoire4_display.afficher_text()
        ratio_degat4_display.afficher_text()
        win4_display.afficher_text()
        score4_display.afficher_text()

        Stat5_display.afficher_text()
        ratio_victoire5_display.afficher_text()
        ratio_degat5_display.afficher_text()
        win5_display.afficher_text()
        score5_display.afficher_text()

        Stat6_display.afficher_text()
        ratio_victoire6_display.afficher_text()
        ratio_degat6_display.afficher_text()
        win6_display.afficher_text()
        score6_display.afficher_text()

        Stat7_display.afficher_text()
        ratio_victoire7_display.afficher_text()
        ratio_degat7_display.afficher_text()
        win7_display.afficher_text()
        score7_display.afficher_text()

        Stat8_display.afficher_text()
        ratio_victoire8_display.afficher_text()
        ratio_degat8_display.afficher_text()
        win8_display.afficher_text()
        score8_display.afficher_text()

        Stat9_display.afficher_text()
        ratio_victoire9_display.afficher_text()
        ratio_degat9_display.afficher_text()
        win9_display.afficher_text()
        score9_display.afficher_text()

        Stat10_display.afficher_text()
        ratio_victoire10_display.afficher_text()
        ratio_degat10_display.afficher_text()
        win10_display.afficher_text()
        score10_display.afficher_text()

        Stat11_display.afficher_text()
        ratio_victoire11_display.afficher_text()
        ratio_degat11_display.afficher_text()
        win11_display.afficher_text()
        score11_display.afficher_text()
        
        Stat12_display.afficher_text()
        ratio_victoire12_display.afficher_text()
        ratio_degat12_display.afficher_text()
        win12_display.afficher_text()
        score12_display.afficher_text()

    ### DISPLAY PAUSE WHEN PLAYING ###
    if game.in_pause:
        background_pause.afficher_image()
        bouton_go_menu.afficher_image()
        bouton_exit.afficher_image()
    ################################ MENU DISPLAY INFORMATION ####################################
    ##############################################################################################
    

################################ UPDATE - RUNNING - FPS - OPTIMISATION  ################################
########################################################################################################