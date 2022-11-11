from pico2d import *

class BG_jungle:
    def __init__(self):
        self.image = load_image('background_jungle.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 300)



