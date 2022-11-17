from pico2d import *
import game_world
import game_framework
width , height = 1024, 684
class Sight:
    image = None
    def __init__(self, x= 100 , y = 684//2, time = 1):
        if Sight.image == None:
            Sight.image = load_image('star.png')
        self.x, self.y, self.time = x, y, time

    def draw(self):
        self.image.draw(self.x, self.y-90)

