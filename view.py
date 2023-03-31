import pygame
import player
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
screenColor = (132, 192, 17)
lineColor = (255, 255, 255)
ballColor = (255, 165, 0)
fieldCenter = FIELD_WIDTH, FIELD_LENGTH = 300, 150
midlineBegin = wid1, len1 = 300, 0
midlineEnd = wid2, len2 = 300, 600
surface = pygame.display.set_mode(SCREEN_SIZE)
image_surface = pygame.image.load("soccer-ball-realistic-png.png")
image_surface = pygame.transform.scale(image_surface, (15,15))
#gL = goalieL()

def leftGoalBox():
    goal1LineB = wid3, len3 = 0, 115
    goal1LineE = wid4, len4 = 50, 115
    goal2LineB = wid5, len5 = 0, 185
    goal2LineE = wid6, len6 = 50, 185
    goal3LineB = wid5, len5 = 50, 115
    goal3LineE = wid6, len6 = 50, 185
    pygame.draw.line(surface, lineColor, goal1LineB, goal1LineE)
    pygame.draw.line(surface, lineColor, goal2LineB, goal2LineE)
    pygame.draw.line(surface, lineColor, goal3LineB, goal3LineE)

def rightGoalBox():
    goal1LineB = wid3, len3 = 600, 115
    goal1LineE = wid4, len4 = 550, 115
    goal2LineB = wid5, len5 = 600, 185
    goal2LineE = wid6, len6 = 550, 185
    goal3LineB = wid5, len5 = 550, 115
    goal3LineE = wid6, len6 = 550, 185
    pygame.draw.line(surface, lineColor, goal1LineB, goal1LineE)
    pygame.draw.line(surface, lineColor, goal2LineB, goal2LineE)
    pygame.draw.line(surface, lineColor, goal3LineB, goal3LineE)

def up():
    surface.fill(screenColor)
    pygame.draw.circle(surface, lineColor, fieldCenter, 15, 1)
    pygame.draw.line(surface, lineColor, midlineBegin, midlineEnd)
    leftGoalBox()
    rightGoalBox()
    #pygame.draw.circle(surface, ballColor, fieldCenter, 8)
    #surface.blit(image_surface, [295,145])
    #MOUSE_POS = pygame.mouse.get_pos()
    #surface.blit(image_surface, MOUSE_POS)
    pygame.display.update()

def upball(position):
    surface.blit(image_surface, position)
    pygame.display.update()
