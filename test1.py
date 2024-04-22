import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Player vs Player")

CLOCK = pygame.time.Clock()

# Paddles

player1 = pygame.Rect(0, 0, 10, 100)
player1.center = (WIDTH - 100, HEIGHT / 2)

player2 = pygame.Rect(0, 0, 10, 100)
player2.center = (100, HEIGHT / 2)

player1_score, player2_score = 0, 0

# Ball

ball = pygame.Rect(0, 0, 20, 20)
ball.center = (WIDTH / 2, HEIGHT / 2)

x_speed, y_speed = 1, 1

game_over = False

while not game_over:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player1.top > 0:
            player1.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if player1.bottom < HEIGHT:
            player1.bottom += 2

    if keys_pressed[pygame.K_w]:
        if player2.top > 0:
            player2.top -= 2
    if keys_pressed[pygame.K_s]:
        if player2.bottom < HEIGHT:
            player2.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        if ball.y >= HEIGHT:
            y_speed = -1
        if ball.y <= 0:
            y_speed = 1
        if ball.x <= 0:
            player1_score += 1
            if player1_score >= 10:
                game_over = True
            else:
                ball.center = (WIDTH / 2, HEIGHT / 2)
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        if ball.x >= WIDTH:
            player2_score += 1
            if player2_score >= 10:
                game_over = True
            else:
                ball.center = (WIDTH / 2, HEIGHT / 2)
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])

        if player1.x - ball.width <= ball.x <= player1.right and ball.y in range(player1.top - ball.width,
                                                                                 player1.bottom + ball.width):
            x_speed = -1
        if player2.x - ball.width <= ball.x <= player2.right and ball.y in range(player2.top - ball.width,
                                                                                 player2.bottom + ball.width):
            x_speed = 1

    player1_score_text = FONT.render("Player 1: " + str(player2_score), True, "white")
    player2_score_text = FONT.render("Player 2: " + str(player1_score), True, "white")

    player1_score_rect = player1_score_text.get_rect(center=(WIDTH - 1000, 50))
    player2_score_rect = player2_score_text.get_rect(center=(WIDTH * 3 / 4, 50))

    ball.x += x_speed * 2
    ball.y += y_speed * 2

    SCREEN.fill("Black")

    # Draw dashed line in the middle
    dash_length = 10
    dash_gap = 5
    dash_y = 0
    while dash_y < HEIGHT:
        pygame.draw.rect(SCREEN, "white", pygame.Rect(WIDTH / 2 - 2.5, dash_y, 5, dash_length))
        dash_y += dash_length + dash_gap

    pygame.draw.rect(SCREEN, "white", player1)
    pygame.draw.rect(SCREEN, "white", player2)

    # Draw ball only if game is not over
    if not game_over:
        pygame.draw.circle(SCREEN, "white", ball.center, 10)

    SCREEN.blit(player1_score_text, player1_score_rect)
    SCREEN.blit(player2_score_text, player2_score_rect)

    pygame.display.update()
    CLOCK.tick(300)

# Display winner message
if player1_score >= 10:
    winner_text = "Player 2 Wins!"
else:
    winner_text = "Player 1 Wins!"

winner_text_render = FONT.render(winner_text, True, "white")
winner_text_rect = winner_text_render.get_rect(center=(WIDTH / 2, HEIGHT / 2))
SCREEN.blit(winner_text_render, winner_text_rect)
pygame.display.update()
pygame.time.delay(10000)  # Delay 3 seconds before quitting
import test3
