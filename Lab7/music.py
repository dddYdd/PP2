import pygame
import sys
import time
from tkinter import Tk, filedialog

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 400, 250
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Музыкальный плеер")

# Загрузка изображений кнопок
try:
    play_img = pygame.image.load('play.jpg')
    pause_img = pygame.image.load('pause.jpg')
    stop_img = pygame.image.load('stop.jpg')
    next_img = pygame.image.load('next.jpg')
    prev_img = pygame.image.load('prev.png')
except pygame.error as e:
    print("Ошибка загрузки изображений:", e)
    sys.exit()

# Масштабирование изображений
button_size = (40, 40)
play_img = pygame.transform.scale(play_img, button_size)
pause_img = pygame.transform.scale(pause_img, button_size)
stop_img = pygame.transform.scale(stop_img, button_size)
next_img = pygame.transform.scale(next_img, button_size)
prev_img = pygame.transform.scale(prev_img, button_size)

# Расположение кнопок
button_y = HEIGHT - 60
play_rect = play_img.get_rect(center=(WIDTH // 2, button_y))
pause_rect = pause_img.get_rect(center=(WIDTH // 2, button_y))
stop_rect = stop_img.get_rect(center=(WIDTH // 2 - 60, button_y))
next_rect = next_img.get_rect(center=(WIDTH // 2 + 60, button_y))
prev_rect = prev_img.get_rect(center=(WIDTH // 2 - 120, button_y))

# Прогресс-бар
progress_bar_x = 20
progress_bar_y = button_y - 40
progress_bar_width = WIDTH - 40
progress_bar_height = 15

# Состояния
playlist = []
current_track_index = 0
is_playing = False
paused = False
start_time = 0
paused_time = 0

def load_music():
    global playlist, current_track_index
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(filetypes=[("Music files", "*.mp3 *.wav")])
    if files:
        playlist = list(files)
        current_track_index = 0
        play_music()

def play_music():
    global is_playing, paused, start_time, paused_time
    if playlist:
        pygame.mixer.music.load(playlist[current_track_index])
        pygame.mixer.music.play()
        is_playing = True
        paused = False
        start_time = time.time()
        paused_time = 0

def stop_music():
    global is_playing, paused, start_time, paused_time
    pygame.mixer.music.stop()
    is_playing = False
    paused = False
    start_time = 0
    paused_time = 0

def pause_music():
    global is_playing, paused, paused_time
    pygame.mixer.music.pause()
    is_playing = False
    paused = True
    paused_time = time.time() - start_time

def unpause_music():
    global is_playing, paused, start_time
    pygame.mixer.music.unpause()
    is_playing = True
    paused = False
    start_time = time.time() - paused_time

def next_track():
    global current_track_index
    if playlist:
        current_track_index = (current_track_index + 1) % len(playlist)
        play_music()

def prev_track():
    global current_track_index
    if playlist:
        current_track_index = (current_track_index - 1) % len(playlist)
        play_music()

def get_track_length():
    if playlist:
        try:
            audio = pygame.mixer.Sound(playlist[current_track_index])
            return audio.get_length()
        except:
            return 0
    return 0

def draw_progress_bar():
    if is_playing:
        elapsed = time.time() - start_time
    else:
        elapsed = paused_time
    total = get_track_length()
    progress = min(elapsed / total, 1) if total else 0
    pygame.draw.rect(screen, GRAY, (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height))
    pygame.draw.rect(screen, BLACK, (progress_bar_x, progress_bar_y, progress_bar_width * progress, progress_bar_height))

def seek_music(mouse_x):
    total = get_track_length()
    if total > 0:
        rel_x = mouse_x - progress_bar_x
        rel_x = max(0, min(rel_x, progress_bar_width))
        new_pos = rel_x / progress_bar_width
        pygame.mixer.music.play(start=new_pos * total)
        global start_time, paused_time
        start_time = time.time() - (new_pos * total)
        paused_time = 0

# Основной цикл
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Кнопки
    screen.blit(pause_img if is_playing else play_img, play_rect)
    screen.blit(stop_img, stop_rect)
    screen.blit(next_img, next_rect)
    screen.blit(prev_img, prev_rect)

    # Прогресс
    draw_progress_bar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if is_playing:
                    pause_music()
                elif paused:
                    unpause_music()
                elif not playlist:
                    load_music()
                else:
                    play_music()
            elif stop_rect.collidepoint(event.pos):
                stop_music()
            elif next_rect.collidepoint(event.pos):
                next_track()
            elif prev_rect.collidepoint(event.pos):
                prev_track()
            elif progress_bar_y <= event.pos[1] <= progress_bar_y + progress_bar_height:
                seek_music(event.pos[0])

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if is_playing:
                    pause_music()
                elif paused:
                    unpause_music()
                else:
                    load_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_o:
                load_music()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
