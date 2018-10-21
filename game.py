import pygame
import time
import sys
import string
import random
from pygame.locals import *

from pygameGUI.cursor import cursor
from pygameGUI.button import button
from pygameGUI.loadImage import loadImage
from logic.objects import objects,attack,score,cards

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
    s1=loadImage("sprites/1 sol.png")
    s2=loadImage("sprites/2 sol.png")
    s3=loadImage("sprites/3 sol.png")
    s4=loadImage("sprites/4 sol.png")
    s5=loadImage("sprites/5 sol.png")
    s6=loadImage("sprites/6 sol.png")
    

    urano=loadImage("cards/urano.png")
    dimidio=loadImage("cards/dimidio.png")
    mercurio=loadImage("cards/mercurio.png")
    neptuno=loadImage("cards/neptuno.png")
    venus=loadImage("cards/venus.png")
    jupiter=loadImage("cards/jupiter.png")
    cometCard = loadImage("cards/Cartas3-20.png")
    asteroidCard = loadImage("cards/comet.png")

    dimidioP = loadImage("planets/dimidio.png")
    jupiterP = loadImage("planets/jupiter.png")
    mercurioP = loadImage("planets/mercurio.png")
    uranoP = loadImage("planets/urano.png")
    venusP = loadImage("planets/venus.png")
    neptunoP = loadImage("planets/neptuno.png")
    jupiterP = loadImage("planets/jupiter.png")

    effect1 = loadImage("effects/Planetas-01.png")
    effect2 = loadImage("effects/Planetas-02.png")
    effect3 = loadImage("effects/Planetas-03.png")
    effect4 = loadImage("effects/Planetas-04.png")
    effect5 = loadImage("effects/Planetas-05.png")
    effect6 = loadImage("effects/Planetas-06.png")
    effect7 = loadImage("effects/Planetas-07.png")
    effect8 = loadImage("effects/Planetas-08.png")
    effect9 = loadImage("effects/Planetas-09.png")

    effects = [effect1,effect2,effect3,effect4,effect5,effect6,effect7,effect8,effect9]

    urano2=pygame.transform.scale(urano, (50,   100))
    dimidio2=pygame.transform.scale(dimidio, (50, 100))
    mercurio2=pygame.transform.scale(mercurio, (50, 100))
    neptuno2=pygame.transform.scale(neptuno, (50, 100))
    venus2=pygame.transform.scale(venus, (50, 100))
    jupiter2=pygame.transform.scale(jupiter, (50, 100))
    
    listPlanets = [uranoP,dimidioP,mercurioP,neptunoP,venusP,jupiterP]

    listCardPosIzq = [(980,381),(722,329),(692,485),(612,266),(518,552)]
    listCardPosDer = [(980,381),(1007,339),(1048,485),(1180,381),(1231,552)]


    burano=cards([urano2,urano],2,0,0)
    bdimidio=cards([dimidio2,dimidio],2,0,1)
    bmercurio=cards([mercurio2,mercurio],2,0,2)
    
    rightPlanet1 = objects([neptunoP],0,3)
    rightPlanet1.put(screen,1180,381)

    rightPlanet2 = objects([mercurioP],0,3)
    rightPlanet2.put(screen,980,381)

    listCardPosIzqCheck = [0,0,0,0]
    listCardPosDerCheck = [rightPlanet1,rightPlanet2]

    asteroidCard2=pygame.transform.scale(asteroidCard, (50, 100))
    cometCard2=pygame.transform.scale(cometCard, (50, 100))

    listMenu2 = [[asteroidCard2,asteroidCard], [cometCard2,cometCard]]

    asterC = cards(listMenu2[0],2,1,0)
    listTmp = [burano,bdimidio,bmercurio,asterC]
    listTmpPos = [(20,70), (20,190), (20,310),(20,430)]
    listMenu = [[urano2,urano],[dimidio2,dimidio],[mercurio2,mercurio],[neptuno2,neptuno],[venus2,venus],[jupiter2,jupiter]]
    
    


    burano.put(screen,20,70)
    bdimidio.put(screen,20,190)
    bmercurio.put(screen,20,310)
    asterC.put(screen,20,430)

    aster1 = loadImage("planets/aster.png")
    aster2 = loadImage("planets/aster2.png")

    comet = loadImage("planets/comet.png")
    comet = [comet]
    listOfAttack = [[aster1,aster1],[comet,comet]]
    ss=[s1,s2,s3,s4,s5,s6]
    
    aster = [aster1,aster2]
    sun=objects(ss,5,3)
    sun.put(screen,872,375)
    
    
    boom=loadImage("planets/exp.png")
    now=False
    now2=False
    while True:
        screen.blit(wallp,(0,0))
        c1=pygame.draw.circle(screen, (0,0,0),(761 , 381),15, 3)
        c2=pygame.draw.circle(screen, (0,0,0),(682 , 572), 15, 3)
        myCursor.update()
        
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key==K_DOWN:
                    attack(aster,2,4)
                if event.key==K_UP:
                    attack(comet,1,4)
            if event.type==pygame.MOUSEBUTTONDOWN:
                for obj in listTmp:
                    if myCursor.colliderect(obj.rect):
                        if(not obj.state):
                            obj.state= not obj.state
                        else: 
                            if (myCursor.colliderect(c1) and listCardPosIzqCheck[0] == 0 and obj.type == 0):
                                index = obj.index
                                listIndex = listTmp.index(obj)
                                objects(effects+[listPlanets[index]],9,1).put(screen,761 , 381)                
                                listCardPosIzqCheck[0] = 1
                                element = listMenu[random.randint(0,len(listMenu) - 1)]
                                listTmp[listIndex] = cards(element,2,0,listIndex)
                                listTmp[listIndex].put(screen, listTmpPos[listIndex][0],listTmpPos[listIndex][1])
                                obj.state= not obj.state                                
                                obj.delete(obj.instances)                                                                                

                            if(myCursor.colliderect(c2) and obj.type == 1):
                                index = obj.index
                                if index==0:
                                    attack(aster,2,4)
                                else:    
                                    attack(comet,1,4)
                                listIndex = listTmp.index(obj)
                                i = (random.randint(0,len(listMenu2) - 1))
                                element = listMenu2[i]
                                listTmp[listIndex] = cards(element,1,1,i)
                                listTmp[listIndex].put(screen, listTmpPos[listIndex][0],listTmpPos[listIndex][1])
                                obj.state= not obj.state                                
                                obj.delete(obj.instances)
                            
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for obj in listTmp:
            obj.update(screen,myCursor)
            obj.move(screen, myCursor)
        for obj in attack.instances:
            if(obj.state):obj.move(screen)
            if(obj.rect.colliderect(rightPlanet1.rect)):
                screen.blit(boom,obj.rect)
                pygame.display.flip()
                screen.blit(boom,(obj.rect))
                time.sleep(0.1)
                if now:
                    rightPlanet1.put(screen,1007,339)
                    obj.delete(obj.instances)
                    now =False
                else:
                    rightPlanet1.put(screen,1048,485)
                    obj.delete(obj.instances)
                    listCardPosIzqCheck[0] = 0
                    now =True
                
        for obj in objects.instances:
            obj.update(screen,myCursor)
            obj.move(screen, myCursor)
            if now and obj.type!=3 and not now2:
                obj.put(screen,722,329)
                now2=True
        pygame.display.flip()
        time.sleep(0.07)

main()