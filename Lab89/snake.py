import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Snake initialization
snake = [(5, 5)]
direction = (1, 0)

# Food
foods = []

# Score, level, speed
score = 0
level = 1
speed = 3

# Timed food list
timed_foods = []

# Function to draw a block
def draw_block(color, pos):
    x, y = pos
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Spawn food avoiding snake
def spawn_food():
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            weight = random.choice([1, 2, 3])  # Weight of the food
            timer = time.time() + 5           # Food disappears after 5 seconds
            foods.append((pos, weight, timer))
            break

# Game Over function
def game_over():
    msg = font.render("Game Over!", True, RED)
    screen.blit(msg, (WIDTH // 2 - 50, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    exit()

# Main game loop
running = True
spawn_food()
while running:
    clock.tick(speed)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Move snake
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check collision with wall
    if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS):
        game_over()

    # Check collision with self
    if head in snake:
        game_over()

    snake.insert(0, head)

    # Check for food collection
    collected = False
    for food in foods:
        if head == food[0]:
            score += food[1]
            foods.remove(food)
            spawn_food()
            collected = True
            break

    if not collected:
        snake.pop()

    # Remove expired food
    current_time = time.time()
    foods = [f for f in foods if f[2] > current_time]
    if len(foods) == 0:
        spawn_food()

    # Level and speed increase
    level = score // 5 + 1
    speed = 10 + level * 2

    # Draw snake
    for segment in snake:
        draw_block(GREEN if segment == snake[0] else DARK_GREEN, segment)

    # Draw food
    for food in foods:
        draw_block(ORANGE if food[1] > 1 else WHITE, food[0])

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    pygame.display.flip()

pygame.quit()
