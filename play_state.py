from pico2d import *
import title_state
import game_framework
import game_world

from character import Character
from bg_jungle import BG_jungle

character = None
bg_jungle = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        # else:
        #     character.handle_event(event)

def enter():
    global character, bg_jungle
    character = Character()
    bg_jungle = BG_jungle()
    game_world.add_object(bg_jungle, 0)
    game_world.add_object(character, 1)

#게임 종료 - 객체를 소멸
def exit():
    game_world.clear()

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    # 게임 월드 랜더링
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()