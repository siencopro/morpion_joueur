import pygame

class Case:
    def __init__(self):
        self.image = pygame.image.load('case_blanche.png')
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 5
