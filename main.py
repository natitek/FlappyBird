import pygame , sys
from tubes import tubes

class Game:
    def __init__(self):
         
    
        self.tubes = pygame.sprite.Group()
        self.tube_setup()
    def run(self):
         self.tubes.update(-2) #pass speed 
         self.tubes.draw(screen)
         
         
    def tube_setup(self):
        #  tubes(screen_height,screen_width)
         tube_sprite = tubes(screen_width,100,1)
         tube_sprite2 = tubes(screen_width,800,-1)
        #  tube_sprite = tubes(500,300,-1)
         self.tubes.add(tube_sprite,tube_sprite2)
pygame.init()
screen_width = 800
screen_height = 400
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('assets/background.jpg'),(screen_width,screen_height))


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
    game.run()
    clock.tick(60)
    