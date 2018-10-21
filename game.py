import pygame
import time
import sys
import string
from pygame.locals import *

from pygameGUI.cursor import cursor
from pygameGUI.button import button
from pygameGUI.loadImage import loadImage
from logic.objects import objects,attack,score

pygame.mixer.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
#pygame.mixer.music.load("sound.mp3")
#back_sound= pygame.mixer.Sound("back.wav")
#pygame.mixer.music.play(loops=-1)


def main():
    pygame.init()
    screen=pygame.display.set_mode([1366,768])
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
    

    urano=loadImage("cards/urano.png")
    dimidio=loadImage("cards/dimidio.png")
    mercurio=loadImage("cards/mercurio.png")
    neptuno=loadImage("cards/neptuno.png")
    venus=loadImage("cards/venus.png")
    jupiter=loadImage("cards/jupiter.png")

    urano2=pygame.transform.scale(urano, (50,   100))
    dimidio2=pygame.transform.scale(dimidio, (50, 100))
    mercurio2=pygame.transform.scale(mercurio, (50, 100))
    neptuno2=pygame.transform.scale(neptuno, (50, 100))
    venus2=pygame.transform.scale(venus, (50, 100))
    jupiter2=pygame.transform.scale(jupiter, (50, 100))
    

    #burano=objects([urano,urano2],0,0)
    #bdimidio=objects([dimidio,dimidio2],0,0)
    #bmercurio=objects([mercurio,mercurio2],0,0)
    #bneptuno=objects([neptuno,neptuno2],0,0)
    #bvenus=objects([venus,venus2],0,0)
    #bjupiter=objects([jupiter,jupiter2],0,0)
    
    #burano.put(screen,50,668)
    #bdimidio.put(screen,110,668)
    #bmercurio.put(screen,170,668)

    tt=[t1,t2,t3,t4,t5,t6]
    
    p1=objects(tt,5,3)
    #p2=objects(tt,0,0)
    #p3=objects(tt,3,4)

    p1.put(screen,0,0)
    #p2.put(screen,100,100)
    #p3.put(screen,200,200)

    while True:
        screen.blit(wallp,(0,0))
        c1=pygame.draw.circle(screen, (0,0,0),(761 , 381), 10, 5)
        myCursor.update()
        
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    attack(tt,5,4)
            if event.type==pygame.MOUSEBUTTONDOWN:
                for obj in objects.instances:
                    if myCursor.colliderect(obj.rect):
                        if(not obj.state):
                            obj.state= not obj.state
                        else: 
                            if (myCursor.colliderect(c1)):
                                obj.state= not obj.state
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for obj in attack.instances:
            if(obj.state):obj.move(screen)
        for obj in objects.instances:
            obj.update(screen)
            obj.move(screen, myCursor)
        pygame.display.flip()
        time.sleep(0.07)

main()