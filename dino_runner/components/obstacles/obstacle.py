from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    SCREEN_WIDTH
)

class Obstacle(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x > 0 # true if image is still on the screen, false otherwise
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)
