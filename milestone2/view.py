import pygame
from player import Players
from ball import Ball

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
screenColor = (132, 192, 17)
lineColor = (255, 255, 255)
ballColor = (255, 165, 0)
leftColor = (255, 255, 255)
rightColor = (0, 0, 0)
fieldCenter = FIELD_WIDTH, FIELD_LENGTH = 300, 150
midlineBegin = wid1, len1 = 300, 0
midlineEnd = wid2, len2 = 300, 600
surface = pygame.display.set_mode(SCREEN_SIZE)
image_surface = pygame.image.load("soccer-ball-realistic-png.png")
arg_img = pygame.image.load("argentinaflag.png")
image_surface = pygame.transform.scale(image_surface, (15,15))
ball_speed = x_speed, y_speed = 1, 1
#ball = Ball(surface)

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
    leftTeam()
    rightTeam()
    #pygame.draw.circle(surface, ballColor, fieldCenter, 8)

    surface.blit(image_surface, [293,143])
    

    #surface.blit(image_surface, fieldCenter)
    #MOUSE_POS = pygame.mouse.get_pos()
    #surface.blit(image_surface, MOUSE_POS)
    pygame.display.update()

def leftTeam():
    # [goalPos, def1Pos, def2Pos, mid1Pos, mid2Pos, attPos]
    # goalPos = goalX, goalY = 15, 150
    # leftGoalie = pygame.draw.circle(surface, leftColor, goalPos, 15)
    # def1Pos = def1X, def1Y = 100, 75
    # def2Pos = def2X, def2Y = 100, 225
    # LeftDef1 = pygame.draw.circle(surface, leftColor, def1Pos, 15)
    # LeftDef2 = pygame.draw.circle(surface, leftColor, def2Pos, 15)
    # mid1Pos = mid1X, mid1Y = 275, 75
    # mid2Pos = mid2X, mid2Y = 275, 225
    # LeftMid1 = pygame.draw.circle(surface, leftColor, mid1Pos, 15)
    # LeftMid2 = pygame.draw.circle(surface, leftColor, mid2Pos, 15)
    # attPos = attX, attY = 450, 150
    # LeftAtt = pygame.draw.circle(surface, leftColor, attPos, 15)
    players = [Players("goalie1"), Players("def1"), Players("def2"), Players("mid1"), Players("mid2"), Players("att1")]
    #print("GOIN THRU THE LLEFT TEAM")
    for x in players:
        #print(x.type)
        x.drawIt(surface, leftColor)
    #
    # for player in players:
    #     player.draw(surface)
        # draw playere


    #pygame.display.update()

def rightTeam():
    players = [Players("goalie2"), Players("def3"), Players("def4"), Players("mid3"), Players("mid4"), Players("att2")]
    #print("GOIN THRU THE LLEFT TEAM")
    for x in players:
        #print(x.type)
        x.drawIt(surface, rightColor)
    # defPos = defX, defY = 585, 150
    # pygame.draw.circle(surface, rightColor, defPos, 15)
    # def1Pos = def1X, def1Y = 500, 75
    # def2Pos = def2X, def2Y = 500, 225
    # pygame.draw.circle(surface, rightColor, def1Pos, 15)
    # pygame.draw.circle(surface, rightColor, def2Pos, 15)
    # mid1Pos = mid1X, mid1Y = 325, 75
    # mid2Pos = mid2X, mid2Y = 325, 225
    # pygame.draw.circle(surface, rightColor, mid1Pos, 15)
    # pygame.draw.circle(surface, rightColor, mid2Pos, 15)
    # attPos = attX, attY = 150, 150
    # pygame.draw.circle(surface, rightColor, attPos, 15)

#def upball(position):
     #surface.blit(image_surface, position)
     #pygame.display.update()
