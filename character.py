from pico2d import *
from fire import Fire
from sight import Sight
import game_framework
import game_world
import gameover_state

from bg_jungle import BG_jungle
import play_state
width, height = 1024, 684

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RD, LD, UD, DD, RU, LU, UU, DU, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_w): UD,
    (SDL_KEYDOWN, SDLK_s): DD,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_w): UU,
    (SDL_KEYUP, SDLK_s): DU,
    (SDL_KEYDOWN, SDLK_j): SPACE
}
class RUN:
    @staticmethod
    def enter(character, event):
        if event == RD:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1
        elif event == RU:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        if event == LD:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        elif event == LU:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1

        if event == UD:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1
        elif event == UU:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        if event == DD:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        elif event == DU:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1



    @staticmethod
    def exit(character, event):
        character.face_dir = character.dir
        if event == SPACE:
            character.fire()


    @staticmethod
    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        character.x += character.x_velocity * game_framework.frame_time
        character.y += character.y_velocity * game_framework.frame_time
        character.x = clamp(25, character.x, get_canvas_width() - 25)
        character.y = clamp(25, character.y, get_canvas_height() - 25)

    @staticmethod
    def draw(character):
        if character.x_dir>0:
            character.image.clip_draw(int(character.frame), 0, 100, 100, character.x, character.y)
            character.dir = 4
        elif character.x_dir <0:
            character.image.clip_draw(int(character.frame), 0, 100, 100, character.x, character.y)
            character.dir = 5
        elif character.x_dir ==0 and character.y_dir >0:
            character.image.clip_draw(int(character.frame), 0, 100, 100, character.x, character.y)
            character.dir = 6
        elif character.x_dir ==0 and character.y_dir <0:
            character.image.clip_draw(int(character.frame), 0, 100, 100, character.x, character.y)
            character.dir = 7
        elif character.x_dir ==0 and character.y_dir ==0:
            character.image.clip_draw(int(character.frame), abs((character.face_dir)), 100, 100, character.x, character.y)


next_state = {
    RUN:   {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UU: RUN, DU: RUN, UD: RUN, DD: RUN, SPACE: RUN}
}


class Character:
    image = None
    def __init__(self):
        self.x, self.y = 256, 350
        if Character.image is None:
            Character.image =load_image('image/char1.png')
        self.frame = 0
        self.dir = 1
        self.face_dir =4
        self.x_dir, self.y_dir = 0, 0
        self.x_velocity, self.y_velocity =0, 0
        self.q = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)
        self.font = load_font('font/ENCR10B.TTF', 32)
        self.HP = 100
        self.hit_flag = 1
        self.fail_sound = load_wav('bgm/fail.wav')



    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir, 'cur_state': self.cur_state}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def fire(self):
       # print('FIRE')
        # star = Star.star_diretion(self.dir)
        #fire = Fire(self.x, self.y, (self.RL_face_dir * 2 + self.UD_face_dir * 2) / 2)
        fire = Fire(self.x+55, self.y-25, self.dir * 0.5,self.face_dir)
        # fire.get_direction(self.RL_face_dir, self.UD_face_dir)
        game_world.add_object(fire, 1)
        return fire


    # def sight(self):
    #     print('sight')
    #     sight = Sight(self.x, self.y)
    #     game_world.add_object(sight, 2)

    def update(self):

        self.cur_state.do(self)
        self.hit_flag += game_framework.frame_time
        if len(self.q) > 0: # q??? ?????? ?????????
            event = self.q.pop()#???????????? ????????????
            self.cur_state.exit(self,event)  #?????? ????????? ?????????,
            self.cur_state = next_state[self.cur_state][event] #?????? ????????? ????????????
            self.cur_state.enter(self, event)

        if self.HP <= 0:
            self.fail_sound.play()
            game_framework.push_state(gameover_state)



    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 50, self.y + 30, f'(HP: {self.HP:.2f})', (255, 0, 0))


    def add_event(self,event):
        self.q.insert(0, event)


    def handle_event(self,event): # ????????? ????????? ???????????? ???????????? ??????
        # event ??? ????????????, ????????? ?????? rd ????????? ??????
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #????????? ?????? ???????????? ?????? ??????

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_collision(self, other, group):
        if group == 'character:enemies':
            self.HP -= 0.1
            if self.hit_flag >= 1:
                self.hit_flag = 0
        # if group == 'left:enemies':
        #     game_framework.push_state(gameover_state)
            pass


#
# from pico2d import *
# import game_world
# import game_framework
# import play_state
#
# class Character:
#
#     def __init__(self):
#         self.image = load_image('char1.png')
#
#     def handle_events(self):
#         global running
#         global dir_x, dir_y
#         events = get_events()
#         for event in events:
#             if event.type == SDL_QUIT:
#                 running = False
#             elif event.type == SDL_KEYDOWN:
#                 if event.key == SDLK_d:
#                     dir_x += 1
#                 elif event.key == SDLK_a:
#                     dir_x -= 1
#                 elif event.key == SDLK_w:
#                     dir_y += 1
#                 elif event.key == SDLK_s:
#                     dir_y -= 1
#                 elif event.key == SDLK_ESCAPE:
#                     running = False
#             elif event.type == SDL_KEYUP:
#                 if event.key == SDLK_d:
#                     dir_x -= 1
#                 elif event.key == SDLK_a:
#                     dir_x += 1
#                 elif event.key == SDLK_w:
#                     dir_y -= 1
#                 elif event.key == SDLK_s:
#                     dir_y += 1
#         pass
#
#
# running = True
#
#
# def run():
#     x = 200
#     y = 300
#     while running:
#         Character.image.draw(x, y)
#         x += dir_x * 5
#         y += dir_y * 5
#         update_canvas()
#         Character.handle_events()
#
#         delay(0.02)