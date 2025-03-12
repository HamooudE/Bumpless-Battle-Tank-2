###################################################
############  ██████╗ ██████╗ ██████╗  ############
############  ██╔══██╗██╔══██╗██╔══██╗ ############
############  ██████╔╝██║  ██║██║  ██║ ############
############  ██╔══██╗██║  ██║██║  ██║ ############
############  ██████╔╝██████╔╝██████╔╝ ############
############  ╚═════╝ ╚═════╝ ╚═════╝  ############
###################################################


###########################################
############### BIBLIOTEQUE ###############
import csv 
import pandas
############### BIBLIOTEQUE ###############
###########################################


#######################################################################################################
########################### CLASS BDD -> LEADERBOARD / SCORE / PLAYER #################################
class Bdd:
    def __init__(self) -> None:
        #nom de la bdd
        self.file = 'web/bdd.csv'


    def score_name(self, name):
        """
        Cette fonction return les scores (victoires, défaites, dégats infligés etc...)
        correspondants à un Joueur, sous forme de dictionnaire
        """
        f = open(self.file,'r')                 #ouvre la bdd en mode lecture
        reader = csv.reader(f,delimiter=';')    #lecteur de la bdd
        lignes = list(reader)                   #liste de toute les lignes de la bdd
        f.close()                               #fermeture de la bdd
        l = []                                  #variable de stockage 
        test = None
        for ligne in lignes :                   #pour chaque ligne de la bdd
            if ligne[0] == name :               #si la ligne correspond au name du player
                l = ligne                       #on stocke la ligne
                test = 1                        #le joueur est enregistré dans la bdd
        if test is None :                       #si le joueur n'est pas enregistré dans la bdd : return None
            return {'wins':0,
                    'defeats':0, 
                    'degats_infliges': 0,
                    'degats_subis': 0,
                    'score': 0}
        else :
            return {'wins':l[1],
                    'defeats':l[2], 
                    'degats_infliges': l[3],
                    'degats_subis': l[4],
                    'score': l[5]}              #return les scores correspondant au name du player
    
    def edit_score(self,name,score:str,amount:int) :
        """
        Cette fonction permet de modifier un des scores (victoires, défaites, dégats infligés etc...) 
        d'un Joueur (passés en paramètres)
        """
        with open(self.file, 'r', newline='') as f:     #Ouverture de la bdd en mode lecture
            reader = csv.reader(f, delimiter=';')       #Objet lecture
            lignes = list(reader)                       #Mettre la bdd sous forme de liste

        with open(self.file, 'w', newline='') as fi:    #Ouverture de la bdd en mode écriture
            writer = csv.writer(fi, delimiter=';')      #Objet écriture
            for ligne in lignes:                        #Pour chaque ligne de la bdd
                if ligne[0] == name :                   #Si la ligne correspond au Joueur passé en paramètre
                    dico = {'wins':ligne[1],            #Dictionnaire des scores du Joueur
                            'defeats':ligne[2], 
                            'degats_infliges': ligne[3],
                            'degats_subis': ligne[4],
                            'score': ligne[5]}
                    if score == 'wins' :                #Si on veut modifier les victoires
                        a = int(ligne[1])               #On met le score sous forme de int (au lieu de str dans la liste)
                        a += amount                     #On l'incrémente
                        ligne[1] = str(a)               #On le replace dans liste de la bdd
                    
                    elif score == 'defeats' :           #Si on veut modifier les défaites
                        a = int(ligne[2])               #On met le score sous forme de int (au lieu de str dans la liste)
                        a += amount                     #On l'incrémente
                        ligne[2] = str(a)               #On le replace dans liste de la bdd
                    
                    elif score == 'degats_infliges' :   #Si on veut modifier les dégâts infligés
                        a = int(ligne[3])               #On met le score sous forme de int (au lieu de str dans la liste)
                        a += amount                     #On l'incrémente
                        ligne[3] = str(a)               #On le replace dans liste de la bdd
                    
                    elif score == 'degats_subis':       #Si on veut modifier les dégâts subis
                        a = int(ligne[4])               #On met le score sous forme de int (au lieu de str dans la liste)
                        a += amount                     #On l'incrémente
                        ligne[4] = str(a)               #On le replace dans liste de la bdd
                    
                    elif score == 'score':              #Si on veut modifier le Score 
                        #Calcul du Score : les différents scores du Joueur multiplié par un coefficient (100,60,5,3)
                        a = int(dico['wins'])*99 - int(dico['defeats'])*55 + int(dico['degats_infliges'])*7 - int(dico['degats_subis'])*4
                        if a < 0 :                      #Si le Score du Joueur est inférieur à 0
                            a = 0                       #On le remet à 0
                        ligne[5] = str(a)               #On remplace le Score dans liste de la bdd
                
                writer.writerow(ligne)              #On écrit 'ligne' dans la bdd

    def leader_score(self):
        """
        Cette fonction return la bdd sous forme de liste triée en fonction des Score des Joueurs
        Du plus grand Score (1er) au plus petit
        """
        data = pandas.read_csv(self.file,sep=';')           #On met la bdd en type DataFrame
        a = data.sort_values(by=['Score'],ascending=False)  #On tri la bdd en fonction des Score des joueurs
        a = a.values.tolist()                               #On met la bdd sous forme de liste
        return a                                            #On return la liste de la bdd triée


    def new_pseudo(self,pseudo):
        """
        Cette fonction vérifie si il y a un nouveau joueur et si oui écrit dans la bdd des valeurs par défauts (0)
        """
        new = True
        with open(self.file, 'r', newline='') as f:     #Ouverture de la bdd en mode lecture
            reader = csv.reader(f, delimiter=';')       #Objet lecture
            lignes = list(reader)                       #Mettre la bdd sous forme de liste

        for ligne in lignes :                           #pour chaque ligne de la bdd
            if ligne[0] == pseudo :                     #Vérifie si le pseudo est déjà connu des services de renseignement
                new = False                             #Si oui pas besoin d'ajouter de nouvelle ligne, fin de la fonction
                return None

        with open(self.file, 'w', newline='') as fi:    #Ouverture de la bdd en mode écriture
            writer = csv.writer(fi, delimiter=';')      #Objet écriture
            if new is True :
                l = [pseudo,0,0,0,0,0]
                for ligne in lignes :                   #On prend chaque ligne de la bdd
                    writer.writerow(ligne)              #On écrit 'ligne' dans la bdd
                writer.writerow(l)                      #On ajoute une nouvelle ligne neuve pour le nouveau pseudo 
        
########################### CLASS BDD -> LEADERBOARD / SCORE / PLAYER #################################
#######################################################################################################