from pico2d import *
import random

open_canvas()

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir
    global z

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                z = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                z = 0
            elif event.key == SDLK_ESCAPE:
                running = False


def draw_curve_4_points(p1, p2, p3, p4):
    global x, y
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        x = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2


    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]

    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p1[0] + (t**3 - t**2)*p2[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p1[1] + (t**3 - t**2)*p2[1])/2


size = 10
points = [(random.randint(0, KPU_WIDTH // 2), random.randint(0, KPU_HEIGHT // 2)) for i in range(size)]
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
z = 0
n = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    draw_curve_4_points(points[n], points[n+1], points[n+2], points[n+3])
    character.clip_draw(frame * 100, z * 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    n = n + 1
    if n == 11:
        n = 1

    handle_events()

close_canvas()