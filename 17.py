import turtle
turtle.Screen().bgcolor("orange")
sc = turtle.Screen()
sc.setup(400,300)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1
for i in range(4):
    board.forward(100)
    board.right(90)
    i = i+1

