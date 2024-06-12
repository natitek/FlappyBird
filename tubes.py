import pygame

class tubes(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        if direction == 1:
            self.image = pygame.image.load("assets/pipe.png").convert_alpha()
            self.rect = self.image.get_rect(bottomleft = (x,y))
        else:
            self.image = pygame.image.load("assets/pipe_2.png").convert_alpha()
            self.rect = self.image.get_rect(bottomleft = (x,y))

    def destroy(self):
         if self.rect.x < -100:
            self.kill()
    def update(self,speed):
         self.rect.x += speed
         self.destroy()
        
        
