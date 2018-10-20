import pygame

class objects(pygame.sprite.Sprite):#se crea la clase para los botones
    def __init__(self,pics,cant):#se define cada boton con dos imagenes y las coordenadas
        self.pics=pics
        self.cant=cant
        self.pos=0
        self.basic_pic=pics[self.pos] #se define una imagen bacica qie inicia como la no seleccionada
  
    def put(self,screen,x,y):
        self.rect=self.basic_pic.get_rect()
        self.rect.left,self.rect.top=(x,y)
        screen.blit(self.basic_pic,self.rect)

    def update(self,screen):
        if (self.pos>=self.cant):
            self.pos=0
        else:
            self.pos=self.pos+1
        self.basic_pic=self.pics[self.pos]
        screen.blit(self.basic_pic,self.rect)