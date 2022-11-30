from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('image/press_space_continue.jpg')

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)

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
