####################################################################################################################
########## ██████╗  ██████╗ ███╗   ██╗██╗   ██╗███████╗      ███╗   ███╗ █████╗ ██╗     ██╗   ██╗███████╗ ##########
########## ██╔══██╗██╔═══██╗████╗  ██║██║   ██║██╔════╝      ████╗ ████║██╔══██╗██║     ██║   ██║██╔════╝ ##########
########## ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗█████╗██╔████╔██║███████║██║     ██║   ██║███████╗ ##########
########## ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║╚════╝██║╚██╔╝██║██╔══██║██║     ██║   ██║╚════██║ ##########
########## ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████║      ██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝███████║ ##########
########## ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝ ##########
####################################################################################################################              

###########################################
############### BIBLIOTEQUE ###############
import pygame
from classes.Constante import *
############### BIBLIOTEQUE ###############
###########################################


#######################################################################################################
########################### CLASS BONUSMALUS -> ITEM IN MATCH #########################################
class BonusMalus(pygame.sprite.Sprite): 
    def __init__(self,name:str,image,size:tuple,x,y,game):
        super().__init__()                                      #initialisation de la class Sprite
        self.name = name                                        #nom de l'obstacle
        self.size = size                                        #tuple : taille en pixel ex : 100px*100px
        self.x = x                                      
        self.y = y
        self.image = pygame.image.load(image)                   #Image de l'obstacle
        self.image = pygame.transform.scale(self.image, size)   #Redimensionne l'image
        self.game = game                                        #Implémentation de la class Game
        self.rect = self.image.get_rect()                       #Récupère le rectangle de l'image de l'obstacle
        self.rect.x = x                                         #initialisation x de la position de l'obstacle
        self.rect.y = y                                         #initialisation y de la position de l'obstacle
        self.pos = pygame.Vector2(self.rect.center)             #position de l'obstacle


    def durability(self,player, amount:int):
        """
        Cette fonction augmente la durabilité d'un tank"""
        if player.durability + amount <= player.max_durability : #la durabilité du tank ne peux pas dépasser son max
            player.durability += amount                          #incrémentation de la durabilité
        else :                                              
            player.durability = player.max_durability

    def speed(self,player):
        """
        Cette fonction permet d'augmenter la vitesse d'un tank
        """
        if player.speed <= SPEED_LIMITE: #la vitesse ne peut pas dépasser 12
            player.speed += 3  #incrémentation de la vitesse

    def slow(self,player):
        """
        Cette fonction permet de diminuer la vitesse d'un tank
        """
        if player.speed >= 2:  #la vitesse ne peut pas être inférieure à 0 (mais peut être égale à 0 -> immobile)
            player.speed -= 2  #décrémentation de la vitesse
        else :                 #si non
            player.speed = 0   #tank immobilisé

    def boom(self,player,amount:int):
        """
        Cette fonction permet de diminuer la durabilité d'un tank
        """
        if player.durability - amount > 0:      #Si le tank du player peut prendre des dégâts sans se détruire 
            player.durability -= (amount + 3)   #Tank de player perd de la durabilité
        else :                                  #Sinon (si le tank du player ne peut pas prednre des dégâts sans se détruire)
            player.durability = 0               #Tank du player détruit 
########################### CLASS BONUSMALUS -> ITEM IN MATCH #########################################
#######################################################################################################