#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Board.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 24.04.2021
# Last Modified Date: 24.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

import pygame

class Board:
    def drawBoard(self, screen, cA, cB):
        i_width = 0
        for i in range(0, 8):
            count = 0
            j_width = -40
            for j in range(0, 8):
                j_width+=40
                if i%2 == 0:
                    if j%2 == 0:
                        pygame.draw.rect(screen, cA,[j_width,i_width,40,40],0)
                    else:
                        pygame.draw.rect(screen, cB,[j_width,i_width,40,40],0)
                else:
                    if j%2 == 0:
                        pygame.draw.rect(screen, cB,[j_width,i_width,40,40],0)
                    else:
                        pygame.draw.rect(screen, cA,[j_width,i_width,40,40],0)
            i_width+=40
        

