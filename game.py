import pygame
import random
import time

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Obstacles & Rewards")

clock = pygame.time.Clock()

# Game settings
BLOCK = 10
BASE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
ORANGE = (255, 165, 0)  # Reward food


# Load background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 30)

def draw_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, (10, 10))

def draw_snake(snake, direction):
    for block in snake[:-1]:
        pygame.draw.rect(screen, DARK_GREEN, (*block, BLOCK, BLOCK))

    head_x, head_y = snake[-1]
    pygame.draw.rect(screen, GREEN, (head_x, head_y, BLOCK, BLOCK))

    # Eyes
    if direction == "RIGHT":
        eyes = [(head_x + 7, head_y + 3), (head_x + 7, head_y + 7)]
    elif direction == "LEFT":
        eyes = [(head_x + 2, head_y + 3), (head_x + 2, head_y + 7)]
    elif direction == "UP":
        eyes = [(head_x + 3, head_y + 2), (head_x + 7, head_y + 2)]
    else:
        eyes = [(head_x + 3, head_y + 7), (head_x + 7, head_y + 7)]

    for eye in eyes:
        pygame.draw.circle(screen, BLACK, eye, 2)

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    direction = "RIGHT"

    snake = []
    snake_length = 1
    score = 0
    speed = BASE_SPEED

    food_x = random.randrange(0, WIDTH, BLOCK)
    food_y = random.randrange(0, HEIGHT, BLOCK)

    reward_x = random.randrange(0, WIDTH, BLOCK)
    reward_y = random.randrange(0, HEIGHT, BLOCK)
    reward_active = False
    reward_timer = 0

    # Obstacles (fixed)
    obstacles = [
        (200, 200), (210, 200), (220, 200),
        (300, 100), (300, 110), (300, 120),
        (400, 300), (410, 300), (420, 300)
    ]

    reward_active = True
    reward_start_time = pygame.time.get_ticks()
    REWARD_DURATION = 5000  # 5 seconds
    REWARD_GROWTH = 5  # grows by 5 blocks

    # Reward food settings
    reward_x = random.randrange(0, WIDTH, BLOCK)
    reward_y = random.randrange(0, HEIGHT, BLOCK)
    reward_active = True
    reward_start_time = pygame.time.get_ticks()

    REWARD_DURATION = 5000  # milliseconds (5 seconds)
    REWARD_GROWTH = 5  # snake grows by 5 blocks

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press C to Restart or Q to Quit", True, RED)
            screen.blit(msg, (60, HEIGHT // 2))
            draw_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK, 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK, 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK
                    direction = "DOWN"

        # Draw reward food
        if reward_active:
            pygame.draw.rect(screen, ORANGE, (reward_x, reward_y, BLOCK, BLOCK))

            # Check reward timer
            if pygame.time.get_ticks() - reward_start_time > REWARD_DURATION:
                reward_x = random.randrange(0, WIDTH, BLOCK)
                reward_y = random.randrange(0, HEIGHT, BLOCK)
                reward_start_time = pygame.time.get_ticks()

        # If snake eats reward food within time
        if reward_active and x == reward_x and y == reward_y:
            snake_length += REWARD_GROWTH  # BIG growth
            score += 50

            # Move reward to new position
            reward_x = random.randrange(0, WIDTH, BLOCK)
            reward_y = random.randrange(0, HEIGHT, BLOCK)
            reward_start_time = pygame.time.get_ticks()

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        x += dx
        y += dy

        screen.blit(background, (0, 0))

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, BLUE, (*obs, BLOCK, BLOCK))

        # Draw food
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK, BLOCK))

        # Reward logic
        if not reward_active and random.randint(1, 300) == 1:
            reward_active = True
            reward_timer = pygame.time.get_ticks()

        if reward_active:
            pygame.draw.rect(screen, ORANGE, (reward_x, reward_y, BLOCK, BLOCK))
            if pygame.time.get_ticks() - reward_timer > 5000:
                reward_active = False

        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        # Collision with self
        if snake_head in snake[:-1]:
            game_close = True

        # Collision with obstacle
        if tuple(snake_head) in obstacles:
            game_close = True

        # Eat food
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, BLOCK)
            food_y = random.randrange(0, HEIGHT, BLOCK)
            snake_length += 1
            score += 10

        # Eat reward
        if reward_active and x == reward_x and y == reward_y:
            score += 50
            speed += 3
            reward_active = False

        draw_snake(snake, direction)
        draw_score(score)

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
