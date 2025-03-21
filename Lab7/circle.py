import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
radius = 25
x, y = WIDTH // 2, HEIGHT // 2
move_dist = 20

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw ball
    pygame.draw.circle(screen, RED, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - radius - move_dist >= 0:
        y -= move_dist
    if keys[pygame.K_DOWN] and y + radius + move_dist <= HEIGHT:
        y += move_dist
    if keys[pygame.K_LEFT] and x - radius - move_dist >= 0:
        x -= move_dist
    if keys[pygame.K_RIGHT] and x + radius + move_dist <= WIDTH:
        x += move_dist

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
