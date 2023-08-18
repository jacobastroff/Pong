from turtle import Turtle
SCORE_POS_Y = 240
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.penup()
    def refresh_score(self, pos_x, alignment):
        self.clear()
        self.goto(pos_x, SCORE_POS_Y)
        self.write(f'{self.score}', False, alignment, ('Courier', 48, 'bold'))


