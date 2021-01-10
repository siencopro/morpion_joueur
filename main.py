import pygame
import traceback
from jeu import Jeu

pygame.init()

jeu_en_cours = True

#génération fenetre
pygame.display.set_caption("morpion")
ecran = pygame.display.set_mode((1080,700))

#import arrière plan
ArrierePlan = pygame.image.load('bg.jpg')

#importé le jeu
jeu = Jeu(ecran)

def jeu_boucle():
    global jeu_en_cours
    try:
        # appliquer arrière plan
        ecran.blit(ArrierePlan, (0, -200))

        jeu.boucle_du_jeu()

        # mettre a jour l'écrant
        pygame.display.flip()

        # si il ferme la fenetre
        for event in pygame.event.get():
            # fermeture fenetre
            if event.type == pygame.QUIT:
                jeu_en_cours = False
                pygame.quit()

    except Exception as e:
        texte = str(traceback.extract_tb(e.__traceback__, None))
        print(texte)

while jeu_en_cours:
    jeu_boucle()