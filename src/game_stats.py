class GameStats:
    """Track statistics for Alien Invasion."""
    """
    This keeps track of stuff like collisions, so we can track how many points we scored playing the game, or how many lives we have left (if the aliens collide with the ship)
    """
    def __init__(self, ai_game):
        """ Constructor, initializes statistics instance """
        self.settings = ai_game.settings_for_game
        # takes a copy of the same settings used by the game
        self.reset_stats()
        # resets values (score, lives, etc.) for a new game
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.lives = self.settings.ship_limit
        # sets the lives equal to whatever we set in the settings
        # as this is called at the beginning of the game, this essentially sets the initial lives a player has