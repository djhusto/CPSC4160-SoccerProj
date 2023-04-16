import pygame
import view

pygame.init()

while True:
    for event in pygame.event.get():  #Listening for Events (key press, times, etc)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                MOUSE_POS = pygame.mouse.get_pos()
                view.upball(MOUSE_POS)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                goalY = goalY + 1
            #if event.type == pygame.KEYDOWN:

    # for player in team:
    #     player.update()


    #clock = pygame.time.Clock()
    #surface.fill(screenColor)

    view.up()

    # pygame.display.update()
