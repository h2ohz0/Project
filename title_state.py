from pico2d import *
import game_framework
import play_state
import game_world

from bg_jungle import BG_jungle
image = None

def enter():
    clear_canvas()
    bg_jungle = BG_jungle()
    global image
    image = load_image('image/Insector_X_Title.png')
    bg_jungle.bgm.stop()

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_world.clear()
            game_framework.push_state(play_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    image.draw(1024//2,684//2)
    update_canvas()

def update():
    # global logo_time
    # delay(0.05)
    # logo_time += 0.05
    # if logo_time > 1.0:
    #     logo_time = 0
    #     # game_framework.quit()
    #     game_framework.chage_state(play_state)
    pass

def pause():
    pass

def resume():
    pass


def test_self():
    import play_state
    open_canvas()
    game_framework.run(play_state)
    close_canvas()

if __name__ == '__main__':
    test_self()





