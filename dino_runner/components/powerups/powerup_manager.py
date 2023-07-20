import pygame

from dino_runner.components.powerups.shield import Shield


class PowerUpManager:

    def __init__(self):
        self.has_powerup = False
        self.powerup = None
        self.next_powerup_show = 100

    def update(self, game):
        if not self.has_powerup and game.score == self.next_powerup_show:
            self.create_powerup()
        if self.has_powerup:
            self.has_powerup = self.powerup.update(game.game_speed)
            if game.player.rect.colliderect(self.powerup.rect):
                self.has_powerup = False

    def create_powerup(self):
        self.powerup = Shield()
        self.has_powerup = True

    def draw(self, screen):
        if self.has_powerup:
            self.powerup.draw(screen)
