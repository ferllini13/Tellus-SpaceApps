import pygame
import time
import sys
import string
from pygame.locals import *

from pygameGUI.cursor import cursor
from pygameGUI.button import button
from pygameGUI.loadImage import loadImage
from logic.objects import objects,attack

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
    wallp=loadImage("backgrounds/f1.jpg",1)
    t1=loadImage("sprites/1.png")
    t2=loadImage("sprites/2.png")
    t3=loadImage("sprites/3.png")
    t4=loadImage("sprites/4.png")
    t5=loadImage("sprites/5.png")
    t6=loadImage("sprites/6.png")

    tt=[t1,t2,t3,t4,t5,t6]
    
    p1=objects(tt,5,3)
    p2=objects(tt,0,0)
    p3=objects(tt,3,4)
    p4=attack(tt,5,4)

    p1.put(screen,0,0)
    p2.put(screen,100,100)
    p3.put(screen,200,200)
    
    while True:
        screen.blit(wallp,(0,0))
        myCursor.update()
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    p4.state = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                for obj in objects.instances:
                    if myCursor.colliderect(obj.rect):
                        obj.state= not obj.state
                        #obj.delete(obj.instances)
                        #counter = 0
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for obj in attack.instances:
            if(obj.state): obj.move(screen)
        for obj in objects.instances:
            obj.update(screen)
            obj.move(screen, myCursor)
        pygame.display.flip()
        time.sleep(0.07)

main()