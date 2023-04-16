import pygame

class Ball(object):
    def __init__ (self, surface):
        self.image = pygame.image.load("soccer-ball-realistic-png.png")
        #[]
        self.image = pygame.transform.scale(self.image, (15,15))
        surface.blit(self.image, [293,143])
