import sys
import pygame

def start_game():
    # Define the background colour 
    # using RGB color coding. 
    # background_colour = (234, 212, 252) 
    background_colour = (100, 100, 100)
    
    # Define the dimensions of 
    # screen object(width,height) 
    screen = pygame.display.set_mode((800, 600))

    # Set the caption of the screen 
    # pygame.display.set_caption('Geeksforgeeks') 
    pygame.display.set_caption('Ryans SpiderWeb design')

    # Fill the background colour to the screen     
    screen.fill(background_colour)

    # Update the display using flip 
    # TO update teh display use the flip function as part of pygame.display();
    pygame.display.flip()
    
    # Variable to keep our game loop running     
    running = True
    
    # game loop  - so while running is true, do this over and over:
    while running: 
        
    # for loop through the event queue   
        for event in pygame.event.get(): 
        
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
                print('We are quitting the game now..')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('you clicked a button you clown')
            elif event.type == pygame.MOUSEWHEEL:
                print('you did sutin with the middle mouse button')
            elif event.type == pygame.KEYUP:
                print('key was released!')

def main():
    start_game()
    print('hello world from after we quit the game')
    pass

if __name__ == '__main__':
    sys.exit(main())
