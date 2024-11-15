#pong
from turtle import *
import time

screen = Screen()
screen.setup(height=600,width=900)
screen.bgcolor("black")
screen.tracer(0)

score_l_value = 0
score_r_value = 0

line = Turtle()
line.hideturtle()
line.pencolor("white")
line.pensize(4)
line.penup()
line.goto(0,280)
line.setheading(90)

score_r = Turtle()
score_r.hideturtle()
score_r.color("white")
score_r.penup()
score_r.goto(250,260)
score_r.write("SCORE : 0 " , align="left", font=("Arial", 16, "normal"))

score_l = Turtle()
score_l.hideturtle()
score_l.color("white")
score_l.penup()
score_l.goto(-350,260)
score_l.write("SCORE : 0", align="left", font=("Arial", 16, "normal"))

ball = Turtle()

ball.shape("circle")
ball.color("red")
ball.shapesize(1.5)
ball.penup()
ball.goto(0,0)
ball_dx = 20
ball_dy = 20


for i in range(10):
    line.pendown()
    line.backward(30)
    line.penup()
    line.backward(30)

left_paddle = None
right_paddle = None

def paddle(x):
    paddle = Turtle()
    paddle.color("white")
    paddle.shape("square")
    paddle.shapesize(1,5,5)
    paddle.penup()
    paddle.goto(x,-235)
    paddle.setheading(90)
    return paddle

def move_up_right():
    if right_paddle.ycor() < 260: 
        right_paddle.forward(55)

def move_down_right():
    if right_paddle.ycor() > -250:
        right_paddle.backward(55) 

def move_up_left():
    if left_paddle.ycor() < 260: 
        left_paddle.forward(55)

def move_down_left():
    if left_paddle.ycor() > -250:
        left_paddle.backward(55)      

def update_score_l():
    score_l.clear()
    score_l.write(f"Score: {score_l_value}", align="left", font=("Arial", 16, "normal"))

def update_score_r():
    score_r.clear()
    score_r.write(f"Score: {score_r_value}", align="right", font=("Arial", 16, "normal"))

left_paddle = paddle(-420) 
right_paddle = paddle(420)

screen.listen()
screen.onkey(move_up_right,"Up")
screen.onkey(move_down_right,"Down")
screen.onkey(move_up_left,"w")
screen.onkey(move_down_left,"s")

while True:
    screen.update()
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)    

    if ball.ycor() < -290 or ball.ycor() > 290:
        ball_dy *= -1

    if ball.distance(left_paddle) < 50:
        score_l_value += 1
        update_score_l()
        ball_dx *= -1  

    elif ball.distance(right_paddle) < 50:
        score_r_value += 1
        update_score_r()
        ball_dx *= -1    

    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.goto(0,0)
        ball_dx *= -1

        break  
         
    time.sleep(0.08)
    


