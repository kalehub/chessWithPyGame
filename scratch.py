#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : scratch.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 22.04.2021
# Last Modified Date: 24.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

import pygame


def main():
    pygame.init()
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    DARK_BROWN = '#9C745C'
    LIGHT_BROWN = '#D3B38C'

    imgs = 'imgs/whites/bird.png'
    piecesPos_x = 0
    piecesPos_y = 280

    size = (340,340)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Caturnya TEGUH SATYA!')

    is_not_closed = True
    clock = pygame.time.Clock()
    total = 0


    while is_not_closed:
        is_clicked = False
        pawns = pygame.image.load('imgs/whites/pawns-01.png').convert_alpha()
        #pawns = pygame.image.load('imgs/whites/pawns-01.png').convert_alpha()
        pawns = pygame.transform.scale(pawns, (40, 40)) 
        # pygame.draw.rect(screen, LIGHT_BROWN, [0, 280, 40, 40], 0)

        pygame.draw.rect(screen, LIGHT_BROWN, [0, 280, 40, 40], 0)
        pygame.draw.rect(screen, DARK_BROWN, [0, 240, 40, 40], 0)
        screen.blit(pawns,(piecesPos_x, piecesPos_y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_not_closed = False
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    piecesPos_x+= event.rel[0]
                    piecesPos_y+= event.rel[1]
            
        screen.fill(WHITE)        


            
            
        # pygame.display.update()





    pygame.quit()





if __name__ == '__main__':
    main()






