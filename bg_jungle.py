from pico2d import *

width, height = 1024, 684
class BG_jungle:
    def __init__(self):
        self.image = load_image('image/background_jungle.png')
        self.bgm = load_music('bgm/play_state.mp3')
        self.bgm.set_volume(34)
        self.bgm.repeat_play()


    def update(self):
        pass

    def draw(self):
        self.image.draw(width//2, height//2)

    # def get_bb(self):
    #     return 0, self.y, self.x, self.y
    #
    # def handle_collision(self, other, group):
    #     if group == 'left:enemies':
    #         game_world.remove_object(self)
    #         # if group == 'character:enemies':
    #         #     game_world.remove_object(self)




