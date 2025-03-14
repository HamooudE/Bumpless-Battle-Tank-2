####################################################################################################################################
#Ceci n'est pas une classe mais un fichier Python regroupant toutes les constantes permettant la modulation et l'équilibrage du jeu#
####################################################################################################################################
import pygame
pygame.init()  # Initialisation de Pygame
info = pygame.display.Info()

# Physique
HEIGHT =  info.current_h # Hauteur de l'écran (par défaut: 1920)
WIDTH =  info.current_w   # Largeur de l'écran (par défaut: 1080)
TAILLE_TANK = 65  # Taille du tank (par défaut: 65)
TAILLE_PROJECTILE = 55  # Taille du projectile (par défaut: 55)
VITESSE_INITIAL_BOUNCE = 3.2  # Vitesse initiale du rebond (par défaut: 3.2)    # Ne pas depasser 5 => la fonction exp s'applique ici
VITESSE_INITIAL_CHOC = 2.8  # Vitesse initiale du choc (par défaut: 2.8)        # Ne pas depasser 5 => la fonction exp s'applique ici
PERTE_VITESSE_BOUNCE = 0.04  # Perte de vitesse du rebond (par défaut: 0.04)
PERTE_VITESSE_CHOC = 0.08  # Perte de vitesse du choc (par défaut: 0.08)
# Jeu
SPEED = 12  # Vitesse (par défaut: 12)
SPEED_ROTATION = 5  # Vitesse de rotation (par défaut: 5)
SPEED_LIMITE = 45  # Limite de vitesse (par défaut: 45)
SHOOT_PLAYER = 10  # Dégats Tir du joueur (par défaut: 10)
FPS = 60  # FPS (par défaut: 60)
DURABILITY = 100  # Durabilité (par défaut: 100)
MAX_DURABILITY = 100  # Durabilité maximale (par défaut: 100)
SHOT_DELAY = 0.1  # Délai de tir (par défaut: 0.1)
DELAY_BONUS = 4  # Bonus de délai (par défaut: 4)
NOMBRE_DE_SKIN = 8  # Nombre de skins (modulable possibilité de rajouter des skin dans le selecteur)
NOMBRE_DE_THEME = 3  # Nombre de thèmes (modulable possibilité de rajouter des Themes dans le selecteur)
# Keyboard
# Player 1
FORWARD1 = pygame.K_w
LEFT1 = pygame.K_a
RIGHT1 = pygame.K_d
SHOOT1 = pygame.K_SPACE
# Player 2
FORWARD2 = pygame.K_UP
LEFT2 = pygame.K_LEFT
RIGHT2 = pygame.K_RIGHT
SHOOT2 = pygame.K_RSHIFT
# Ancienne résolution (celle d'origine)
OLD_WIDTH, OLD_HEIGHT = 1920, 1080

# Facteur d'échelle
SCALE_X = WIDTH / OLD_WIDTH
SCALE_Y = HEIGHT / OLD_HEIGHT
####################################################################################################################################
#Ceci n'est pas une classe mais un fichier Python regroupant toutes les constantes permettant la modulation et l'équilibrage du jeu#
####################################################################################################################################