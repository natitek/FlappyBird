import pygame
running=True
pygame.init()
screen=pygame.display.set_mode((800,400))
class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        #pth="green.png"
        #self.image = pygame.transform.scale(pygame.image.load(pth).convert_alpha(),(40,30))
        #self.rect = self.image.get_rect(topleft = (300,200))
        self.x=x
        self.y=y
        file_path = 'assets/flappy.png'
        self.image = pygame.transform.scale(pygame.image.load(file_path).convert_alpha(),(40,30))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.flappy=pygame.sprite.Group()
    def add(self):
        self.flappy.add(bird(self.x,self.y))
    def draw(self,window):
        self.flappy.draw(window)