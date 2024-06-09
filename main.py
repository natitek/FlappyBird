import pygame
from flappy import bird
# Initialize Pygame
pygame.init()

# Set display dimensions
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Image Display')

# Load an image (replace the path with your image file)

# Blit the image onto the screen
flappy=bird(width/3,height/2)
flappy.add()
# Update the display
pygame.display.flip()

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    flappy.draw(screen)
# Clean up and quit
pygame.quit()
