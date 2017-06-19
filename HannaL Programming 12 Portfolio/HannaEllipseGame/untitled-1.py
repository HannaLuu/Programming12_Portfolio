import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
 
class MyEllipse(pygame.sprite.Sprite):
 
    def __init__(self, color, width, height):
        """
        Ellipse Constructor. Pass in the color of the ellipse,
        and its size
        """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the ellipse
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        
        self.rect = self.image.get_rect()
        
class Ship(pygame.sprite.Sprite):
    
    def __init__(self):
        """ Graphic Sprite Constructor. """
     
        # Call the parent class (Sprite) constructor
        super().__init__()
     
        # Load the image
        self.image = pygame.image.load("player.bmp").convert()
     
        # Set our transparent color
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
myellipse_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    myellipse = MyEllipse(BLUE, 20, 15)
 
    # Set a random location for the block
    myellipse.rect.x = random.randrange(screen_width)
    myellipse.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    myellipse_list.add(myellipse)
    all_sprites_list.add(myellipse)
 
# Create a RED player block
player = Ship
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    myellipse_hit_list = pygame.sprite.spritecollide(player, myellipse_list, True)
 
    # Check the list of collisions.
    for myellipse in myellipse_hit_list:
        score += 1
        print(score)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
