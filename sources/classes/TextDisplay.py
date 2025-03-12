import pygame

class TextDisplay:
    """
    Classe pour afficher du texte à l'écran.

    """
    def __init__(self, screen, content, font_url, color, scale, xpos, ypos):
        
        self.screen = screen  # Surface d'affichage
        self.content = content  # Contenu textuel à afficher
        self.font_url = font_url  # Chemin vers le fichier de police
        self.color = color  # Couleur du texte au format RGB
        self.scale = scale  # Taille de la police
        self.xpos = xpos  # Position horizontale du texte
        self.ypos = ypos  # Position verticale du texte
        
        # Initialisation de la police et du rendu du texte
        self.font = pygame.font.Font(self.font_url, self.scale)
        self.rendu = self.font.render(self.content, True, self.color)

    def text_update(self):
        self.rendu = self.font.render(self.content, True, self.color)
        
    def afficher_text(self):
        self.screen.blit(self.rendu, (self.xpos, self.ypos))
    