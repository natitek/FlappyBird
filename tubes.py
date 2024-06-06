import pygame

class tubes(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))
    def update(self,direction):
        self.rect.x += direction