from turtle import Turtle
import random
SPEED = 2
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()

        self.speed(SPEED)
        self.last_hit_position = [0, 0]
        self.last_hit_position_hit_count = [0, 0]
    def ball_init(self):
        self.speed('fastest')
        self.goto(0,0)
        self.speed('slowest')
        self.angle_x_increment = random.randint(20, 90)
        self.angle_y_increment = random.randint(20, 90)
    def move(self):
        self.goto(self.xcor() + self.angle_x_increment, self.ycor() + self.angle_y_increment)
    def has_hit_wall(self):
        return self.ycor() > 250 or self.ycor() < -250
    def bounce_off_wall(self):
        self.angle_y_increment *= -1
        self.move()
        print('ball has bounced')
    def bounce_off_paddle(self, left_or_right):
        self.angle_x_increment = random.randint(20, 90) * (-1 if left_or_right == 'right' else 1)
        self.angle_y_increment = random.randint(20, 90) * (-1 if left_or_right == 'right' else 1)
        self.speed(SPEED)
        self.move()

    def has_ball_been_scored(self):
        return self.xcor() > 380 or self.xcor() < -380
    def has_ball_been_scored_player_one(self):
        return self.xcor() > 380
    def has_ball_been_scored_player_two(self):
        return self.xcor() < -380

