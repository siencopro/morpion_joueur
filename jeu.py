import pygame
import random

class Jeu:
    def __init__(self, ecran):
        self.ecran = ecran


    def choisir_qui_commence:
        alea = random.randint(1,2)
        if alea == 1:
            print("machine commence")
        else:
            print("joueur commence")