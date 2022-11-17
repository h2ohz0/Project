import game_framework
import pico2d

import play_state

pico2d.open_canvas(1024, 684)
game_framework.run(play_state)
pico2d.close_canvas()

# import game_framework
#
# import play_state
#
# open_canvas()
#
# bg_jungle = load_image('background_jungle.png')
# character = load_image('char1.png')
# enemy = load_image('enemy1_1.png')
#
#
# def handle_events():
#     global running
#     global dir_x, dir_y
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_d:
#                 dir_x += 1
#             elif event.key == SDLK_a:
#                 dir_x -= 1
#             elif event.key == SDLK_w:
#                 dir_y += 1
#             elif event.key == SDLK_s:
#                 dir_y -= 1
#             elif event.key == SDLK_ESCAPE:
#                 running = False
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_d:
#                 dir_x -= 1
#             elif event.key == SDLK_a:
#                 dir_x += 1
#             elif event.key == SDLK_w:
#                 dir_y -= 1
#             elif event.key == SDLK_s:
#                 dir_y += 1
#     pass
#
#
# running = True
# x = 200
# y = 300
# frame = 0
# dir_x = 0
# dir_y = 0
# while running:
#     clear_canvas()
#     bg_jungle.draw(400, 300)
#     character.draw(x, y)
#     enemy.clip_draw(frame * 100, 100 * 1, 103, 120, 600, 300)
#     x += dir_x * 5
#     y += dir_y * 5
#     update_canvas()
#     handle_events()
#     frame = (frame + 1) % 5
#
#     delay(0.02)
#
# close_canvas()