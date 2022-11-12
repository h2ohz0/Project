from pico2d import *

class Enemy:
    def __init__(self):
        self.image = load_image('enemy1_1.png')

    def update(self):
        pass

    def draw(self):
        self.frame = 0
        self.image.clip_draw(self.frame * 100, 100 * 1, 103, 120, 600, 300)


    def handle_events():
        global running
        global dir_x, dir_y
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    dir_x += 1
                elif event.key == SDLK_a:
                    dir_x -= 1
                elif event.key == SDLK_w:
                    dir_y += 1
                elif event.key == SDLK_s:
                    dir_y -= 1
                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_d:
                    dir_x -= 1
                elif event.key == SDLK_a:
                    dir_x += 1
                elif event.key == SDLK_w:
                    dir_y -= 1
                elif event.key == SDLK_s:
                    dir_y += 1
        pass


running = True

while running:
    clear_canvas()
    update_canvas()
    Enemy.handle_events()
    frame = (frame + 1) % 5

    delay(0.05)
