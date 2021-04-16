class GameStats:
    """Track statistics for Unicorn Invasion."""

    def __init__(self, ui_game):
        """Initialize statistics."""
        self.settings = ui_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # Start Unicorn Invasion in an active state.
        self.game_active = True

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
