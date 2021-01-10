import pygame
import random

class Jeu:
    def __init__(self, ecran):
        self.ecran = ecran

    def boucle_du_jeu(self):
        self.affichage_plateau()


    def choisir_qui_commence(self):
        alea = random.randint(1,2)
        if alea == 1:
            print("machine commence")
        else:
            print("joueur commence")

    def affichage_plateau(self):
        pygame.draw.rect(self.ecran, (0,0,0), [0,0,210,210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [5, 5, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [0, 210, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [5, 215, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [0, 420, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [5, 425, 200, 200])

        pygame.draw.rect(self.ecran, (0, 0, 0), [210, 0, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [215, 5, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [210, 210, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [215, 215, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [210, 420, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [215, 425, 200, 200])

        pygame.draw.rect(self.ecran, (0, 0, 0), [420, 0, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [425, 5, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [420, 210, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [425, 215, 200, 200])
        pygame.draw.rect(self.ecran, (0, 0, 0), [420, 420, 210, 210])
        pygame.draw.rect(self.ecran, (255, 255, 255), [425, 425, 200, 200])