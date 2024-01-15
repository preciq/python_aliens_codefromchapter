# Import the pygame module, which contains the functionality needed for game development
import pygame
# Import the Sprite class from pygame.sprite module, which is a simple base class for visible game objects
from pygame.sprite import Sprite

# Define a class named Bullet that inherits from the Sprite class


class Bullet(Sprite):
    # A class to manage bullets fired from the ship

    # The constructor method for the Bullet class
    def __init__(self, game_instance):
        # Create a bullet object at the ship's current position
        # Call the constructor of the parent class (Sprite)
        super().__init__()
        # Store a reference to the game's screen object
        self.screen = game_instance.screen
        # Store a reference to the game's settings object
        self.settings = game_instance.settings_for_game
        # Store the color of the bullet
        self.color = self.settings.bullet_color
        # Create a rectangle for the bullet at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        # Position the bullet at the top center of the ship
        self.rect.midtop = game_instance.ship.rect.midtop
        # Store the bullet's vertical position as a float for more precise positioning
        self.y = float(self.rect.y)

    # Method to update the bullet's position
    def update(self):
        # Move the bullet up the screen
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rectangle's position
        self.rect.y = self.y

    # Method to draw the bullet on the screen
    def draw_bullet(self):
        # Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
