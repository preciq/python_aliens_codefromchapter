import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        # Load the alien image and set its rect attribute.
        self.settings = ai_game.settings_for_game
        # Creates a local instance of the settings used by the main game, for use by the alien instance
        self.image = pygame.image.load('images/alien.bmp')
        # image to be used to draw the aliens in game
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        # checks to see if the alien reaches the edge of the screen
        # returns true if so
        # used to tell all aliens to move down; how far down is defined in the settings
        screen_rect = self.screen.get_rect()
        # Get current screen size (dimensions) as a rectangle
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        # boolean conidition that checks if the aliens right edge x coordinate is at or past the screens rightmost x coordinate
        # also checks if the aliens left edge x coordinate is at or past 0, which is the leftmost part of the screen
        
    def update(self):
        """Move an alien instance to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        # takes the alien speed from the settings page object, and adds it to the x value of the alien instance rectangle
        # this effectively shifts the alien rectangle to the right by however much is specified in the settings
        # fleet direction is 1 or -1, meaning the fleet moves either to the right (1) or left (-1)