#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : moving-sc.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 24.04.2021
# Last Modified Date: 24.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>


import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill((255,0,0))
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)


def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    MyPlayer = Character((0,0,150,150))
    MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(60)
