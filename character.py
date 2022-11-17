from pico2d import *
from Star import Star
from sight import Sight
import game_framework
import game_world
width, height = 1024, 684
blind = True

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_w): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_s): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_a): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_w): UPKEY_UP,
    (SDL_KEYUP, SDLK_s): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_j): SPACE
}
class WalkingState:
    @staticmethod
    def enter(character, event):
        if event == RIGHTKEY_DOWN:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1
        elif event == RIGHTKEY_UP:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        if event == LEFTKEY_DOWN:
            character.x_velocity -= RUN_SPEED_PPS
            character.x_dir -= 1
        elif event == LEFTKEY_UP:
            character.x_velocity += RUN_SPEED_PPS
            character.x_dir += 1

        if event == UPKEY_DOWN:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1
        elif event == UPKEY_UP:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        if event == DOWNKEY_DOWN:
            character.y_velocity -= RUN_SPEED_PPS
            character.y_dir -= 1
        elif event == DOWNKEY_UP:
            character.y_velocity += RUN_SPEED_PPS
            character.y_dir += 1



    @staticmethod
    def exit(character, event):
        character.face_dir = character.dir
        if event == SPACE:
            character.star()
        elif event == SDLK_a:
            character.sight()

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


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Character:
    image = None
    def __init__(self):
        self.x, self.y = 256, 350
        if Character.image is None:
            Character.image =load_image('char1.png')
        self.frame = 0
        self.dir = 1
        self.face_dir =4
        self.x_dir, self.y_dir = 0, 0
        self.x_velocity, self.y_velocity =0, 0
        self.q = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y, 'dir': self.dir, 'cur_state': self.cur_state}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def star(self):
        # star = Star.star_diretion(self.dir)
        star = Star(self.x, self.y, self.dir * 0.5,self.face_dir)
        game_world.add_object(star, 1)

    def sight(self):
        print('sight')
        sight = Sight(self.x, self.y)
        game_world.add_object(sight, 2)
    def update(self):

        self.cur_state.do(self)
        if len(self.q) > 0: # q에 뭔가 있다면
            event = self.q.pop()#이벤트를 가져오고
            self.cur_state.exit(self,event)  #현재 상태를 나가고,
            self.cur_state = next_state_table[self.cur_state][event] #다음 상태를 계산하기
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): # 소년이 스스로 이벤트를 처리할수 있게
        # event 는 키이벤트, 이것을 내부 rd 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #변환된 내부 이벤트를 큐에 추가



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