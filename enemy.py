from pico2d import *
import random
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0) / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Enemy:
    image = None

    def __init__(self):
        if Enemy.image == None:
            Enemy.image = load_image('image/enemy1_2_1.png')
        self.frame = 5
        self.x = 1024
        self.y = random.randint(142,542)
        self.move_speed = 0.5

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        self.x -= self.move_speed * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 0:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_draw(int(self.frame)*192, 7, 192, 241, self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 10, self.y + 15

    def handle_collision(self, other, group):
        if group == 'fire:enemies':
            game_world.remove_object(self)
        # if group == 'character:enemies':
        #     game_world.remove_object(self)


# from pico2d import*
# import character
# import random
# class Walk:
#     @staticmethod
#     def enter(obj):
#         obj.x = 900
#         obj.y = random.randint(150,550)
#         obj.frame = 0
#         obj.active = True
#     @staticmethod
#     def draw(obj):
#         obj.images[0].clip_draw(int(obj.frame) * 124, 0, 124, 73, obj.x, obj.y)
#     @staticmethod
#     def update(obj):
#         obj.frame = (obj.frame + 3 * character.ACTION_PER_TIME * character.frame_time) % 3
#     @staticmethod
#     def exit(obj):
#         pass
#     @staticmethod
#     def get_bb(obj):
#         return obj.x - 62, obj.y - 36.5, obj.x + 62, obj.y + 36.5
# class Dead:
#     @staticmethod
#     def enter(obj):
#         obj.frame = 0
#
#     @staticmethod
#     def draw(obj):
#
#         obj.images[1].clip_draw(int(obj.frame) * 174,0,174,175,obj.x,obj.y)
#
#     @staticmethod
#     def update(obj):
#         if obj.frame >= 5:
#             obj.active = False
#         obj.frame = (obj.frame + 6 * character.ACTION_PER_TIME * character.frame_time ) % 6
#     @staticmethod
#     def exit(obj):
#         obj.active = False
#     @staticmethod
#     def get_bb(obj):
#         return 0,0,0,0
#
#
# class Enemy:
#     def __init__(self):
#         self.x = 900
#         self.y = 200
#         self.frame = 0
#         self.images = [load_image("image/enemy1_2.png"),load_image("image/enemy1_3.png")]
#         # self.velocity = character.GRASS_SPEED_PPS * 1.5
#         self.active = False
#         self.current_state = Dead
#     def enter(self):
#         self.x = 900
#         self.current_state.enter(self)
#     def draw(self):
#         if self.active == True:
#             self.current_state.draw(self)
#     def update(self):
#         self.current_state.update(self)
#         character.move_update(self)
#     def exit(self):
#         self.current_state.exit(self)
#     def get_bb(self):
#         return self.current_state.get_bb(self)
#     def change_state(self,state):
#         self.current_state.exit(self)
#         self.current_state = state
#         self.current_state.enter(self)
