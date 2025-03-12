import pygame

class Obstacle(pygame.sprite.Sprite) :
    def __init__(self,image,size:tuple,x,y):
        super().__init__() #initialisation de la class Sprite
        self.size = size #tuple : taille en pixel ex : 100px*100px
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x #initialisation de la position de l'obstacle
        self.rect.y = y #initialisation de la position de l'obstacle


