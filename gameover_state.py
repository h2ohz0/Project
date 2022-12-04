from pico2d import *
import game_framework
import game_world
import play_state
import title_state

from bg_jungle import BG_jungle

image = None
# pause_music = True
def enter():
    bg_jungle = BG_jungle()
    global image
    image = load_image('image/game_over.png')
    bg_jungle.bgm.stop()




def exit():
    global image
    del image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.clear()
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(title_state)
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(1024//2, 684//2)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
