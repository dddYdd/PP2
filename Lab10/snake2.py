import pygame, random, time, psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        user_id INTEGER PRIMARY KEY REFERENCES users(id),
        level INTEGER,
        score INTEGER
    );
""")
conn.commit()

pygame.init()
WIDTH, HEIGHT, CELL_SIZE = 600, 400, 20
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

BLACK, GREEN, DARK_GREEN, RED, WHITE, ORANGE, GRAY = (0,0,0), (0,255,0), (0,155,0), (255,0,0), (255,255,255), (255,165,0), (100,100,100)

def ask_username():
    input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN and text.strip():
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        msg = font.render('Enter username and press Enter', True, WHITE)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 70))
        pygame.display.flip()
        clock.tick(30)

    return text

def get_walls(level):
    walls = []
    if level >= 2:
        for i in range(10, 20):
            walls.append((i, 5))
            walls.append((i, 15))
    if level >= 3:
        for i in range(5, 15):
            walls.append((5, i))
            walls.append((20, i))
    return walls

def draw_block(color, pos):
    x, y = pos
    pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def spawn_food():
    while True:
        pos = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
        if pos not in snake and pos not in walls:
            weight = random.choice([1, 2, 3])
            timer = time.time() + 5
            foods.append((pos, weight, timer))
            break

def restart_game():
    global snake, direction, foods, walls, score, level
    snake = [(5, 5)]
    direction = (1, 0)
    foods.clear()
    walls = get_walls(1)
    score = 0
    level = 1
    spawn_food()

def game_over():
    pause_menu(death=True)

def pause_menu(death=False):
    paused = True
    view_mode = False
    while paused:
        screen.fill((50, 50, 50))

        if not view_mode:
            if death:
                msg1 = font.render("Game Over!", True, RED)
                msg5 = font.render("C - New Game", True, WHITE)
            else:
                msg1 = font.render("Paused", True, WHITE)
                msg5 = font.render("C - Continue", True, WHITE)

            msg2 = font.render("S - Save game", True, WHITE)
            msg3 = font.render("V - View tables", True, WHITE)
            msg4 = font.render("ESC - Exit game", True, WHITE)

            screen.blit(msg1, (WIDTH//2 - 50, HEIGHT//2 - 130))
            screen.blit(msg2, (WIDTH//2 - 80, HEIGHT//2 - 80))
            screen.blit(msg3, (WIDTH//2 - 80, HEIGHT//2 - 30))
            screen.blit(msg5, (WIDTH//2 - 80, HEIGHT//2 + 20))
            screen.blit(msg4, (WIDTH//2 - 80, HEIGHT//2 + 70))
        else:
            cur.execute("""
                SELECT users.username, user_score.level, user_score.score 
                FROM users
                LEFT JOIN user_score ON users.id = user_score.user_id
                ORDER BY users.id
            """)
            data = cur.fetchall()

            title = font.render("Users and Scores:", True, WHITE)
            screen.blit(title, (20, 20))

            y_offset = 60
            for row in data:
                user, lvl, scr = row
                text = f"{user}: Level {lvl or 0}, Score {scr or 0}"
                line = font.render(text, True, WHITE)
                screen.blit(line, (20, y_offset))
                y_offset += 30

            back_text = font.render("Press B to go back", True, RED)
            screen.blit(back_text, (WIDTH - 250, HEIGHT - 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if not view_mode:
                    if event.key == pygame.K_s:
                        cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
                        conn.commit()
                    elif event.key == pygame.K_v:
                        view_mode = True
                    elif event.key == pygame.K_c:
                        if death:
                            restart_game()
                        paused = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                else:
                    if event.key == pygame.K_b:
                        view_mode = False

username = ask_username()
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()
if user:
    user_id = user[0]
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    data = cur.fetchone()
    if data:
        score, level = data
    else:
        score, level = 0, 1
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, 1, 0))
    conn.commit()
    score, level = 0, 1

snake = [(5, 5)]
direction = (1, 0)
foods = []
walls = get_walls(level)
base_speed = 5

spawn_food()
running = True

screen.fill(BLACK)
welcome = font.render(f"Welcome {username}! Level {level}", True, WHITE)
screen.blit(welcome, (WIDTH//2 - welcome.get_width()//2, HEIGHT//2 - 20))
pygame.display.flip()
time.sleep(2)

while running:
    speed = base_speed + level * 2
    clock.tick(speed)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)
    elif keys[pygame.K_p]:
        cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
        conn.commit()
        time.sleep(0.5)
    elif keys[pygame.K_ESCAPE]:
        pause_menu()

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake or head in walls:
        game_over()

    snake.insert(0, head)

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

    foods = [f for f in foods if f[2] > time.time()]
    if len(foods) == 0:
        spawn_food()

    level = score // 5 + 1
    walls = get_walls(level)

    for segment in snake:
        draw_block(GREEN if segment == snake[0] else DARK_GREEN, segment)
    for food in foods:
        draw_block(ORANGE if food[1] > 1 else WHITE, food[0])
    for wall in walls:
        draw_block(GRAY, wall)

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))
    pygame.display.flip()

pygame.quit()
cur.close()
conn.close()

