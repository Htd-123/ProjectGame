import pygame

def show_menu(screen):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    screen.fill(BLACK)
    text1 = font.render("1 Player vs Player", True, WHITE)
    text2 = font.render("2 Player vs Computer", True, WHITE)
    screen.blit(text1, (400 - text1.get_width() // 2, 200))
    screen.blit(text2, (400 - text2.get_width() // 2, 300))
    pygame.display.flip()

def main():
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ping Pong Game")

    show_menu(screen)

    mode = None
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "PVP"
                    menu_running = False
                elif event.key == pygame.K_2:
                    mode = "PVC"
                    menu_running = False

    pygame.quit()

    if mode:
        if mode == "PVP":
            import player_vs_player
            player_vs_player.main()
        elif mode == "PVC":
            import pong_computer
            pong_computer.main(mode)

if __name__ == "__main__":
    main()
