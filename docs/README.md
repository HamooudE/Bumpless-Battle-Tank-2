# Modification du code

Bien que le jeux soit terminé et que nous avons pris le temps de l'équilibrer, vous pourriez être tanté de modifier certaines choses et explorer le fonctionnement du code.

Et c'est ce que nous vous invitons a faire, voila quelque detail sur de potentiel modification:

- La modification des Frames Per Second, les FPS sont tout à fait manipulable en fonction des performences de la machine qui fait tourner le jeux.
Dans ``main.py``, modifier 60 par la valeur choisis, -1 permet de ne pas limiter les FPS.
	> clock.tick(60) # -1 : NO FPS CAP 

## Résumé des fonctionnalités implantées

Voici un résumé des fonctionnalités qui ont au moins connu l'étape de conception.

|                |Idée Depart                    |Rendu Finale                 |
|----------------|-------------------------------|-----------------------------|
|Rebond Bordure  |||
|Bounce          |||
|Multimodes      |Foot, Slide, 1VS1              ||

## Partie Mathematique

En effet, la simulation d'une physique pareille nous a contraint à des recherches pour comprendre comment manipuler la partie vectorielle.

La *fonction Exponentiel* afin d'obtenir une fluidité de recul lors d'un ``Bounce``.

$$
	f(x) = \exp^x
$$


# Documentation

# Classes

Vous trouverez a la suite, une liste de la documentation de chaque classe, vous pouvais acceder au classes dans les liens ``VOIR PLUS``.

## main.py

Cette classe permet de lancer le jeu, de gérer certains évenments.

Voir plus de detail: [main.py](../sources/main.py)

## Game

Cette classe permet de gérer le jeu, actualisation du jeu, fin de partie, réinitialisation du jeu .

Voir plus de detail: [Game.py](../sources/classes/Game.py)

## Player

Cette classe permet de gérer les tank (déplacement, tir) .

Voir plus de detail: [Player.py](../sources/classes/Player.py)

## Projectile

Cette classe permet de gérer les projectiles envoyés par les tanks (déplacement, dégâts etc).

Voir plus de detail: [Projectile.py](../sources/classes/Projectile.py)

## Sound

Cette classe permet de gérer les sons du jeu (clic sur un bouton, tir etc) .

Voir plus de detail: [Sound.py](../sources/classes/Sound.py)

## BonusMalus

Cette classe permet de gérer les Bonus et les Malus que les tank peuvent prendre en jeu (durabilité, vitesse) .

Voir plus de detail: [BonusMalus.py](../sources/classes/BonusMalus.py)

## TextDisplay

Cette classe permet d'afficher du texte sur le fenêtre de jeu (menu, en partie) .

Voir plus de detail: [TextDisplay.py](../sources/classes/TextDisplay.py)

## obstacle

Cette classe permet de gérer les obstacles et leur fonctionnalité obstacle .

Voir plus de detail: [Obstacle.py](../sources/classes/Obstacle.py)

## Bdd

Cette classe permet de gérer la base de données .

Voir plus de detail: [Bdd.py](../sources/classes/Bdd.py)

## Menu

Cette classe permet de générer un menu et de le gérer .

Voir plus de detail: [Menu.py](../sources/classes/Menu.py)

# Controles

## Joueur 1 (gauche)

Avancer : Z 

Rotation (gauche/droite): Q/D 

Tirer : Espace

## Joueur 2 (droite)

Avancer : flèche du haut 

Rotation (gauche/droite) : flèche de gauche/flèche de droite 

Tirer : control droit 



