import socket
import errno
import sys
import turtle

t1 = turtle.Turtle()
t1.penup()
t1.goto(-350, 0)
t1.shape('square')
t1.color('blue')
t1.speed(0)
t1.shapesize(stretch_wid=4, stretch_len=1)

screen = turtle.Screen()
screen.setup(800, 800)
message = ""
screen.bgcolor('black')

my_username = screen.textinput('Name', 'Enter your name')

tt = turtle.Turtle()
tt.ht()
tt.color('brown')
tt.speed(0)
tt.goto(0, 400)
tt.goto(0, -400)

t2 = turtle.Turtle()
t2.penup()
t2.speed(0)
t2.goto(350, 0)
t2.shape('square')
t2.color('red')
t2.shapesize(stretch_wid=4, stretch_len=1)

t3 = turtle.Turtle()
t3.shape('circle')
t3.color('white')
t3.penup()
t3.direction = 1.5
t3.isUp = 1

scoreA = turtle.Turtle()
scoreA.score = 0
scoreA.penup()
scoreA.ht()
scoreA.goto(-150, 350)
scoreA.speed(0)

scoreB = turtle.Turtle()
scoreB.score = 0
scoreB.speed(0)
scoreB.penup()
scoreB.ht()
scoreB.goto(150, 350)
scoreB.color('White')
scoreA.color('White')
scoreA.write(scoreA.score, font=("Arial", 18, "normal"))
scoreB.write(scoreB.score, font=("Arial", 18, "normal"))


def handleUp():
    global message
    t1.goto(-350, t1.ycor() + 20)
    message = 'Up'


def handleUp2():
    global message
    t1.goto(-350, t1.ycor() - 20)
    message = 'Down'


def move_t2_up():
    t2.goto(350, t2.ycor() + 20)


def move_t2_down():
    t2.goto(350, t2.ycor() - 20)


move_ball1 = False
move_ball2 = False


def setBall():
    global move_ball2, message
    move_ball2 = True
    message = 'Enter'


turtle.listen()

turtle.onkey(handleUp, 'Up')
turtle.onkey(handleUp2, 'Down')
turtle.onkey(setBall, 'Return')

header_length = 20
ip = '192.168.1.6'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{header_length}}".encode('utf-8')
client_socket.send(username_header + username)


def moveball():
    global message, move_ball1, move_ball2
    if not move_ball1 and not move_ball2:
        return
    if t3.xcor() > 370 or t3.xcor() < -370:
        if t3.xcor() > 370:
            scoreA.score += 1
            scoreA.clear()
            scoreA.write(str(scoreA.score), font=("Arial", 18, "normal"))

        if t3.xcor() < -370:
            scoreB.score += 1
            scoreB.clear()
            scoreB.write(str(scoreB.score), font=("Arial", 18, "normal"))

        if scoreA.score == 10:
            screen.clear()
            message1 = 'WinA'
            message1 = message1.encode('utf-8')
            message1_header = f'{len(message1) :< {header_length}}'.encode('utf-8')
            client_socket.send(message1_header + message1)
            import win

        if scoreB.score == 10:
            screen.clear()
            message1 = 'WinB'
            message1 = message1.encode('utf-8')
            message1_header = f'{len(message1) :< {header_length}}'.encode('utf-8')
            client_socket.send(message1_header + message1)
            import lost

        t3.ht()
        t3.goto(0, 0)
        t3.showturtle()
        move_ball1 = False
        move_ball2 = False

    if t3.ycor() > 370 or t3.ycor() < -370:
        t3.isUp = -t3.isUp

    if t1.ycor() + 40 > t3.ycor() > t1.ycor() - 40 and -340 > t3.xcor() > -350:
        t3.direction = -t3.direction

    if t2.ycor() + 40 > t3.ycor() > t2.ycor() - 40 and 340 < t3.xcor() < 350:
        t3.direction = -t3.direction

    t3.goto(t3.xcor() + 7.0 * t3.direction, t3.ycor() + 0.8 * t3.isUp)


while True:
    message = ""
    moveball()

    screen.update()
    if message:
        message = message.encode('utf-8')
        message_header = f'{len(message) :< {header_length}}'.encode('utf-8')
        client_socket.send(message_header + message)
    try:
        while True:
            username_header = client_socket.recv(header_length)
            if not len(username_header):
                print('Connection closed by server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(header_length)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            print(f'{username} > {message}')

            if message == 'Enter':
                move_ball1 = True

            if message == 'Up':
                move_t2_up()
            if message == 'Down':
                move_t2_down()
            # message = ""
            screen.update()

    except IOError as ioe:
        if ioe.errno != errno.EAGAIN and ioe.errno != errno.EWOULDBLOCK:
            print('Reading error', str(ioe))
            sys.exit()
        continue

    except Exception as e:
        print(('General error', str(e)))
        pass
    screen.update()
