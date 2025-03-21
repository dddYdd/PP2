import pygame
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Load images
try:
    mickey_body = pygame.image.load('mickey.png')
    left_hand = pygame.image.load('left_hand.png')
    right_hand = pygame.image.load('right_hand.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    sys.exit()

# Scale images if necessary
mickey_body = pygame.transform.scale(mickey_body, (400, 400))
left_hand = pygame.transform.scale(left_hand, (150, 150))
right_hand = pygame.transform.scale(right_hand, (150, 150))

# Calculate positions
mickey_pos = (WIDTH // 2 - mickey_body.get_width() // 2, HEIGHT // 2 - mickey_body.get_height() // 2)
clock_center = (mickey_pos[0] + mickey_body.get_width() // 2, mickey_pos[1] + mickey_body.get_height() // 2)

# Function to rotate an image around its center
def rotate_image(image, angle):
    """Rotate an image while keeping its center."""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=(0, 0)).center)
    return rotated_image, new_rect

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Get current time
    current_time = datetime.now()
    minute_angle = -current_time.minute * 6  # Each minute represents 6 degrees
    second_angle = -current_time.second * 6  # Each second represents 6 degrees

    # Rotate hands
    rotated_right_hand, right_hand_rect = rotate_image(right_hand, minute_angle)
    rotated_left_hand, left_hand_rect = rotate_image(left_hand, second_angle)

    # Position hands
    right_hand_rect.center = clock_center
    left_hand_rect.center = clock_center

    # Draw clock
    screen.blit(mickey_body, mickey_pos)
    screen.blit(rotated_right_hand, right_hand_rect.topleft)
    screen.blit(rotated_left_hand, left_hand_rect.topleft)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
