from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('title.png')

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
    image.draw(400,300)
    update_canvas()

def update():
    global logo_time
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.chage_state(play_state)
    pass

def pause():
    pass

def resume():
    pass

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10, self.y+50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)

    def handle_events():
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                elif event.key == SDLK_i:
                    game_framework.push_state(item_state)


def test_self():
    import play_state
    open_canvas()
    game_framework.run(play_state)
    close_canvas()

if __name__ == '__main__':
    test_self()





