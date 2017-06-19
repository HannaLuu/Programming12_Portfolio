import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FOREST_GREEN = (38, 108, 46)
RED = (255, 0, 0)
BURGANDY = (140, 0, 26)
BROWN = (130, 82, 1)
LIGHT_BROWN = (193, 154, 107)
 
PI = 3.141592653

size = (1000, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Christmas Tree Drawing?")

done = False
clock = pygame.time.Clock()

while not done:
 
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(BURGANDY)
 
    for x_offset in range (460, 550, 20):
        pygame.draw.line(screen, BLACK, [x_offset, 437], [x_offset, 550], 5)
 
    pygame.draw.rect(screen, LIGHT_BROWN, [0, 600, 1000, 250], 0)
    pygame.draw.rect(screen, BROWN, [437, 550, 125, 250], 0)
 
    pygame.draw.polygon(screen, FOREST_GREEN, [[500, 100], [350, 250], [650, 250]], 0)
    pygame.draw.polygon(screen, FOREST_GREEN, [[500, 175], [250, 400], [750, 400]], 0)
    pygame.draw.polygon(screen, FOREST_GREEN, [[500, 275], [150, 550], [850, 550]], 0)
    
    for x_offset in range (460, 550, 20):
        pygame.draw.line(screen, BLACK, [x_offset, 550], [x_offset, 800], 5)    
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()