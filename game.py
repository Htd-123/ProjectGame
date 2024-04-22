import pygame
import socket
import pickle

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

# Kết nối đến server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

# Hàm gửi dữ liệu đến server
def send_data(data):
    try:
        client_socket.send(pickle.dumps(data))
    except pickle.PicklingError:
        print("Error while pickling data.")

# Gửi dữ liệu mẫu đến server
sample_data = {"message": "Hello from client"}
send_data(sample_data)

# Hàm nhận dữ liệu từ server
def receive_data():
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        try:
            received_data = pickle.loads(data)
            print("Received:", received_data)
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

    show_game()

# Đóng kết nối
client_socket.close()

# Kết thúc Pygame
pygame.quit()
