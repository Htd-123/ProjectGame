import pygame
import socket
import pickle

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong - Player Online")

# Các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Các font chữ
font = pygame.font.Font(None, 36)

# Hàm hiển thị màn hình chơi
def show_game(player_paddle, opponent_paddle, player_score, opponent_score):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    player_text = font.render("Player: " + str(player_score), True, WHITE)
    opponent_text = font.render("Opponent: " + str(opponent_score), True, WHITE)
    screen.blit(player_text, (50, 20))
    screen.blit(opponent_text, (SCREEN_WIDTH - 250, 20))
    pygame.display.flip()

# Kết nối đến server
server_address = '127.0.0.1'  # Địa chỉ IP của server
server_port = 12345  # Cổng của server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

# Biến đánh dấu chế độ chơi
player_score = 0
opponent_score = 0
paddle_width = 10
paddle_height = 100
player_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(SCREEN_WIDTH - 50 - paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

# Hàm gửi dữ liệu đến server
def send_data(data):
    try:
        client_socket.send(pickle.dumps(data))
    except pickle.PicklingError:
        print("Error while pickling data.")

# Hàm nhận dữ liệu từ server
def receive_data():
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        try:
            received_data = pickle.loads(data)
            opponent_paddle.y = received_data.y
            show_game(player_paddle, opponent_paddle, player_score, opponent_score)
        except pickle.UnpicklingError:
            print("Error while unpickling data.")

# Bắt đầu nhận dữ liệu từ server
receive_data()

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

    send_data(player_paddle)  # Gửi vị trí của thanh chắn người chơi đến server

    show_game(player_paddle, opponent_paddle, player_score, opponent_score)

# Đóng kết nối
client_socket.close()

# Kết thúc Pygame
pygame.quit()
