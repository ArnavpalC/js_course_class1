import turtle

screen = turtle.Screen()
screen.setup(width=600, height=400)
t = turtle.Turtle()
t.speed(2) 

t.penup()
t.goto(-200, -50) 
t.pendown()

t.fillcolor("blue")
t.begin_fill() 
for _ in range(3):
    t.forward(100)
    t.left(120) 
t.end_fill() 


t.penup()
t.goto(-50, -50) 
t.pendown()

for _ in range(4):
    t.forward(100)
    t.left(90) 


t.penup()
t.goto(100, -50) 
t.pendown()

for _ in range(6):
    t.forward(100)
    t.left(60) 

t.hideturtle() 
screen.exitonclick() 
