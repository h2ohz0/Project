from pico2d import *
import time
import title_state
import game_framework
import game_world
import pause_state

from character import Character
from bg_jungle import BG_jungle
from character import Character
from enemy import Enemy
import fire

enemies = []
character = None
bg_jungle = None
i_flag = 0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(pause_state)
        else:
            character.handle_event(event)

def enter():
    global character, bg_jungle
    character = Character()
    bg_jungle = BG_jungle()
    game_world.add_object(bg_jungle, 0)
    game_world.add_object(character, 1)

def add_enemy():
    global enemy
    enemy = Enemy()
    # enemies.append(Enemy())
    game_world.add_object(enemy, 1)
    game_world.add_collision_group(character, enemy, 'character:enemies')
    game_world.add_collision_group(character.fire(), enemy, 'fire:enemies')

#게임 종료 - 객체를 소멸
def exit():
    game_world.clear()

#게임 월드 객체를 업데이트 - 게임 로직
def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if colide(a, b):
            print('COLLISION by ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    global i_flag
    i_flag += 1
    if i_flag == 500:
        add_enemy()
        i_flag = 0
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


def colide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()