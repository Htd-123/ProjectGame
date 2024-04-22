import pygame
import sys
import subprocess

# Khởi tạo Pygame
pygame.init()

# Các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cài đặt cửa sổ
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Home")

# Tạo font
font = pygame.font.SysFont("Consolas", 50)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    while True:
        screen.fill(BLACK)
        # Tính toán tọa độ để vẽ tiêu đề ở giữa màn hình
        draw_text("Main Menu", font, WHITE, screen, WIDTH // 2, HEIGHT // 4)

        # Tính toán tọa độ để vẽ nút Play ở giữa màn hình
        play1_button_x = WIDTH // 2
        play1_button_y = HEIGHT // 2 - 50
        pygame.draw.rect(screen, WHITE, (play1_button_x - 150, play1_button_y - 25, 300, 50))
        draw_text("PVP", font, BLACK, screen, play1_button_x, play1_button_y)

        # Tính toán tọa độ để vẽ nút Play ở giữa màn hình
        play2_button_x = WIDTH // 2
        play2_button_y = HEIGHT // 2 + 50
        pygame.draw.rect(screen, WHITE, (play2_button_x - 150, play2_button_y - 25, 300, 50))
        draw_text("PVC", font, BLACK, screen, play2_button_x, play2_button_y)

        # Tính toán tọa độ để vẽ nút Caro Online ở giữa màn hình
        caro_button_x = WIDTH // 2
        caro_button_y = HEIGHT // 2 + 150
        pygame.draw.rect(screen, WHITE, (caro_button_x - 150, caro_button_y - 25, 300, 50))
        draw_text("CARO ONLINE", font, BLACK, screen, caro_button_x, caro_button_y)

        # Tính toán tọa độ để vẽ nút Quit ở giữa màn hình
        quit_button_x = WIDTH // 2
        quit_button_y = HEIGHT // 2 + 250
        pygame.draw.rect(screen, WHITE, (quit_button_x - 150, quit_button_y - 25, 300, 50))
        draw_text("QUIT", font, BLACK, screen, quit_button_x, quit_button_y)

        # Cập nhật màn hình
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play1_button_x - 150 <= mouse_x <= play1_button_x + 150:
                    if play1_button_y - 25 <= mouse_y <= play1_button_y + 25:
                        # Xử lý khi nhấn Play PVP
                        subprocess.Popen(["python", "test1.py"])
                    elif play2_button_y - 25 <= mouse_y <= play2_button_y + 25:
                        # Xử lý khi nhấn Play PVC
                        subprocess.Popen(["python", "test2.py"])
                    elif caro_button_y - 25 <= mouse_y <= caro_button_y + 25:
                        # Xử lý khi nhấn Play Caro Online
                        subprocess.Popen(["python", "caro.py"])
                    elif quit_button_y - 25 <= mouse_y <= quit_button_y + 25:
                        # Xử lý khi nhấn Quit
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main_menu()
