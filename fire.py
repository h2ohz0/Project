from pico2d import *
import game_world
import game_framework

width, height = 1024, 684

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Fire:
    image = None
    def __init__(self, x= 100 , y = 684//2, velocity = 1,dir=4):
        if Fire.image == None:
            Fire.image = load_image('image/fire.png')
        # if Fire.shoot_sound is None:
        self.x, self.y, self.velocity,self.fire_dir = x, y, velocity, dir
        self.hit_sound = load_wav('bgm/fire.wav')
        self.hit_sound.set_volume(5)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        # if self.star_dir ==4:
        self. x += self.velocity+RUN_SPEED_PPS * game_framework.frame_time
        # elif self.star_dir ==5:
        #     self.x -= self.velocity+RUN_SPEED_PPS * game_framework.frame_time
        # elif self.star_dir ==6:
        #     self.y += self.velocity+RUN_SPEED_PPS * game_framework.frame_time
        # elif self.star_dir ==7:
        #     self.y -= self.velocity+RUN_SPEED_PPS * game_framework.frame_time

        # if self.x < 30 or self.x > width-30:
        #     game_world.remove_object(self)
        # elif self.y <30 or self.y >height -40:
        #     game_world.remove_object(self)

    # def get_direction(self, cur_RL_dir, cur_UD_dir):
    #     self.RL_direction = cur_RL_dir
    #     self.UD_direction = cur_UD_dir

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 20, self.y + 18
    def handle_collision(self, other, group):
        if group == 'fire:enemies':
            self.hit_sound.play()
            game_world.remove_object(other)