# Import the pygame module, which contains the functionality needed for game development
import pygame

# Define a class named Ship


class Ship:
    # The constructor method for the Ship class
    def __init__(self, game_instance):
        # Store a reference to the game's screen object
        self.screen = game_instance.screen
        # Store a reference to the game's settings object
        self.settings = game_instance.settings_for_game
        # Get the rectangular area of the screen, which will be used to position the ship
        self.screen_rect = game_instance.screen.get_rect()

        # Load the image for the ship and store it in self.image
        self.image = pygame.image.load('images/ship.bmp')
        # Get the rectangular area of the image, which will be used to position the image on the screen
        self.rect = self.image.get_rect()

        # Position the ship at the middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ship's horizontal position as a float for more precise positioning
        self.x = float(self.rect.x)

        # Create two flags to track the ship's movement
        self.moving_right = False
        self.moving_left = False

    # Method to update the ship's position based on the movement flags
    def update(self):
        # If the right movement flag is True and the ship's right edge is not at the screen's right edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # Move the ship to the right
            self.x += self.settings.ship_speed
        # If the left movement flag is True and the ship's left edge is not at the screen's left edge
        if self.moving_left and self.rect.left > 0:
            # Move the ship to the left
            self.x -= self.settings.ship_speed

        # Update the ship's rect object with the new x position
        self.rect.x = self.x

    # Method to draw the ship on the screen
    def draw_ship_blit(self):
        # Draw the ship at its current position
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        # sets the ships rectangle's middle position to the screens rectangle's middle position
        self.x = float(self.rect.x)
        # resets the ships x position used elsewhere for calculations, like if the ship is at the edge of the screen (done elsewhere, as mentioned)