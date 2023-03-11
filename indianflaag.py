import turtle
flag = turtle.Turtle()
flag.speed(5)
flag.pensize(5)
flag.color('#054187')

def draw(x,y):
    flag.penup()
    flag.goto(x,y)
    flag.pendown()

for i in range(24):
    flag.forward(88)
    flag.backward(88)
    flag.left(15)
draw(0, -88)

flag.circle(88, 360)

#green rectangle
flag.color('green')
flag.begin_fill()

flag.forward(350)
flag.backward(700)
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)

flag.end_fill()

#orange rectangle
flag.color('orange')
draw(-350,90)

flag.begin_fill()

flag.right(180)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)

flag.end_fill()

turtle.done()