import pygame
import time
from pygameGUI.cursor import cursor


class attack(pygame.sprite.Sprite):
    tattack=[]
    battack=[]
    instances = []
    pics = None 
    cant = None
    pos = None
    state = None
    type = None

    def __init__(self,pics,cant,pType=0):#se define cada boton con dos imagenes y las coordenadas
        self.instances.append(self)
        self.pics=pics
        self.cant=cant
        self.pos=0
        self.state=False
        self.type = pType
        self.basic_pic=pics[self.pos] #se define una imagen bacica qie inicia como la no seleccionada
        self.tattack=[(1036 , 180),
            (1009 , 171) ,
            (979 , 162),
            (950 , 153),
            (924 , 148),
            (892 , 146),
            (864 , 147),
            (836 , 149),
            (808 , 153),
            (776 , 160),
            (748 , 168),
            (720 , 179) ,
            (697 , 191),
            (663 , 210),
            (638 , 229),
            (6167 , 246),
            (598 , 267),
            (582 , 292),
            (572 , 316),
            (562 , 343),
            (561 , 367),
            (560 , 392),
            (564 , 418),
            (577 , 448),
            (592 , 475),
            (625 , 450),
            (623 , 521),
            (646 , 540),
            (669 , 553)]

        self.battack=[(700 , 579),(725 , 590),(755 , 600),(784 , 610),(810 , 616),
            (842 , 620),(869 , 621),(897 , 619),(925 , 616),(958 , 610),(986 , 604),
            (1014 , 594),(1036 , 583),(1076 , 558),(1101 , 538),(1121 , 517),(1140 , 496),
            (1155 , 471),(1165 , 446),(1175 , 420),(1177 , 395),(1179 , 369),(1173 , 341),
            (1167 , 315),(1151 , 287),(1133 , 263),(1115 , 242),(1092 , 223),(1069 , 210)]
            
        self.poss=0

    def put(self,screen, xy):
        self.rect=self.basic_pic.get_rect()
        self.rect.left,self.rect.top= xy
        screen.blit(self.basic_pic,self.rect)

    def move(self,screen):
        if (self.poss>=len(self.battack)-1):
            self.state = False
            self.put(screen,(2000,2000))    
        else:
            self.poss=self.poss+1    
        self.put(screen,self.battack[self.poss])
        time.sleep(0.03)
    
    def delete(self,instances):
        instances.remove(self)
        del self
        


class objects(pygame.sprite.Sprite):#se crea la clase para los botones
    instances=[]
    pics = None 
    cant = None
    pos = None
    state = None
    type = None

    def __init__(self,pics,cant,pType=0):#se define cada boton con dos imagenes y las coordenadas
        self.instances.append(self)
        self.pics=pics
        self.cant=cant
        self.pos=0
        self.state=False
        self.type = pType
        self.basic_pic=pics[self.pos] #se define una imagen bacica qie inicia como la no seleccionada
  
    def put(self,screen,x,y):
        self.rect=self.basic_pic.get_rect()
        self.rect.left,self.rect.top=(x,y)
        screen.blit(self.basic_pic,self.rect)

    def update(self,screen):
        if(self.type == 3 or self.type == 4):
            if (self.pos>=self.cant):
                self.pos=0
            else:
                self.pos=self.pos+1
        self.basic_pic=self.pics[self.pos]
        screen.blit(self.basic_pic,self.rect)

    def move(self, screen, cursor):
        if (self.state):
            x,y = pygame.mouse.get_pos()    
            self.put(screen,x,y)
    
    def delete(self,instances):
        instances.remove(self)
        del self
