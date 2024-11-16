import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1900, 1000))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (252, 3, 3)
BLUE = (3, 3, 252)
GREEN = (3, 3, 252)

# Story state
scene = 1

def preparescene(colour,text,scan)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scene = 1
                screen.fill(WHITE)
            elif event.key == pygame.K_2:
                scene = 2
                screen.fill(RED)
            elif event.key == pygame.K_3:
                scene = 3
            elif event.key == pygame.K_4:
                scene = 4



    # Render text based on the scene
    if scene == 1:
        text = font.render("You are in a dark forest. Press 2 to go to Aidan's castle.", True, BLACK)
    elif scene == 2:
        text = font.render("You are now in the castle. Press 1 to go back to the forest or 3 to go to the shop.", True, BLACK)
    elif scene == 3:
        text = font.render("You are now in a shop. press 2 to go back to Aidan's castle", True, BLACK)
    elif scene == 4:
        text = font.render("You are now in a shop. press 3 to go back to the shop", True, BLACK)

    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()