#############################################
#                                           #
#                  PLAYER                   #
#                                           #
#############################################

###########################################
############### BIBLIOTEQUE ###############
import pygame
import time
from classes.Projectile import Projectile
from classes.Bdd import Bdd
from classes.Sound import MakeSound
import numpy as np
import math
from classes.Constante import *
############### BIBLIOTEQUE ###############
###########################################

###################################
############# Sound ###############
pygame.mixer.init()
pick2_sfx = MakeSound("assets/sounds/pick2.mp3", 1)
############# Sound ###############
###################################

#Variable global qui défini le délai entre chaque tir 

#Class qui gère le tank
class Player(pygame.sprite.Sprite):                                                 #JoueurP = Joueur Propriétaire du tank
    def __init__(self, game, name, image, x, y, speed, angle):          
        super().__init__()                                                          #Initialisation de la class Sprite
        self.game = game                                                            #Implémentation de la class Game
        self.bdd = Bdd()                                                            #Implémentation de la class Base de données
        self.speed = speed                                                          #Vitesse de déplacement du tank
        self.power = SHOOT_PLAYER                                                   #Puissance de tir du tank
        self.name = name                                                            #Nom du JoueurP
        self.durability = DURABILITY                                                #Durabilité du tank
        self.max_durability = MAX_DURABILITY                                        #Maximum de la durabilité
        self.image = pygame.image.load(image).convert_alpha()                       #Image du tank
        self.image = pygame.transform.scale(self.image, (TAILLE_TANK, TAILLE_TANK)) #Redimensionne la taille du tank 
        self.rect = self.image.get_rect()                                           #Récupération du "rectangle" du tank
        self.rect.x = x                                                             #Initialisation de la position x du tank
        self.rect.y = y                                                             #Initialisation de la position y du tank
        self.pos =  pygame.Vector2(self.rect.center)                                #Position du tank
        self.all_projectiles = pygame.sprite.Group()                                #Groupe de tous les projectile du tank encore sur la fenêtre
        self.angle = angle                                                          #Angle (par rapport au canon) du tank
        self.direction = pygame.Vector2(1, 0)                                       #Direction du tank
        self.origin_image = self.image                                              #Image d'origine du tank
        self.last_shot = None                                                       #Dernier tir du tank
        self.wins = self.bdd.score_name(self.name)['wins']                          #Nombre de victoire du JoueurP
        self.degats_infliges = self.bdd.score_name(self.name)['degats_infliges']    #Nombre de dégâts infligés par le tank du JoueurP
        self.degats_subis = self.bdd.score_name(self.name)['degats_subis']          #Nombre de dégâts subis par le tank du JoueurP
        self.vecteur = pygame.Vector2(0, 0)
        self.angle_to_rad = math.radians(self.angle + 90)
        self.rad_to_vec = [math.cos(self.angle_to_rad), -math.sin(self.angle_to_rad)]
        self.turn_x = 1
        self.turn_y = 1
        self.angle_save = [math.cos(self.angle_to_rad), -math.sin(self.angle_to_rad)]
        self.bounce_force = 0
    #Vector2(vec1.x * vec2.x, vec1.y * vec2.y)
    #[math.cos(math.cos(math.radians(self.angle + 90)),math.sin(math.radians(self.angle + 90)))]

    def angle_to_vec2(self):
        vecteur2_rota = math.radians(self.angle + 90)

        # Calcul des composantes x et y du vecteur
        x = math.cos(vecteur2_rota)
        y = math.sin(vecteur2_rota)
        self.rad_to_vec = [x, -y]
        
    def hit_bordure(self):
        pass

    def set_vecteur(self):
        self.pos += self.vecteur
        self.rect.center = round(self.pos[0]), round(self.pos[1])
        self.vecteur = pygame.Vector2(0,0)

    def bounce(self, angle = None):
        """
        detection des bordures pour reboncir si besoin + utilisation de exp pour fluiditée de mouvements
        """
        if angle == None:
            if self.bounce_force == VITESSE_INITIAL_BOUNCE:
                self.angle_save = self.rad_to_vec
                self.turn_x = 1
                self.turn_y = 1
            elif self.rect.x < 0  :
                self.turn_x *= -1
                pick2_sfx.play()
            elif self.rect.x > WIDTH - TAILLE_TANK-TAILLE_TANK / 8:
                self.turn_x *= -1
                pick2_sfx.play()
            elif self.rect.y < 0 : 
                self.turn_y *= -1
                pick2_sfx.play()
            elif self.rect.y > HEIGHT - TAILLE_TANK-TAILLE_TANK / 8:
                self.turn_y *= -1
                pick2_sfx.play()
            self.vecteur = pygame.Vector2(-self.angle_save[0]*np.exp(self.bounce_force)*self.turn_x, -self.angle_save[1]*np.exp(self.bounce_force)*self.turn_y)
        elif angle != None:
            if self.bounce_force == VITESSE_INITIAL_BOUNCE:
                self.angle_save = [math.cos(math.radians(angle + 90)), math.sin(math.radians(angle + 90))]
                self.turn_x = 1
                self.turn_y = 1
            elif self.rect.x < 0 :
                self.turn_x *= -1
                pick2_sfx.play()
            elif self.rect.x > WIDTH - TAILLE_TANK-TAILLE_TANK / 8:
                self.turn_x *= -1
                pick2_sfx.play()
            elif self.rect.y < 0 : 
                self.turn_y *= -1
                pick2_sfx.play()
            elif self.rect.y > HEIGHT - TAILLE_TANK-TAILLE_TANK / 8:
                self.turn_y *= -1
                pick2_sfx.play()
            self.vecteur = pygame.Vector2(-self.angle_save[0]*np.exp(self.bounce_force)*self.turn_x, self.angle_save[1]*np.exp(self.bounce_force)*self.turn_y)


    def set_skin(self, new_skin):
        """
        Cette fonction permet de changer le skin du tank
        """
        self.image = new_skin   #Changement de l'image du tank

    def get_durability(self):
        """"
        Cette fonction return la durabilité du tank"""
        return self.durability  #Retroune la durabilité du tank
    
    def set_durability(self,durability):
        """
        Cette fonction permet de modifier la durabilité du tank
        """
        self.durability = durability    #Change le durabilité du tank

    def update_durability_bar(self,surface):
        """
        Cette fonction permet d'actualiser la bar de durabilité du tank"""
        pygame.draw.rect(surface, (60,63,00), [self.rect.x -15, self.rect.y-40, self.max_durability, 7])    #Colorie en Gris une partie de la bar
        pygame.draw.rect(surface, (111,210,46), [self.rect.x -15, self.rect.y-40, self.durability, 7])      #Colorie en Vert une partie de la bar
        
    
    def update_image(self,step):
        """
        Cette fonction permet de changer l'image du tank"""
        self.image = pygame.image.load(step).convert()  #Change l'image du tank
        return self.image                               #Retourne l'image du tank
    
    def rotate(self,gauche,droite) :
        """
        Cette fonction permet au tank de tourner
        """
        pressed = pygame.key.get_pressed()                                  #Stocke les touche préssées
        if pressed[gauche]:                                                 #Si la touche 'gauche' (q ou flèche gauche) est préssée
            self.angle += SPEED_ROTATION                                    #Incrémentation de l'angle du tank
            self.angle = self.angle % 360
        if pressed[droite]:                                                 #Si la touche 'droite' (d ou flèche droite) est préssée
            self.angle -= SPEED_ROTATION                                    #Décrémentation de l'angle du tank
            self.angle = self.angle % 360
        self.image = pygame.transform.rotate(self.origin_image, self.angle) #Rotation de l'image du tank
        self.rect = self.image.get_rect(center=self.rect.center)            #Actualise le rectangle du tank
    
    def move(self, touche):
        """
        Cette fonction permet au tank de se déplacer
        """

        pressed = pygame.key.get_pressed()                                  #Stocke les touches préssées
        if pressed[touche]:                                                 #Si la touche qui permet au tank de se déplacer (z ou flèche du haut) est préssée
            self.vecteur = self.rad_to_vec[0]*self.speed, self.rad_to_vec[1]*self.speed
        
    def reculer(self):
        """
        Cette fonction permet de faire reculer le tank (pour les collisions par exemple)
        """
        direction = pygame.Vector2(0, self.speed+0.3).rotate(-self.angle)   #Actualise la direction du tank
        self.pos += direction                                               #Change la position du tank
        self.rect.center = round(self.pos[0]), round(self.pos[1])           #Change le rectangle du tank de position
    
    
    def damage(self, amount):
        """
        Cette fonction permet de faire subir des dégâts au tank
        """
        if self.durability - amount > amount :  #Si le tank peut subir 'amount' dégâts en ayant encore de la durabilité
            self.durability -= amount           #Décrémentation de la durabilité du tank
        else :                                  #Sinon (si le tank n'a pas assez de durabilité pour subir 'amount' dégâts)
            self.game.game_over(self.name)      #Fin du jeu avec JoueurP perdant
            self.game.reset(self.name)          #Réinitialisation du jeu

    def add_durability(self,amount):
        """
        Cette fonction permet d'augmenter la durabilité du tank
        """
        self.durability += amount   #Incrémentation de la durabilité du tank

    def launch_projectile(self):
        """
        Cette fonction permet au tank de tirer un projectile
        """
        #Prise en compte du délai 'SHOT_DELAY' (variable global)
        if self.last_shot is None :                                     #Si le tank n'a jamais tiré
            self.last_shot = time.time()                                #Stockage du temps actuel comme temps du dernier tir
            self.all_projectiles.add(Projectile(self,self.game))        #Ajout d'un projectile sur la fenêtre
            return True
        else :                                                          #Sinon (si le tank a déjà tiré)
            x = time.time()                                             #Stockage du temps actuel
            if x > self.last_shot + SHOT_DELAY :                        #Si le temps actuel est supérieur au temps du dernier tir + délai
                self.all_projectiles.add(Projectile(self,self.game))    #Ajout d'un projectile sur la fênetre
                self.last_shot = x                                      #Stockage du temps actuel comme temps du dernier tir
                return True