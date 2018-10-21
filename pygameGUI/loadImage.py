import pygame
from pygame.locals import *
import sys

def loadImage(pImageName, pWallPaperFlag = 0):
    tmpImage = None
    try:
        if(pWallPaperFlag):
            tmpImage = pygame.image.load(pImageName).convert()
            
        else:
            tmpImage = pygame.image.load(pImageName)
        return tmpImage
    except:
        print("Unable to open: " + pImageName)
        sys.exit()
