from pico2d import *
import game_world
# from ball import Ball

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')


    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.draw(200,300)
        else:
            self.image.draw(200,300)


class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir


    def do(self):
        self.x += self.dir
        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == -1:
            self.image.draw(200,300)
        elif self.dir == 1:
            self.image.draw(200,300)


class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        pass

#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, TIMER: SLEEP},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN}
}




class Character:

    def __init__(self):
        self.x, self.y = 200,300
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('char1.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    # def fire_ball(self):
    #     print('FIRE BALL')
    #     ball = Ball(self.x, self.y, self.face_dir*2)
    #     game_world.add_object(ball, 1)

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