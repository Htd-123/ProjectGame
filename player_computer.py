import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 1280, 720

FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Player vs Computer")

CLOCK = pygame.time.Clock()

# Paddles

player = pygame.Rect(0, 0, 10, 100)
player.center = (WIDTH - 100, HEIGHT / 2)

opponent = pygame.Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT / 2)

player_score, opponent_score = 0, 0

# Ball

ball = pygame.Rect(0, 0, 20, 20)
ball.center = (WIDTH / 2, HEIGHT / 2)

x_speed, y_speed = 1, 1

game_over = False

while not game_over:
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
        if opponent.top > 0:
            opponent.top -= 2
    if keys_pressed[pygame.K_s]:
        if opponent.bottom < HEIGHT:
            opponent.bottom += 2

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
            player_score += 1
            if player_score >= 10:
                game_over = True
            else:
                ball.center = (WIDTH / 2, HEIGHT / 2)
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        if ball.x >= WIDTH:
            opponent_score += 1
            if opponent_score >= 10:
                game_over = True
            else:
                ball.center = (WIDTH / 2, HEIGHT / 2)
                x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        if player.x - ball.width <= ball.x <= player.right and ball.y in range(player.top - ball.width,
                                                                               player.bottom + ball.width):
            x_speed = -1
        if opponent.x - ball.width <= ball.x <= opponent.right and ball.y in range(opponent.top - ball.width,
                                                                                   opponent.bottom + ball.width):
            x_speed = 1

    player_score_text = FONT.render("Player: " + str(opponent_score), True, "white")
    opponent_score_text = FONT.render("Computer: " + str(player_score), True, "white")

    player_score_rect = player_score_text.get_rect(center=(WIDTH - 1000, 50))
    opponent_score_rect = opponent_score_text.get_rect(center=(WIDTH * 3 / 4, 50))

    if player.y < ball.y:
        player.top += 1
    if player.bottom > ball.y:
        player.bottom -= 1

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

    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)

    # Draw ball only if game is not over
    if not game_over:
        pygame.draw.circle(SCREEN, "white", ball.center, 10)

    SCREEN.blit(player_score_text, player_score_rect)
    SCREEN.blit(opponent_score_text, opponent_score_rect)

    pygame.display.update()
    CLOCK.tick(300)

# Display winner message
if player_score >= 10:
    winner_text = "Computer Wins!"
else:
    winner_text = "Player Wins!"

winner_text_render = FONT.render(winner_text, True, "white")
winner_text_rect = winner_text_render.get_rect(center=(WIDTH / 2, HEIGHT / 2))
SCREEN.blit(winner_text_render, winner_text_rect)
pygame.display.update()
pygame.time.delay(10000)  # Delay 3 seconds before quitting
import menu
