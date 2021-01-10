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

    def boucle_du_jeu(self):
        self.affichage_plateau()


    def choisir_qui_commence(self):
        alea = random.randint(1,2)
        if alea == 1:
            print("machine commence")
        else:
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