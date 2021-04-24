#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : initUI.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 24.04.2021
# Last Modified Date: 24.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

import pygame
from Board import *
from pygame.locals import *

class initUI:
    def __init__(self):
        print('launching init')
        pygame.init()
        # colors -> have 'c'
        self.cDarkBrown = '#9C745C'
        self.cLightBrown = '#D3B38C'
        self.cWhite = (255,255,255)
        self.size = (320,320)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Caturnya TEGUH SATYA!')
        self.clock = pygame.time.Clock()

        # run the UI
        self.runUI()

    def updateDisplay(self):
        pygame.display.update()
    
    def flipDisplay(self):
        pygame.display.flip()

    def setUI(self):
        self.screen.fill(self.cWhite)
        board = Board().drawBoard(self.screen, self.cLightBrown, self.cDarkBrown)
        # pygame.display.flip()
        self.flipDisplay()
    

    def runUI(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit(0)
            self.setUI()
            # self.screen.fill(self.cWhite)
        pygame.quit()





