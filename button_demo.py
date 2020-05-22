# Imports
import pygame
from buttons import *

# Initialize game engine
pygame.init()

# Window
WIDTH = 550
HEIGHT = 300
TITLE = "Button Demo"
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN1 = (0, 200, 0)
GREEN2 = (0, 125, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)

# Fonts
MY_FONT = pygame.font.Font(None, 30)

# Functions    
def thing1():
    print(1)

def thing2():
    print(2)

# Make buttons
button1 = Button("Click me!", 100, 100, 150, 50, GREEN1, GREEN2, WHITE, MY_FONT)
button2 = Button("Click me too!", 300, 100, 150, 50, GREEN1, GREEN2, WHITE, MY_FONT)

# Game loop
running = True

while running:
    # Set base state
    do_thing1 = False
    do_thing2 = False

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            do_thing1 = button1.is_clicked()
            do_thing2 = button2.is_clicked()

    # Game logic
    if do_thing1:
        thing1()
    elif do_thing2:
        thing2()
        
    # Drawing code
    window.fill(BLUE)
    button1.draw(window)
    button2.draw(window)
    
    # Update window
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
