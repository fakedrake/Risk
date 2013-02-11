import pygame

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
