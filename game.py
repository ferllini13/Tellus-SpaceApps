import pygame
import sys
import string
from pygame.locals import *

from pygameGUI.cursor import cursor
from pygameGUI.button import button
from pygameGUI.loadImage import loadImage
from logic.card import card

pygame.mixer.init()
#pygame.mixer.music.load("sound.mp3")
#back_sound= pygame.mixer.Sound("back.wav")
#pygame.mixer.music.play(loops=-1)


def main():
    pygame.init()
    screen=pygame.display.set_mode([1366,768])
    #pygame.display.toggle_fullscreen
    pygame.display.set_caption("Tellus")
    myCursor=cursor()
    

    #definiciones
    wallp = loadImage("fondo1.jpg",1)
    #wallp=pygame.image.load("fondo1.jpg").convert()
    ready=loadImage("ready.png")
    ready2=loadImage("ready2.png")
    p=loadImage("p1.png")
    bready=button(ready,ready2,400,30)
    p1=card(p,p)

    x=0
    y=0
    flawDown = 0
    counter = 0
    posInit = None
    posEnd = None
    while True:
        screen.blit(wallp,(0,0))
        p1.put(screen,x,y)
        myCursor.update()
        bready.update(screen,myCursor)
        
        events=pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    y=y+100
                    p1.put(screen,x,y)
                if event.key==K_UP:
                    y=y-100
                    p1.put(screen,x,y)
                if event.key==K_LEFT:
                    x=x-100
                    p1.put(screen,x,y)
                if event.key==K_RIGHT:
                    x=x+100
                    p1.put(screen,x,y)
            if event.type == pygame.MOUSEBUTTONUP:
                counter += counter                
            if event.type == pygame.MOUSEBUTTONDOWN:
                counter += 1
                if(counter == 3):
                    counter = 0

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()

main()
