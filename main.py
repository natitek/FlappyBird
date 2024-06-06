import pygame , sys
import tubes
    
    
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
tube = tubes()
def run(sprite,position):
     sprite.draw(screen)
     
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                sys.exit()
    screen.fill((0,0,40))
    pygame.display.flip()
    clock.tick(60)
    run(tube,tube.x)