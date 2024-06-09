import pygame , sys
from tubes import tubes
import random

class Game:
    def __init__(self):
        super().__init__()  
        self.tubes = pygame.sprite.Group()
        self.tube_time = 0
        self.ready = True
        self.random = 0
        
    def run(self):
        self.tubes.update(-2) #pass speed 
        if self.ready:
            self.make_tube()
        self.tubes.draw(screen)
        self.time_out()
        print(self.random)
        
    def tube_setup(self):
        #  tubes(screen_height,screen_width)
        tube_sprite = tubes(screen_width-10,self.random,1)
        tube_sprite2 = tubes(screen_width-10,self.random+700,-1)
        # self.tubes.add(tube_sprite,tube_sprite2)
        self.ready = False
        self.tube_time = pygame.time.get_ticks()
        
        return tube_sprite,tube_sprite2
    def time_out(self):
        if not (self.ready):
            current_time = pygame.time.get_ticks()
            if current_time - self.tube_time >= 3000:
                self.ready = True
                self.random = random.randrange(50,screen_height-50)
    def make_tube(self):
        if self.ready == True:
            # self.tubes.add(tubes(screen_width,100,1),tubes(screen_width,700,-1))
            self.tubes.add(self.tube_setup())
            
pygame.init()
screen_width = 800
screen_height = 400
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('assets/background.jpg'),(screen_width,screen_height))
lower_image = pygame.transform.scale(pygame.image.load('assets/low.png'),(screen_width,screen_height))


# BACKGROUND_IMAGE = pygame.image.load('background.png')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()
    
    pygame.display.flip()
    # screen.fill((0,0,40))
    
    screen.blit(BACKGROUND_IMAGE,(0,0))
    # screen.blit(lower_image,(0,0))
    game.run()
    clock.tick(60)
    