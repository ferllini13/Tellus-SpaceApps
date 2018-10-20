import pygame

class card(pygame.sprite.Sprite):#se crea la clase para los botones
    def __init__(self,pic1,pic2):#se define cada boton con dos imagenes y las coordenadas
        self.unselected_pic=pic1#se define como se vera la imagen sin seleccionar
        self.selected_pic=pic2 #se define como se vera la imagen seleccionada
        self.basic_pic=self.unselected_pic #se define una imagen bacica qie inicia como la no seleccionada
    
    def put(self,screen,x,y):
        self.rect=self.basic_pic.get_rect()
        self.rect.left,self.rect.top=(x,y)
        screen.blit(self.basic_pic,self.rect)