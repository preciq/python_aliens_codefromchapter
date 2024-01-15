# Define a class named Settings
class Settings:
    # The constructor method for the Settings class
    def __init__(self):
        # Set the background color of the game screen to a light gray color
        # The color is specified as an RGB tuple where each value is between 0 and 255
        self.bg_color = (230, 230, 230)

        # Ship settings
        # Set the speed of the ship. The higher the number, the faster the ship will move
        self.ship_speed = 1.5
        # Sets the number of lives (ships) we have per game
        self.ship_limit = 3

        # Bullet settings
        # Set the speed of the bullets. The higher the number, the faster the bullets will move
        self.bullet_speed = 20.0
        # Set the width of the bullets in pixels
        self.bullet_width = 3
        # Set the height of the bullets in pixels
        self.bullet_height = 15
        # For testing purposes, we can make large bullets to test elimination of the entire alien fleet
        
        
        # Set the color of the bullets to a dark gray color
        # The color is specified as an RGB tuple where each value is between 0 and 255
        self.bullet_color = (60, 60, 60)

        # Set the maximum number of bullets that can be on the screen at the same time
        self.bullets_allowed = 3
        
        # Alient settings
        self.alien_speed = 1.0
        # Set the speed of each alien
        self.fleet_drop_speed = 10
        # will control how fast the aliens drop downwards when they reach the bottom of the screen
        self.fleet_direction = 1
        # will control which direction the alien fleet moves on the x axis
        # 1 means to the right
        # -1 means to the left
        
        
