import pygame
import random

def main(mode):
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong Game")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    player_score = 0
    computer_score = 0
    paddle_width = 10
    paddle_height = 100
    player_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    computer_paddle = pygame.Rect(SCREEN_WIDTH - 50 - paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if mode == "PVP":
            if keys[pygame.K_w] and player_paddle.top > 0:
                player_paddle.y -= 5
            if keys[pygame.K_s] and player_paddle.bottom < SCREEN_HEIGHT:
                player_paddle.y += 5
        elif mode == "PVC":
            if keys[pygame.K_w] and player_paddle.top > 0:
                player_paddle.y -= 5
            if keys[pygame.K_s] and player_paddle.bottom < SCREEN_HEIGHT:
                player_paddle.y += 5

        if ball.y < computer_paddle.y:
            computer_paddle.y -= 5
        elif ball.y > computer_paddle.y + paddle_height:
            computer_paddle.y += 5

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
            ball_speed_x *= -1

        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed_y *= -1

        if ball.left <= 0:
            computer_score += 1
            ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))
        elif ball.right >= SCREEN_WIDTH:
            player_score += 1
            ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            ball_speed_x *= random.choice((1, -1))
            ball_speed_y *= random.choice((1, -1))

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, computer_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        player_text = font.render("Player: " + str(player_score), True, WHITE)
        computer_text = font.render("Computer: " + str(computer_score), True, WHITE)
        screen.blit(player_text, (50, 20))
        screen.blit(computer_text, (SCREEN_WIDTH - 250, 20))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main("PVC")  # Đặt chế độ mặc định là "PVC" khi chạy riêng pong.py
