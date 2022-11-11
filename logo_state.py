import game_framework
from pico2d import *
import title_state

image = None
running = True
logo_time = 0.0

def enter():
    global image
    image = load_image('tuk_credit.png')

def exit():
    global image
    del image

def update():
    global logo_time
    # global running
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.05)
    logo_time += 0.05

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()





