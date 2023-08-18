from turtle import Screen
from paddle import Paddle
from ball import Ball
from dotted_line import DottedLine
from score import Score
import time

# Constants
PADDLE_RIGHT_INIT_POS_X = 350
PADDLE_LEFT_INIT_POS_X = -350
PLAYER_1_SCORE_DISTANCE_FROM_CENTER = -50
PLAYER_2_SCORE_DISTANCE_FROM_CENTER = 50

# Screen Init
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

# Line init
dotted_line = DottedLine()
dotted_line.create_line()

# Paddle Init
paddle_right = Paddle()
paddle_left = Paddle()


# Ball Init
ball = Ball()

# Score init
player_1_score = Score()
player_2_score = Score()
screen.listen()


def game():
    player_1_score.refresh_score(PLAYER_1_SCORE_DISTANCE_FROM_CENTER, 'right')
    player_2_score.refresh_score(PLAYER_2_SCORE_DISTANCE_FROM_CENTER, 'left')
    paddle_right.paddle_init(PADDLE_RIGHT_INIT_POS_X)
    paddle_left.paddle_init(PADDLE_LEFT_INIT_POS_X)
    new_round()


def new_round():
    round_is_on = True
    paddle_right.goto(PADDLE_RIGHT_INIT_POS_X, 0)
    paddle_left.goto(PADDLE_LEFT_INIT_POS_X, 0)
    ball.ball_init()
    time.sleep(2)
    while round_is_on:
        time.sleep(0.1)
        screen.onkey(paddle_left.move_paddle_up, 'w')
        screen.onkey(paddle_right.move_paddle_up, 'Up')
        screen.onkey(paddle_left.move_paddle_down, 's')
        screen.onkey(paddle_right.move_paddle_down, 'Down')
        # print(ball.position())
        if ball.distance(paddle_left) < 55:
            ball.bounce_off_paddle('left')
        if ball.distance(paddle_right) < 55:
            ball.bounce_off_paddle('right')
        if ball.has_hit_wall():
            ball.bounce_off_wall()
        if ball.has_ball_been_scored():
            round_is_on = False
            if ball.has_ball_been_scored_player_one():
                player_1_score.score += 1
                player_1_score.refresh_score(PLAYER_1_SCORE_DISTANCE_FROM_CENTER, 'left')
            if ball.has_ball_been_scored_player_two():
                player_2_score.score += 1
                player_2_score.refresh_score(PLAYER_2_SCORE_DISTANCE_FROM_CENTER, 'right')
        ball.move()
    if player_1_score.score != 7 and player_2_score.score != 7:
        new_round()


game()
screen.exitonclick()
