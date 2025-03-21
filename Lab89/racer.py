import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Load images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
coin_image = pygame.image.load("coin.png")

# Scale images
player_image = pygame.transform.scale(player_image, (50, 100))
enemy_image = pygame.transform.scale(enemy_image, (50, 100))
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.speed, 0)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
        self.speed = 5

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -20)
        self.speed = 4

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -20)

# Create sprite groups
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin)

# Score tracking
coin_score = 0
font = pygame.font.SysFont("Verdana", 20)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        print("Game Over!")
        running = False

    # Check for coin collection
    if pygame.sprite.spritecollide(player, coins, True):
        coin_score += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Draw all sprites
    all_sprites.draw(screen)

    # Draw score
    score_text = font.render(f"Coins: {coin_score}", True, BLACK)
    screen.blit(score_text, (SCREEN_WIDTH - 120, 10))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
