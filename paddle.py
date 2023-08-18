from turtle import Turtle
MOVEMENT_INCREMENT = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        self.color('white')
        self.shapesize(0.5, 4)
        self.penup()
        self.speed('fastest')

    def paddle_init(self, pos_x):
        self.right(90)
        self.goto(pos_x, 0)
        self.showturtle()
    def move_paddle_up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + MOVEMENT_INCREMENT)
    def move_paddle_down(self):
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - MOVEMENT_INCREMENT)

