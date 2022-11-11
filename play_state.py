from pico2d import *
import title_state
import game_framework

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        delay(0.01)

#게임 초기화 : 객체들을 생성
boy = None # c NULL
grass = None
running = True

def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True


#게임 종료 - 객체를 소멸
def exit():
    global boy, grass
    del boy
    del grass

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    boy.update()


def draw():
    # 게임 월드 랜더링
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

open_canvas()

enter()
while running:
    handle_events()
    update()
    draw()
exit()

close_canvas()

