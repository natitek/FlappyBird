import pygame
class bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/flappy.png").convert_alpha(),(60,33))
        self.rect = self.image.get_rect(topleft = (300,200))
        self.speed=3
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and (self.rect.y-self.speed)>0:
            self.rect.y-=self.speed+8
        else:
            self.rect.y+=self.speed
    