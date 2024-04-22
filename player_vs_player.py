import pygame

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong - Player vs Player")

# Các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Các font chữ
font = pygame.font.Font(None, 36)

# Hàm hiển thị màn hình chọn chế độ
def show_game():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    player_text = font.render("Player: " + str(player_score), True, WHITE)
    opponent_text = font.render("Opponent: " + str(opponent_score), True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (SCREEN_WIDTH - 250, 20))
    pygame.display.flip()

# Biến đánh dấu chế độ chơi
player_score = 0
opponent_score = 0
paddle_width = 10
paddle_height = 100
player_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(SCREEN_WIDTH - 50 - paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= 5
    if keys[pygame.K_s] and player_paddle.bottom < SCREEN_HEIGHT:
        player_paddle.y += 5

    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= 5
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < SCREEN_HEIGHT:
        opponent_paddle.y += 5

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed_x *= -1

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.left <= 0:
        opponent_score += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x *= -1
    elif ball.right >= SCREEN_WIDTH:
        player_score += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x *= -1

    show_game()
    pygame.time.Clock().tick(60)

# Kết thúc Pygame
pygame.quit()
