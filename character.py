from pico2d import *
import game_world
import game_framework
import play_state

class Character:
    def handle_events(self):
        self.image = load_image('char1.png')
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


def run():
    x = 200
    y = 300
    while running:
        Character.image.draw(x, y)
        x += dir_x * 5
        y += dir_y * 5
        update_canvas()
        Character.handle_events()

        delay(0.02)