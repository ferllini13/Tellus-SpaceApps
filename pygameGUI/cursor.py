import pygame

#se cra la clase cursor, que es un rectangulo qeu sigue al mouse
class cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)#cursos inicia en coordenadas 0,0 y es de 1x1
	def update(self):#actualiza la pocision del cursos dependiendo de la del mouse
		self.left,self.top=pygame.mouse.get_pos()#capta la posicion del mouse

