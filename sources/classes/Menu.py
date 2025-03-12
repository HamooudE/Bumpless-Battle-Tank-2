import pygame

#Création de la class :MenuCustom: qui affiche les images pour le menu
class MenuCustom(): #Idéé: customiser le menu(/ATH/Overlay) a partire d'une classe dédier.
    def __init__(self, screen, url, xpos, ypos, xscale = None, yscale = None):

        self.screen = screen                                            #Initialise la surface d'afichage (+ peut être definit par :screnn: par defaut)
        self.url = url                                                  #Initalise l'URL du fichier image
        self.load = pygame.image.load(url).convert_alpha()              #Creer l'image à partire l'URL
        self.rect = self.load.get_rect()                                #Récupère le rectangle de l'image
        self.xpos = xpos                                                #Définit la valeur coordonné: x
        self.ypos = ypos                                                #Définit la valeur coordonné: y
        self.xscale = xscale                                            #Définit la valeur taille: x (None: taille de l'image par defaut)
        self.yscale = yscale                                            #Définit la valeur taille: y (None: taille de l'image par defaut)
                
        if self.xscale !=None and self.yscale != None :
            self.load = pygame.transform.scale(self.load, (self.xscale, self.yscale))
            self.rect = self.load.get_rect()

    def get_rect(self): #Permet de recuperer le rectangle de l'image 
        return self.rect
    
    def afficher_image(self): #Permet d'affichage l'image
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.screen.blit(self.load, self.rect)
    
    def image_update(self): #Permet d'affichage l'image
        self.rect.x = self.xpos
        self.rect.y = self.ypos
        self.load = pygame.image.load(self.url).convert_alpha()
        if self.xscale !=None and self.yscale != None :
            self.load = pygame.transform.scale(self.load, (self.xscale, self.yscale))