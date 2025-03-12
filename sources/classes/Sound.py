import pygame
from pygame.mixer import Sound
import pandas as pd
from classes.Bdd import Bdd
pygame.mixer.init()

class MakeSound():
    def __init__(self, url, volume:float = 1):

        self.url = url
        self.volume = volume
        self.sound = pygame.mixer.Sound(self.url)
        self.sound.set_volume(self.volume)
    
    def play(self): 
        self.sound.play()
