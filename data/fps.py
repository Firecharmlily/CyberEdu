import pygame

history_length = 60

last_tick = 0
frame_data = []
for i in range(history_length):
    frame_data.append(60)

def get_time():
    global last_tick
    t = pygame.time.get_ticks()
    time_diff = t - last_tick
    last_tick = t
    return time_diff

def get_framerate():
    global frame_data
    time_diff = get_time()
    try:
        time_fps = 1000/time_diff
    except ZeroDivisionError:
        time_fps = 1000
    frame_data.append(time_fps)
    frame_data.pop(0)
    return sum(frame_data) / len(frame_data)
