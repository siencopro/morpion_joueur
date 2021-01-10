import pygame
import random
from case import Case

class Jeu:
    def __init__(self, ecran):
        self.ecran = ecran
        self.case_une = Case()
        self.case_une.rect.x = 5
        self.case_une.rect.y = 5
        self.case_deux = Case()
        self.case_deux.rect.x = 5
        self.case_deux.rect.y = 215
        self.case_trois = Case()
        self.case_trois.rect.x = 5
        self.case_trois.rect.y = 425
        self.case_quatre = Case()
        self.case_quatre.rect.x = 215
        self.case_quatre.rect.y = 5
        self.case_cinque = Case()
        self.case_cinque.rect.x = 215
        self.case_cinque.rect.y = 215
        self.case_six = Case()
        self.case_six.rect.x = 215
        self.case_six.rect.y = 425
        self.case_sept = Case()
        self.case_sept.rect.x = 425
        self.case_sept.rect.y = 5
        self.case_huit = Case()
        self.case_huit.rect.x = 425
        self.case_huit.rect.y = 215
        self.case_neuf = Case()
        self.case_neuf.rect.x = 425
        self.case_neuf.rect.y = 425
        self.a_qui_de_jouer = ""
        self.plateau = {
            1 : "vide",
            2 : "vide",
            3 : "vide",
            4 : "vide",
            5 : "vide",
            6 : "vide",
            7 : "vide",
            8 : "vide",
            9 : "vide"
        }

    def boucle_du_jeu(self):
        self.affichage_plateau()
        if self.a_qui_de_jouer == "machine":
            self.jouer()


    def choisir_qui_commence(self):
        alea = 1 #random.randint(1,2)
        if alea == 1:
            self.a_qui_de_jouer = "machine"
            print("machine commence")
        else:
            self.a_qui_de_jouer = "joueur"
            print("joueur commence")

    def affichage_plateau(self):


        self.ecran.blit(self.case_une.image, self.case_une.rect)

        self.ecran.blit(self.case_deux.image, self.case_deux.rect)
        self.ecran.blit(self.case_trois.image, self.case_trois.rect)
        self.ecran.blit(self.case_quatre.image, self.case_quatre.rect)
        self.ecran.blit(self.case_cinque.image, self.case_cinque.rect)
        self.ecran.blit(self.case_six.image, self.case_six.rect)
        self.ecran.blit(self.case_sept.image, self.case_sept.rect)
        self.ecran.blit(self.case_huit.image, self.case_huit.rect)
        self.ecran.blit(self.case_neuf.image, self.case_neuf.rect)

    def jouer(self):
        # machine commence tour un
        if self.plateau == {1 : "vide", 2 : "vide", 3 : "vide", 4 : "vide", 5 : "vide", 6 : "vide", 7 : "vide", 8 : "vide", 9 : "vide"} :
            self.case_une.image = pygame.image.load('case_croix.png')
            self.case_une.vide = False
            self.plateau[1] = "machine"
            self.a_qui_de_jouer = "joueur"
        #machine commence tour deux
        elif self.plateau == {1 : "machine", 2 : "joueur", 3 : "vide", 4 : "vide", 5 : "vide", 6 : "vide", 7 : "vide", 8 : "vide", 9 : "vide"} :
            self.case_cinque.image = pygame.image.load('case_croix.png')
            self.case_cinque.vide = False
            self.plateau[5] = "machine"
            self.a_qui_de_jouer = "joueur"
        elif self.plateau == {1 : "machine", 2 : "vide", 3 : "joueur", 4 : "vide", 5 : "vide", 6 : "vide", 7 : "vide", 8 : "vide", 9 : "vide"} :
            self.case_neuf.image = pygame.image.load('case_croix.png')
            self.case_neuf.vide = False
            self.plateau[9] = "machine"
            self.a_qui_de_jouer = "joueur"

        elif self.plateau == {1 : "machine", 2 : "vide", 3 : "vide", 4 : "joueur", 5 : "vide", 6 : "vide", 7 : "vide", 8 : "vide", 9 : "vide"} :
            self.case_cinque.image = pygame.image.load('case_croix.png')
            self.case_cinque.vide = False
            self.plateau[5] = "machine"
            self.a_qui_de_jouer = "joueur"