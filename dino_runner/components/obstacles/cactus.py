import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        image_list = SMALL_CACTUS + LARGE_CACTUS
        selected_image = random.choice(image_list)
        super().__init__(selected_image)
        self.rect.y = 300
