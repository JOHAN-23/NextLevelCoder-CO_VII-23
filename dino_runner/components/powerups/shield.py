from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import SHIELD


class Shield(PowerUp):
    def __init__(self):
        selected_image = SHIELD
        super().__init__(selected_image)

