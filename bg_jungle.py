from pico2d import *
width, height = 1024, 684
class BG_jungle:
    def __init__(self):
        self.image = load_image('image/background_jungle.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(width//2, height//2)



