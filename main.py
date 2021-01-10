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
            if jeu.a_qui_de_jouer == "joueur":
                if jeu.case_une.rect.collidepoint(event.pos):
                    if jeu.case_une.vide:
                        jeu.case_une.image = pygame.image.load('case_rond.png')
                        jeu.case_une.vide = False
                        jeu.plateau[1] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_deux.rect.collidepoint(event.pos):
                    if jeu.case_deux.vide:
                        jeu.case_deux.image = pygame.image.load('case_rond.png')
                        jeu.case_deux.vide = False
                        jeu.plateau[2] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_trois.rect.collidepoint(event.pos):
                    if jeu.case_trois.vide:
                        jeu.case_trois.image = pygame.image.load('case_rond.png')
                        jeu.case_trois.vide = False
                        jeu.plateau[3] = "joueur"
                        jeu.a_qui_de_jouer = "machine"

                elif jeu.case_quatre.rect.collidepoint(event.pos):
                    if jeu.case_quatre.vide:
                        jeu.case_quatre.image = pygame.image.load('case_rond.png')
                        jeu.case_quatre.vide = False
                        jeu.plateau[4] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_cinque.rect.collidepoint(event.pos):
                    if jeu.case_cinque.vide:
                        jeu.case_cinque.image = pygame.image.load('case_rond.png')
                        jeu.case_cinque.vide = False
                        jeu.plateau[5] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_six.rect.collidepoint(event.pos):
                    if jeu.case_six.vide:
                        jeu.case_six.image = pygame.image.load('case_rond.png')
                        jeu.case_six.vide = False
                        jeu.plateau[6] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_sept.rect.collidepoint(event.pos):
                    if jeu.case_sept.vide:
                        jeu.case_sept.image = pygame.image.load('case_rond.png')
                        jeu.case_sept.vide = False
                        jeu.plateau[7] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_huit.rect.collidepoint(event.pos):
                    if jeu.case_huit.vide:
                        jeu.case_huit.image = pygame.image.load('case_rond.png')
                        jeu.case_huit.vide = False
                        jeu.plateau[8] = "joueur"
                        jeu.a_qui_de_jouer = "machine"
                elif jeu.case_neuf.rect.collidepoint(event.pos):
                    if jeu.case_neuf.vide:
                        jeu.case_neuf.image = pygame.image.load('case_rond.png')
                        jeu.case_neuf.vide = False
                        jeu.plateau[9] = "joueur"
                        jeu.a_qui_de_jouer = "machine"

    #except Exception as e:
        #texte = str(traceback.extract_tb(e.__traceback__, None))
        #print(texte)

while jeu_en_cours:
    jeu_boucle()