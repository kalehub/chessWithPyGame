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

    size = (320,320)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Caturnya TEGUH SATYA!')

    is_not_closed = True
    clock = pygame.time.Clock()
    total = 0

    while is_not_closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_not_closed = False
        screen.fill(WHITE)
            


        pygame.display.flip()




    pygame.quit()





if __name__ == '__main__':
    main()






