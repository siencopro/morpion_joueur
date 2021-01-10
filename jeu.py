import pygame
import random

class Jeu:
    def __init__(self, ecran):
        self.ecran = ecran

    def boucle_du_jeu(self):
        print("tralala")


    def choisir_qui_commence(self):
        alea = random.randint(1,2)
        if alea == 1:
            print("machine commence")
        else:
            print("joueur commence")

    def affichage_plateau(self):
        print("trululu")