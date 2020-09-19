import pygame
import numpy as np

pygame.init()

width, heigth = 1000,1000
screen = pygame.display.set_mode((height, width))

bg = 25,25,25
screen.fill(bg)

nxC, nyC = 25,25

dimCW = width / nxC
dimCH = heigth / nyC

game_state = np.zeros((nxC, nyC))

while True:
    
    for y in range(0, nxC):
        for x in range(nyC):
            
            n_heigth = game_state[( x - 1), ( y - 1 )]  + \
                       game_state[( x )   , ( y - 1 )]  + \
                       game_state[( x + 1), ( y - 1 )]  + \
                       game_state[( x - 1), ( y )    ]  + \
                       game_state[( x + 1), ( y )    ]  + \
                       game_state[( x - 1), ( y + 1 )]  + \
                       game_state[( x )   , ( y + 1 )]  + \
                       game_state[( x + 1), ( y + 1 )]  
                            
            poly = [
                ((x)   * dimCW ,   y * dimCH),
                ((x+1) * dimCW ,   y * dimCH),
                ((x+1) * dimCW , ( y + 1 ) * dimCH),
                ((x)   * dimCW , ( y + 1 ) * dimCH),
            ]
            
            pygame.draw.polygon(screen, (128,128,128), poly, width=1)

    pygame.display.flip()