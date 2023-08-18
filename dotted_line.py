from turtle import Turtle
LINE_DISTANCE = 20
class DottedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.width(3)
        self.penup()
        self.goto(0, -310)
        self.left(90)
    def create_line(self):
        while self.ycor() < 310:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.showturtle()
        # OR
        # self.pendown()
        # self.goto(0, 310)
