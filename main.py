import pygame
import numpy as np
import time

pygame.init()

width, heigth = 1000,1000
screen = pygame.display.set_mode((height, width))

bg = 25,25,25
screen.fill(bg)

nxC, nyC = 25,25

dimCW = width / nxC
dimCH = heigth / nyC

game_state = np.zeros((nxC, nyC))

pause_exec = False

while True:
    
    new_game_state = np.copy(game_state)
    
    screen.fill(bg)
    time.sleep(0.1)
    
    ev = pygame.event.get()
    
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause_exec = not pause_exec
    
    
    mouse_click = pygame.mouse.get_pressed()
    
    if sum(mouse_click) > 0:
        pos_x, pos_y= pygame.mouse.get_pos()
        cel_x, cel_y = int(np.floor(pos_x / dimCW)), int(np.floor(pos_Y / dimCH))
        new_game_state[cel_x,cel_y] = int(not new_game_state[cel_x,cel_y])
    
    if pause_exec:    
        for y in range(0, nxC):
            for x in range(nyC):
                
                n_heigth = game_state[( x - 1) % nxC, ( y - 1 ) % nyC]  + \
                        game_state[( x )    % nxC, ( y - 1 ) % nyC]  + \
                        game_state[( x + 1) % nxC, ( y - 1 ) % nyC]  + \
                        game_state[( x - 1) % nxC, ( y )     % nyC]  + \
                        game_state[( x + 1) % nxC, ( y )     % nyC]  + \
                        game_state[( x - 1) % nxC, ( y + 1 ) % nyC]  + \
                        game_state[( x )    % nxC, ( y + 1 ) % nyC]  + \
                        game_state[( x + 1) % nxC, ( y + 1 ) % nyC]  
                
                if game_state[x, y] == 0 and n_heigth == 3:
                    new_game_state[x, y] = 1
                
                elif game_state[x, y] == 1 and not n_heigth in [2, 3]:
                    new_game_state[x, y] = 0
                                
                poly = [
                    ((x)   * dimCW ,   y * dimCH),
                    ((x+1) * dimCW ,   y * dimCH),
                    ((x+1) * dimCW , ( y + 1 ) * dimCH),
                    ((x)   * dimCW , ( y + 1 ) * dimCH),
                ]
                if new_game_state[x, y] == 0:
                    pygame.draw.polygon(screen, (128,128,128), poly, width=1)
                else:
                    pygame.draw.polygon(screen, (255,255,255), poly, width=0)
                
        game_state = np.copy(new_game_state)
    
    pygame.display.flip()