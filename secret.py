import turtle
import math

screen = turtle.Screen()
screen.setup(700, 650)
screen.bgcolor('#100810')
screen.title('For Kriti')
screen.tracer(0)
pen = turtle.Turtle(visible=False)
pen.pensize(3)
pen.color('#ff7799', '#e91e46')
text = turtle.Turtle(visible=False)
text.color('white')
text.penup()

def point(i, scale=1):
    t = math.radians(i)
    return (15 * scale * 16 * math.sin(t)**3,
            15 * scale * (13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)))

def draw_heart(scale=1):
    pen.clear()
    pen.penup()
    pen.goto(point(0, scale))
    pen.pendown()
    pen.begin_fill()
    for i in range(1, 361):
        pen.goto(point(i, scale))
    pen.end_fill()

def write_message(count, name=False):
    text.clear()
    text.goto(0, 5)
    text.write('LOVE YOU'[:count], align='center', font=('Arial', 32, 'bold'))
    if name:
        text.goto(0, -40)
        text.write('KRITI', align='center', font=('Arial', 24, 'bold'))

def pulse(frame=0):
    scale = 1 + 0.045 * (1 + math.sin(frame * 0.22))
    draw_heart(scale)
    write_message(8, True)
    screen.update()
    screen.ontimer(lambda: pulse(frame + 1), 45)

def reveal(count=1):
    write_message(count)
    screen.update()
    if count < 8:
        screen.ontimer(lambda: reveal(count + 1), 120)
    else:
        screen.ontimer(pulse, 450)

def outline(i=0):
    if i == 0:
        pen.penup()
        pen.goto(point(0))
        pen.pendown()
    pen.goto(point(i))
    screen.update()
    if i < 360:
        screen.ontimer(lambda: outline(i + 3), 20)
    else:
        draw_heart()
        screen.update()
        screen.ontimer(reveal, 400)

outline()
turtle.done()
