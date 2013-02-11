import pygame
from pygame.locals import *

class Gui(object):
    """Draws the board from image in resources. Gets user input and updates the
    board accordingly
    """

    def __init__(self, image_file):
        """Create the game window and load board image from given filename.
        """

        pygame.init()

        # If image is in a different category, assume that path has been passed
        board_image = pygame.image.load(image_file)

        # Match game window to board size        
        # TODO : check if image size is too large to fit in screen and
        # accomodate
        window = pygame.display.set_mode (board_image.get_size())
        window.blit(board_image, (0,0))
        pygame.display.update()

        pygame.event.set_allowed(None)    #Ignore all events
        pygame.event.set_allowed(MOUSEBUTTONDOWN)   #Except mouse clicks

    def get_user_input(self):
        """Get user input and return it in meaningful way (for example region obj)
        """

        # If an event has already occured, we assume it happened while the game
        # was not expecting it so it makes sense to ignore it
        pygame.event.clear()
        click = pygame.event.wait()
        return self.evaluate_input(click)

    def evaluate_input(self, click):
        """Evaluates user input and returns something the game loop can understand
        
        Arguments:
        - `click`: MOUSEBUTTONDOWN event to be evaluated
        """

        # Need to implement a mapping system to recognize what a given mouse
        # position needs

        return None
