##############################################################
############  ██████╗  █████╗ ███╗   ███╗███████╗ ############
############ ██╔════╝ ██╔══██╗████╗ ████║██╔════╝ ############
############ ██║  ███╗███████║██╔████╔██║█████╗   ############
############ ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝   ############
############ ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗ ############
############  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ############
##############################################################


###########################################
############### BIBLIOTEQUE ###############
import pygame
from pygame.mixer import Sound
import time
import random
import math
from classes.Constante import *
from classes.Player import Player
from classes.Obstacle import Obstacle
from classes.BonusMalus import BonusMalus
import pandas as pd
from classes.Bdd import Bdd
from classes.Sound import MakeSound
############### BIBLIOTEQUE ###############
###########################################

###################################
############# Sound ###############
pygame.mixer.init()
############# Sound ###############
###################################


#Class qui gère le jeu
class Game():
    def __init__(self,screen):
        self.in_menu = True                                                                                     #Etat du menu
        self.in_mode_set = False                                                                                #Etat du selecteur de modes
        self.is_playing = False                                                                                 #Etat du jeu
        self.mode = 0
        self.in_setting = False                                                                                 #Etat des paramètres
        self.in_leaderboard = False                                                                             #Etat du leaderboard
        self.in_pause = False                                                                                   #Etat de la pause
        self.bonus = True                                                                                       #Bonus activés ou désactivés
        self.malus = True                                                                                       #Malus activés ou désactivés
        self.theme = 0                                                                                          #Theme du jeu
        self.p1_skin = 2                                                                                        #Skin du tank1
        self.p2_skin = 2                                                                                        #Skin du tank2
        self.p1_name = "player1"                                                                                #Name du tank1
        self.p2_name = "player2"                                                                                #Name du tank2

        #Génération des Tanks
        self.player1 = Player(self, self.p1_name, "assets/img/player1_step"+str(self.p1_skin)+".png", 50*SCALE_X, 515*SCALE_Y, SPEED, -90)      #Génération du tank1
        self.player2 = Player(self, self.p1_name, "assets/img/player2_step"+str(self.p2_skin)+".png", 1795*SCALE_X, 515*SCALE_Y, SPEED, 90)     #Génération du tank2
        self.pressed_keys = {}                                                                                  #dictionnaire de toutes les touches pressées
        self.screen = screen                                                                                    #"Stockage" de l'écran
        self.n = 0                                                                                              #Variable int
        self.bounce_scale = {"High":4, "Bounce": VITESSE_INITIAL_BOUNCE, "Choc": VITESSE_INITIAL_CHOC ,"Medium": 2.8, "Low": 1.8, "No": 0}
        self.bounce_l =  ["High", "Bounce", "Choc", "Medium", "Low", "No"]
        self.choc_l = ["High", "Bounce", "Choc", "Medium", "Low", "No"]
        self.bounce_i =  1
        self.choc_i = 2
        self.bounce_set = self.bounce_scale[self.bounce_l[self.bounce_i]]
        self.choc_set = self.bounce_scale[self.choc_l[self.choc_i]]
        self.bump1 = False
        self.choc1 = False
        self.bump2 = False
        self.choc2 = False
        self.angle1 = 0
        self.angle2 = 0

        self.ball = Player(self, self.p1_name, "assets/img/ball.png", 540, 960, SPEED, 1)
        self.choc_ball=False
        self.angle_ball = 56
        

        #importation images gagnantes
        self.player1_wins = pygame.image.load("assets/img/player1_wins.png").convert()                                 #Importation de l'image quand player1 gagne
        self.player1_wins = pygame.transform.scale(self.player1_wins, (WIDTH, HEIGHT))                             #Changement de taille de l'image quand player1 gagne
        self.player2_wins = pygame.image.load("assets/img/player2_wins.png").convert()                                 #Importation de l'image quand player2 gagne
        self.player2_wins = pygame.transform.scale(self.player2_wins, (WIDTH, HEIGHT))                             #Changement de taille de l'image quand player2 gagne

        self.obstacle = Obstacle('assets/img/obstacle0.png', (100, 100), 400, 400) #ICI !!                                #Implémentation d'un obstacle

        self.bonus_durability = BonusMalus('Durability','assets/img/cle.png',(50,50), random.randint(600,800)*SCALE_X, random.randint(300,500)*SCALE_Y,self)   #Implémentation d'un bonus de durabilité (durability)
        self.bonus_speed = BonusMalus('Speed','assets/img/wheel.png',(50,50), random.randint(600,800)*SCALE_X, random.randint(300,500)*SCALE_Y,self)           #Implémentation d'un bonus de vitesse (speed)
        self.malus_slow = BonusMalus('Slow', 'assets/img/clou.png', (30,30), random.randint(600,800)*SCALE_X, random.randint(300,500)*SCALE_Y, self)           #Implémentation d'un malus de vitesse (slow)
        self.malus_boom = BonusMalus('Boom','assets/img/dynamite.png',(50,50),random.randint(600,800)*SCALE_X, random.randint(300,500)*SCALE_Y, self)          #Implémentanion d'un malus de durabilité (boom)
        self.temp = None                                                                                        #Variable temporaire 1
        self.temp2 = None                                                                                       #Variable temporaire 2
        self.temp3 = None                                                                                       #Variable temporaire 3
        self.temp4 = None                                                                                       #Variable temporaire 4
        self.bdd = Bdd()                                                                                        #Implémentation de la class Base de données

    def game_over(self, looser): 
        """
        Cette fonction permet d'annoncer le vainqueur
        """
        if looser == 'player1':                         #Si le perdant est player1
            print('PLAYER 2 WINS')                      #Affiche 'PLAYER 2 WINS'
            self.screen.blit(self.player2_wins,(0,0))   #Affiche une image où est marqué que player2 a gagné
            pygame.display.update()                     #Actualise l'affichage
            pygame.time.wait(2500)                      #Attendre 2500


        if looser == 'player2':                         #Si le perdant est player2
            print('PLAYER 1 WINS')                      #Affiche 'PLAYER 1 WINS'
            self.screen.blit(self.player1_wins,(0,0))   #Affiche une image où est marqué que player1 a gagné
            pygame.display.update()                     #Actualise l'affichage
            pygame.time.wait(2500)                      #Attendre 2500

    def reset(self,looser) : 
        """
        Cette fonction permet le retour au menu principale et réinitialise les valeurs utilisées lors de la partieen 
        """

        if looser == self.player1.name :                        #Si player1 perdant
            self.bdd.edit_score(self.player2.name,'wins',1)     #Incrémente les victoires de player2 dans la bdd
            self.bdd.edit_score(self.player1.name,'defeats',1)  #Incrémente les défaites de player1 dans la bdd
            self.bdd.edit_score(self.player1.name,'score',0)    #Modifie le score de player1 dans la bdd
            self.bdd.edit_score(self.player2.name,'score',0)    #Modifie le score de player2 dans la bdd
        
        if looser == self.player2.name :                        #Si player1 perdant
            self.bdd.edit_score(self.player1.name,'wins',1)     #Incrémente les victoires de player1 dans la bdd
            self.bdd.edit_score(self.player2.name,'defeats',1)  #Incrémente les défaites de player2 dans la bdd
            self.bdd.edit_score(self.player1.name,'score',0)    #Modifie le score de player1 dans la bdd
            self.bdd.edit_score(self.player2.name,'score',0)    #Modifie le score de player2 dans la bdd

        self.pressed_keys = {}                                  #Réinitialisation des touches préssées
        self.player1.all_projectiles = pygame.sprite.Group()    #Réinitialisation des projectile lancé par JoueurP du tank1
        self.player2.all_projectiles = pygame.sprite.Group()    #Réinitialisation des projectile lancé par JoueurP du tank2
        self.player1.durability = self.player1.max_durability   #Réinitialisation de la durabilité du tank1
        self.player2.durability = self.player2.max_durability   #Réinitialisation de la durabilité du tank2

        self.player1 = Player(self, "player1", "assets/img/player1_step"+str(self.p1_skin)+".png", 50*SCALE_X, 515*SCALE_Y, SPEED, -90)  #Repositionnement du tank1
        self.player2 = Player(self, "player2", "assets/img/player2_step"+str(self.p2_skin)+".png", 1795*SCALE_X, 515*SCALE_Y, SPEED, 90) #Repositionnement du tank2

        self.in_menu = True                                     #Modifie l'état du menu en 'True'
        self.is_playing = False                                 #Modifie l'état du jeu en 'False'
        self.in_setting = False                                 #Modifie l'état des paramètres en 'False'
        self.in_pause = False                                   #Modifie l'état de la pause en 'False'

    def update(self,screen):
        """<
        Cette fonction permet d'actualiser le jeu
        """
        if self.mode == 2:
            self.ball.set_vecteur()
            self.ball.angle_to_vec2()
            screen.blit(self.ball.image, self.ball.rect)
            self.ball.durability = 100
        if self.mode != 2:
            self.ball.rect.x = 2000
            self.ball.rect.y = 2000

        self.player1.set_vecteur()
        self.player1.angle_to_vec2()
        self.player2.set_vecteur()
        self.player2.angle_to_vec2()
        self.player1.all_projectiles.update()                                           #Actualise les projectiles du tank1
        self.player2.all_projectiles.update()                                           #Actualise les projectiles du tank2

        screen.blit(self.player1.image, self.player1.rect)                              #Actualise l'image du tank1
        screen.blit(self.player2.image, self.player2.rect)                              #Actualise l'image du tank2

        screen.blit(self.obstacle.image,self.obstacle.rect)                             #Actualise l'image de l'obstacle

        self.player1.update_durability_bar(screen)                                      #Actualise la bar de durabilité du tank1
        self.player2.update_durability_bar(screen)                                      #Actualise la bar de durabilité du tank1

        self.player1.all_projectiles.draw(screen)                                       #Actualise l'image des projectiles du tank1
        self.player2.all_projectiles.draw(screen)                                       #Actualise l'image des projectiles du tank2

        screen.blit(self.bonus_durability.image, self.bonus_durability.rect)            #Actualise l'image du bonus de durabilité (durability)
        screen.blit(self.bonus_speed.image, self.bonus_speed.rect)                      #Actualise l'image du bonus de vitesse (speed)
        screen.blit(self.malus_slow.image, self.malus_slow.rect)                        #Actualise l'image du malus de vitesse (slow)
        screen.blit(self.malus_boom.image, self.malus_boom.rect)                        #Actualise l'image du malus de durabilité (boom)
        

        if self.bonus is True :                                                             #Si les bonus sont activés
            #Test collision bonus durability
            if pygame.sprite.collide_mask(self.player1,self.bonus_durability) is not None:  #Si tank1 est en collision avec le bonus de durabilité
                self.bonus_durability.durability(self.player1,20)                           #Appliquation du bonus de durabilité au tank1
                self.bonus_durability.rect.x = 5000                                         #Retire le bonus de durabilité de la vue (en le met looooin)                          
            if pygame.sprite.collide_mask(self.player2,self.bonus_durability) is not None : #Si tank2 est en collision avec le bonus de durabilité
                self.bonus_durability.durability(self.player2,20)                           #Appliquation du bonus de durabilité au tank2
                self.bonus_durability.rect.x = 5000                                         #Retire le bonus de durabilité de la vue (en le met looooin)

            #Test collision bonus speed
            if pygame.sprite.collide_mask(self.player1,self.bonus_speed) is not None :      #Si tank1 est en collision avec le bonus de vitesse
                self.bonus_speed.speed(self.player1)                                        #Appliquation du bonus de vitesse au tank1
                self.bonus_speed.rect.x = 5000                                              #Retire le bonus de durabilité de la vue (en le met looooin)
            if pygame.sprite.collide_mask(self.player2,self.bonus_speed) is not None :      #Si tank2 est en collision avec le bonus de vitesse
                self.bonus_speed.speed(self.player2)                                        #Appliquation du bonus de vitesse au tank2
                self.bonus_speed.rect.x = 5000                                              #Retire le bonus de durabilité de la vue (en le met looooin)

            #Délai entre chaque bonus durability
            if self.temp is None :                                                          #Si le bonus n'a pas encore été présent
                self.temp = time.time()                                                     #Stocke le temp actuel
                self.bonus_durability.rect.x = random.randint(100,1850)                     #Coordonnée x du bonus aléatoire
                self.bonus_durability.rect.y = random.randint(100,960)                      #Coordonnée y du bonus aléatoire
            else :                                                                          #Sinon (si le bonus a déjà été présent)
                a = time.time()                                                             #Stocke le temps actuel
                if a > self.temp + DELAY_BONUS :                                            #Si le temps actuel est supérieur au temps du dernier bonus + délai
                    self.bonus_durability.rect.x = random.randint(100,1850)                 #Coordonnée x du bonus aléatoire
                    self.bonus_durability.rect.y = random.randint(100,960)                  #Coordonnée y du bonus aléatoire
                    self.temp = a                                                           #Actualise le temps actuel du dernier bonus

            #Délai entre chaque bonus vitesse
            if self.temp2 is None :                                                         #Si le bonus n'a pas encore été présent
                self.temp2 = time.time()                                                    #Stocke le temp actuel
                self.bonus_speed.rect.x = random.randint(100,1850)                          #Coordonnée x du bonus aléatoire
                self.bonus_speed.rect.y = random.randint(100,960)                           #Coordonnée y du bonus aléatoire
            else :                                                                          #Sinon (si le bonus a déjà été présent)
                b = time.time()                                                             #Stocke le temps actuel
                if b > self.temp2 + DELAY_BONUS :                                           #Si le temps actuel est supérieur au temps du dernier bonus + délai
                    self.bonus_speed.rect.x = random.randint(100,1850)                      #Coordonnée x du bonus aléatoire
                    self.bonus_speed.rect.y = random.randint(100,960)                       #Coordonnée y du bonus aléatoire
                    self.temp2 = b                                                          #Actualise le temps actuel du dernier bonus

        if self.malus is True :
            #Test collision malus slow
            if pygame.sprite.collide_mask(self.player1,self.malus_slow) is not None:        #Si tank1 est en collision avec le malus slow
                self.malus_slow.slow(self.player1)                                          #Appliquation du malus slow au tank1
                self.malus_slow.rect.x = 5000                                               #Retire le malus slow de la vue (en le met looooin)                          
            if pygame.sprite.collide_mask(self.player2,self.malus_slow) is not None :       #Si tank2 est en collision avec le malus slow
                self.malus_slow.slow(self.player2)                                          #Appliquation du malus slow au tank2
                self.malus_slow.rect.x = 5000                                               #Retire le malus slow de la vue (en le met looooin)
            #Délai entre chaque malus slow
            if self.temp3 is None :                                                         #Si le malus slow n'a pas encore été présent
                self.temp3 = time.time()                                                    #Stocke le temp actuel
                self.malus_slow.rect.x = random.randint(100,1850)                           #Coordonnée x du malus slow aléatoire
                self.malus_slow.rect.y = random.randint(100,960)                            #Coordonnée y du malus slow aléatoire
            else :                                                                          #Sinon (si le malus slow a déjà été présent)
                c = time.time()                                                             #Stocke le temps actuel
                if c > self.temp3 + DELAY_BONUS :                                           #Si le temps actuel est supérieur au temps du dernier bonus + délai
                    self.malus_slow.rect.x = random.randint(100,1850)                       #Coordonnée x du malus slow aléatoire
                    self.malus_slow.rect.y = random.randint(100,960)                        #Coordonnée y du malus slow aléatoire
                    self.temp3 = c                                                          #Actualise le temps actuel du dernier malus slow

            #Test collision malus boom
            if pygame.sprite.collide_mask(self.player1,self.malus_boom) is not None:        #Si tank1 est en collision avec le malus slow
                self.malus_boom.boom(self.player1,self.player2.power)                       #Appliquation du malus slow au tank1
                self.malus_boom.rect.x = 5000                                               #Retire le malus slow de la vue (en le met looooin)                          
            if pygame.sprite.collide_mask(self.player2,self.malus_boom) is not None :       #Si tank2 est en collision avec le malus slow
                self.malus_boom.boom(self.player2,self.player1.power)                       #Appliquation du malus slow au tank2
                self.malus_boom.rect.x = 5000                                               #Retire le malus slow de la vue (en le met looooin)
            #Délai entre chaque malus boom
            if self.temp4 is None :                                                         #Si le malus slow n'a pas encore été présent
                self.temp4 = time.time()                                                    #Stocke le temp actuel
                self.malus_boom.rect.x = random.randint(100,1850)                           #Coordonnée x du malus slow aléatoire
                self.malus_boom.rect.y = random.randint(100,960)                            #Coordonnée y du malus slow aléatoire
            else :                                                                          #Sinon (si le malus slow a déjà été présent)
                d = time.time()                                                             #Stocke le temps actuel
                if d > self.temp4 + DELAY_BONUS :                                           #Si le temps actuel est supérieur au temps du dernier bonus + délai
                    self.malus_boom.rect.x = random.randint(100,1850)                       #Coordonnée x du malus slow aléatoire
                    self.malus_boom.rect.y = random.randint(100,960)                        #Coordonnée y du malus slow aléatoire
                    self.temp4 = d                                                          #Actualise le temps actuel du dernier malus slow
        self.angle2 = math.degrees(math.atan2(self.player1.pos[0] - self.obstacle.rect.x - (self.obstacle.size[0]/2), self.player1.pos[1] - self.obstacle.rect.y - (self.obstacle.size[1]/2)))   
        self.angle1 = math.degrees(math.atan2(self.player2.pos[0] - self.obstacle.rect.x - (self.obstacle.size[0]/2), self.player2.pos[1] - self.obstacle.rect.y - (self.obstacle.size[1]/2)))
        self.angle_ball = math.degrees(math.atan2(self.ball.pos[0] - self.obstacle.rect.x - (self.obstacle.size[0]/2), self.ball.pos[1] - self.obstacle.rect.y - (self.obstacle.size[1]/2)))             #calcule de l'angel entre player 2 et obstacle
        #Vérifier si les joueurs veulent aller à droite/gauche/haut/bas et qu'ils ne sortent pas de la fenetre

        #Pour la ball : bump
        if pygame.sprite.collide_mask(self.ball,self.obstacle) is None :                    #Si la balle pas en collision avec obstacle
            pass
        else :                                                                              #sinon (si la balle en collision avec obstacle)
            self.ball.bounce_force = VITESSE_INITIAL_CHOC
            self.choc_ball = True                                                           #la balle rebondi
        #################################################################
        #Pour pas que le tank2 reste bloqué sur un bord de la fenêtre
        if self.ball.pos[1] < TAILLE_TANK / 2: 
            self.ball.pos[1] = TAILLE_TANK / 2
        elif self.ball.pos[1] > HEIGHT - TAILLE_TANK / 2 :
            self.ball.pos[1] = HEIGHT - TAILLE_TANK / 2

        elif self.ball.pos[0] < TAILLE_TANK / 2 : 
            self.ball.pos[0] = TAILLE_TANK / 2
        elif self.ball.pos[0] > WIDTH - TAILLE_TANK / 2:
            self.ball.pos[0] = WIDTH - TAILLE_TANK / 2
        #################################################################




        #Pour le joueur 1 : zqd
        if pygame.sprite.collide_mask(self.player1,self.obstacle) is None :                 #Si tank1 pas en collision avec obstacle
            self.player1.rotate(LEFT1, RIGHT1)                                      #Le tank peut tourner
            self.player1.move(FORWARD1)                                                   #tank1 peut bouger
        else :                                                                              #sinon (si tank1 en collision avec obstacle)
            self.player1.bounce_force = VITESSE_INITIAL_BOUNCE
            self.choc1 = True                                                               #le tank1 rebondi
        #################################################################
        # Pour pas que le tank1 reste bloqué sur un bord de la fenêtre
        if self.player1.pos[1] < TAILLE_TANK / 2:
            self.player1.pos[1] = TAILLE_TANK / 2
        elif self.player1.pos[1] > HEIGHT - TAILLE_TANK / 2:
            self.player1.pos[1] = HEIGHT - TAILLE_TANK / 2

        if self.player1.pos[0] < TAILLE_TANK / 2:
            self.player1.pos[0] = TAILLE_TANK / 2
        elif self.player1.pos[0] > WIDTH - TAILLE_TANK / 2:
            self.player1.pos[0] = WIDTH - TAILLE_TANK / 2
        #################################################################
   

        #Pour le joueur 2 : flèches
        if pygame.sprite.collide_mask(self.player2,self.obstacle) is None :                 #Si tank2 pas en collision avec obstacle
            self.player2.rotate(LEFT2,RIGHT2)                               #Le tank2 peut tourner
            self.player2.move(FORWARD2)                                                  #le tank2 peut avance
        else :                                                                              #Sinon (si tank2 en collision avec obstacle)
            self.player2.bounce_force = VITESSE_INITIAL_BOUNCE
            self.choc2 = True                                                               #le tank2 rebondi

        #################################################################
        #Pour pas que le tank2 reste bloqué sur un bord de la fenêtre
        if self.player2.pos[1] < TAILLE_TANK / 2 : 
            self.player2.pos[1] = TAILLE_TANK / 2
        elif self.player2.pos[1] > HEIGHT - TAILLE_TANK / 2:
            self.player2.pos[1] = HEIGHT -TAILLE_TANK / 2

        elif self.player2.pos[0] < TAILLE_TANK / 2 : 
            self.player2.pos[0] = TAILLE_TANK / 2
        elif self.player2.pos[0] > WIDTH - TAILLE_TANK / 2:
            self.player2.pos[0] = WIDTH - TAILLE_TANK / 2
        #################################################################
       

        #mettre à jour les dégats fait par les projectiles
        for projectile in self.player1.all_projectiles :                                    #Pour chaque projectile parmi tous les projectiles du tank1 et la balle
            self.angle1 = math.degrees(math.atan2(self.player1.pos[0] - self.player2.pos[0]  ,self.player1.pos[1] - self.player2.pos[1]))
            self.angle_ball = math.degrees(math.atan2(self.player1.pos[0] - self.ball.pos[0]  ,self.player1.pos[1] - self.ball.pos[1]))
            if projectile.collision_damage(self.player1,self.player2):                      #Vérifier si en collison avec l'autre tank ou bordure de la fenêtre
                self.player2.bounce_force = VITESSE_INITIAL_CHOC
                self.choc2 = True                                                           #le tank2 rebondi
            elif projectile.collision_damage(self.player1,self.ball):
                self.ball.bounce_force = VITESSE_INITIAL_CHOC
                self.choc_ball = True                                                       #la balle rebondi
        for projectile in self.player2.all_projectiles :                                    #Pour chaque projectile parmi tous les projectiles du tank2 et la balle
            self.angle2 = math.degrees(math.atan2(self.player2.pos[0] - self.player1.pos[0]  ,self.player2.pos[1] - self.player1.pos[1]))
            self.angle_ball = math.degrees(math.atan2(self.player2.pos[0] - self.ball.pos[0]  ,self.player2.pos[1] - self.ball.pos[1]))
            if projectile.collision_damage(self.player2,self.player1):                      #Vérifier si en collision avec l'autre tank ou bordure de la fenêtre
                self.player1.bounce_force = VITESSE_INITIAL_CHOC
                self.choc1 = True                                                           #le tank1 rebondi
            elif projectile.collision_damage(self.player2,self.ball):
                self.ball.bounce_force = VITESSE_INITIAL_CHOC
                self.choc_ball = True                                                       #la balle rebondi



        
