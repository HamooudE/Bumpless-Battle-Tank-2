#############################################
#                                           #
#                Projectile                 #
#                                           #
#############################################

###########################################
############### BIBLIOTEQUE ##############
import pygame
import math
from classes.Bdd import Bdd
from classes.Sound import MakeSound
from classes.Constante import *
############### BIBLIOTEQUE ##############
###########################################

###################################
############# Sound ###############
pygame.mixer.init()
hit_sfx = MakeSound("assets/sounds/hit.mp3", 1)
############# Sound ###############
###################################

#class qui gère chaque projetile des joueurs
class Projectile(pygame.sprite.Sprite):                                                             #JoueurP = Joueur Propriétaire du Projectile
    def __init__(self, player, game):
        super().__init__()
        self.player = player                                                                        #Propriétaire du projectile
        self.image = pygame.image.load('assets/img/missile.png')                                    #Image du projectile
        self.image = pygame.transform.scale(self.image,(TAILLE_PROJECTILE,TAILLE_PROJECTILE))       #Change la taille du projectile
        self.rect = self.image.get_rect()                                                           #Transforme le projectile en un rectangle
        self.angle = player.angle                                                                   #Angle de tir par rapport au JoueurP
        self.pos = pygame.Vector2(player.pos)                                                       #Position du projectile
        self.rect.center = round(self.pos.x), round(self.pos.y)                                     #Centre du projectile
        self.direction = pygame.Vector2(0, -30).rotate(-self.angle+90)                              #Direction du projectile
        self.origin_image = self.image.copy()                                                       #Image d'origine du projectile
        self.game = game                                                                            #Importation de la classe Game
        self.bdd = Bdd()                                                                            #Importation de la Base de données
        self.vecteur = pygame.Vector2(0, 0)
        self.angle_to_rad = math.radians(self.angle + 90)
        self.rad_to_vec = [math.cos(self.angle_to_rad), -math.sin(self.angle_to_rad)]
        self.angle_save = [math.cos(self.angle_to_rad), -math.sin(self.angle_to_rad)]
    

    def angle_to_vec2(self):
        vecteur2_rota = math.radians(self.angle + 90)

        # Calcul des composantes x et y du vecteur
        x = math.cos(vecteur2_rota)
        y = math.sin(vecteur2_rota)
        self.rad_to_vec = [x, -y]

    def set_vecteur(self):
        self.pos += self.vecteur
        self.rect.center = round(self.pos[0]), round(self.pos[1])
        self.vecteur = pygame.Vector2(0,0)

    def update(self):
        """
        Cette fonction permet de faire bouger le projectile
        """
        self.set_vecteur()                                          
        self.angle_to_vec2()                                          
        self.image = pygame.transform.rotate(self.origin_image, self.angle+90)  #Rotation de l'image du tank
        self.rect = self.image.get_rect(center=self.rect.center)                #Actualise le rectangle du tank
        self.vecteur = ((self.rad_to_vec[0]*30), (self.rad_to_vec[1]*30))

    def remove(self):
        """
        Cette fonction permet de retirer le projectile de la fenêtre
        """
        self.player.all_projectiles.remove(self)                                #Enlève le projectile parmi tous les projectiles

    def collision_damage(self,player, other_player):
        """
        Cette fonction permet de changer la durabilité des tanks et d'actualiser les dégâts dans la bdd
        Aussi elle permet de supprimer le projectile s'il sort de la fenêtre"""

        if self.rect.colliderect(other_player.rect) :                           #Vérifier si le projectile entre en collision avec un joueur
            self.remove()                                                       #Retirer le projectile de la fenêtre
            other_player.damage(self.player.power)                              #Endommage le tank touché
            self.bdd.edit_score(other_player.name,'degats_subis',player.power)  #Augmente les dégâts subis du tank touché
            self.bdd.edit_score(player.name,'degats_infliges',player.power)     #Augmente les dégâts infligés du tank du Joueur
            hit_sfx.play()
            return True
        ##############################
        #Si le projectile sort de la fenêtre -> remove
        if self.rect.x > HEIGHT - 20 or self.rect.x < 20 or self.rect.colliderect(self.game.obstacle.rect): #Vérifier si projectile est sorti de la fenetre
            self.remove()

        if self.rect.y > WIDTH - 20 or self.rect.y < 20 or self.rect.colliderect(self.game.obstacle.rect): #Vérifier si projectile est sorti de la fenetre
            self.remove()
