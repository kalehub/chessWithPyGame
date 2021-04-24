#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : Game.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 24.04.2021
# Last Modified Date: 24.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>


import pygame
from initUI import *

class Game:
    def __init__(self):
        print('game class')
        self.is_not_closed = True
        self.drawUI()


    def drawUI(self):
        UI = initUI().setUI()
        












