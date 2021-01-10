import pygame
import traceback

pygame.init()

#génération fenetre
pygame.display.set_caption("morpion")
ecran = pygame.display.set_mode((1080,700))

#import arrière plan
ArrierePlan = pygame.image.load('image/bg.jpg')

#importé le jeu
jeu = Jeu(ecran)

def jeu_boucle():
    try:


    except Exception as e:
        texte = str(traceback.extract_tb(e.__traceback__, None))
        print(texte)
