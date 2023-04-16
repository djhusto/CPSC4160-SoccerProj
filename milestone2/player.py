import pygame

class Players(object):
    def __init__(self, type):
        self.type = type
        self.x = 0
        self.y = 0

        if type == "goalie1":
            self.x = 15
            self.y = 150
        if type == "goalie2":
            self.x = 585
            self.y = 150
        if type == "def1":
            self.x = 100
            self.y = 75
        if type == "def2":
            self.x = 100
            self.y = 225
        if type == "def3":
            self.x = 500
            self.y = 75
        if type == "def4":
            self.x = 500
            self.y = 225
        if type == "mid1":
            self.x = 275
            self.y = 75
        if type == "mid2":
            self.x = 275
            self.y = 225
        if type == "att1":
            self.x = 450
            self.y = 150
        if type == "mid3":
            self.x = 325
            self.y = 75
        if type == "mid4":
            self.x = 325
            self.y = 225
        if type == "att2":
            self.x = 150
            self.y = 150

    def drawIt(self, surface, color):
        self.pos = self.x, self.y
        pygame.draw.circle(surface, color, self.pos, 15)
        #i = 2
        #pygame.draw.circle(surface, leftColor, goalPos, 15)

    #def goalieL(self):
    #    self.x = 30
    #    self.y = 100

    # def update(self):
    #     if upkeypressed:
    #         x = x + speed
    def handle_Rkeys(self):
        key = pygame.key.get_pressed()
        dist = .5
        if key[pygame.K_DOWN]:
            self.y -= dist
        elif key[pygame.K_UP]:
            self.y += dist
