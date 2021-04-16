import pygame
from pygame.sprite import Sprite

class Unicorn(Sprite):
    """A class to represent a single unicorn in the fleet."""

    def __init__(self, ui_game):
        """Initialize the unicorn and set its starting position"""
        super().__init__()
        self.screen = ui_game.screen
        self.settings = ui_game.settings

        # Load the unicorn image and set its rect attribute.
        self.image = pygame.image.load('images/candy.bmp')
        self.rect = self.image.get_rect()

        # Start each new unicorn near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the unicorn's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if unicorn is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the unicorn to the right or left"""
        self.x += (self.settings.unicorn_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x