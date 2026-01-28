import turtle
t = turtle.Turtle()
t.speed(0)

colors = ['red', 'blue', 'green']

for i in range(3):
    t.color(colors[i])
    t.pensize(3)
    t.circle(50)
    t.right(120)

t.penup()
t.goto(-35, 60) 
t.pendown()
t.color('blue')
t.pensize(3)
t.begin_fill()
for _ in range(4):
    t.forward(70)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0, -25)
t.pendown()
t.color('orange')
t.begin_fill()
t.circle(25)
t.end_fill()

t.hideturtle()
turtle.done()
