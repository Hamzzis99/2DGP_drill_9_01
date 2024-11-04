from pico2d import *

import game_world
from grass import Grass
#from grass2 import Grass2
from boy import Boy

# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global boy
    global grass
    global grass2

    running = True

    grass = Grass(400, 30)
    game_world.add_object(grass, 2)

    boy = Boy() # 400, 60 좌표 지정
    game_world.add_object(boy, 1)

    grass2 = Grass(400, 60)
    game_world.add_object(grass2, 0) #두번째 풀


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
