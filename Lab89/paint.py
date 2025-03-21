import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = WHITE
FPS = 60

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
clock = pygame.time.Clock()

# Drawing settings
drawing = False
shape = "circle"  # default shape
start_pos = None
color = BLACK
thickness = 2

# Color options
colors = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_buttons = []

# Create color selection buttons
for i, c in enumerate(colors):
    rect = pygame.Rect(10 + i * 40, 10, 30, 30)
    color_buttons.append((rect, c))

# Shape buttons
shapes = ["circle", "rectangle", "square", "right_triangle", "equilateral_triangle", "rhombus", "eraser"]
shape_buttons = []
for i, s in enumerate(shapes):
    rect = pygame.Rect(10 + i * 110, 50, 100, 30)
    shape_buttons.append((rect, s))

# Draw shape buttons and color palette
def draw_ui():
    for rect, c in color_buttons:
        pygame.draw.rect(screen, c, rect)

    for rect, label in shape_buttons:
        pygame.draw.rect(screen, (200, 200, 200), rect)
        text = pygame.font.SysFont("Arial", 16).render(label.replace("_", " "), True, BLACK)
        screen.blit(text, (rect.x + 5, rect.y + 5))

# Shape drawing functions
def draw_shape(surface, shape, start, end, color, thickness):
    x1, y1 = start
    x2, y2 = end

    if shape == "rectangle":
        pygame.draw.rect(surface, color, pygame.Rect(min(x1, x2), min(y1, y2),
                                                     abs(x2 - x1), abs(y2 - y1)), thickness)

    elif shape == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, pygame.Rect(x1, y1, side, side), thickness)

    elif shape == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, radius, thickness)

    elif shape == "right_triangle":
        points = [start, (x1, y2), end]
        pygame.draw.polygon(surface, color, points, thickness)

    elif shape == "equilateral_triangle":
        side = abs(x2 - x1)
        height = side * math.sqrt(3) / 2
        points = [
            (x1, y2),
            (x1 + side, y2),
            (x1 + side / 2, y2 - height)
        ]
        pygame.draw.polygon(surface, color, points, thickness)

    elif shape == "rhombus":
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        points = [
            (mid_x, y1),
            (x2, mid_y),
            (mid_x, y2),
            (x1, mid_y)
        ]
        pygame.draw.polygon(surface, color, points, thickness)

    elif shape == "eraser":
        pygame.draw.line(surface, BG_COLOR, start, end, 20)

# Main loop
canvas = screen.copy()
running = True
while running:
    clock.tick(FPS)
    screen.fill(BG_COLOR)
    screen.blit(canvas, (0, 0))
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for rect, c in color_buttons:
                if rect.collidepoint(pos):
                    color = c

            for rect, s in shape_buttons:
                if rect.collidepoint(pos):
                    shape = s

            start_pos = pos
            drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = pygame.mouse.get_pos()
                draw_shape(canvas, shape, start_pos, end_pos, color, thickness)
                drawing = False

    # Show live preview
    if drawing and shape != "eraser":
        end_pos = pygame.mouse.get_pos()
        temp = canvas.copy()
        draw_shape(temp, shape, start_pos, end_pos, color, thickness)
        screen.blit(temp, (0, 0))

    pygame.display.flip()

pygame.quit()
