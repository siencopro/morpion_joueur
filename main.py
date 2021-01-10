import pygame
import traceback
from jeu import Jeu

pygame.init()

jeu_en_cours = True

#génération fenetre
pygame.display.set_caption("morpion")
ecran = pygame.display.set_mode((630,630))

#import arrière plan
ArrierePlan = pygame.image.load('bg.png')

#importé le jeu
jeu = Jeu(ecran)

jeu.choisir_qui_commence()

def jeu_boucle():
    global jeu_en_cours
    #try:
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


        #clique de la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if jeu.case_une.rect.collidepoint(event.pos):
                jeu.case_une.image = pygame.image.load('case_rond.png')
            elif jeu.case_deux.rect.collidepoint(event.pos):
                jeu.case_deux.image = pygame.image.load('case_rond.png')
            elif jeu.case_trois.rect.collidepoint(event.pos):
                jeu.case_trois.image = pygame.image.load('case_rond.png')

    #except Exception as e:
        #texte = str(traceback.extract_tb(e.__traceback__, None))
        #print(texte)

while jeu_en_cours:
    jeu_boucle()