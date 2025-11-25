import turtle
b = turtle.Turtle()
s=turtle.Screen()
col= ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
s.bgcolor('black')
b.speed('fastest')
b.hideturtle()

while True:
    for x in range(200):
        b.pencolor(col[x%len(col)])
        b.width(x/100 +1)
        b.forward(x)
        b.left(59)
    b.right(239)

    for x in range(200, 0, -1):
        b.pencolor('black')
        b.width(x/100 + 7)
        b.forward(x)
        b.right(59)
