import turtle
import random
wn=turtle.Screen()
wn.bgcolor("green")
wn.tracer(0)
wn.setup(width=500, height=600)

GRAVITY=-0.004
bird=turtle.Turtle()
bird.shape("square")
bird.color("white")
bird.penup()
bird.goto(-200, 0)
bird.dy=-0.0001
#hello

pipe_u=turtle.Turtle()
pipe_u.shape("square")
pipe_u.color("red")
pipe_u.penup()
pipe_u.goto(200, random.randint(50, 500))
pipe_u.shapesize(stretch_wid=25, stretch_len=2)

pipe_l=turtle.Turtle()
pipe_l.shape("square")
pipe_l.color("red")
pipe_l.penup()
pipe_l.goto(200, (pipe_u.ycor()-600))
pipe_l.shapesize(stretch_wid=25, stretch_len=2)

pipe_speed=-0.9

game_over_pen=turtle.Turtle()
game_over_pen.hideturtle()
game_over_pen.color("white")
game_over_pen.penup()
game_over_pen.goto(0, 100)

pen=turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(180, 260)
pen.write(f"score: 0", align="center", font=("Calibri", 20))





def flap ():
    bird.dy=0.8

wn.listen()
wn.onkeypress(flap, "space")
game_over=False
score=0
while True:
    wn.update()
    

    bird.dy+=GRAVITY
    y=bird.ycor()
    y+=bird.dy
    bird.sety(y)



    x=pipe_u.xcor()
    x+=pipe_speed
    pipe_u.setx(x)
    pipe_l.setx(x)

    
    


    if (bird.ycor()<pipe_l.ycor()+250 and bird.xcor()>pipe_u.xcor()-20 and bird.xcor()<pipe_u.xcor()+20) or (bird.ycor()>pipe_u.ycor()-250 and bird.xcor()>pipe_u.xcor()-20 and bird.xcor()<pipe_u.xcor()+20)or (bird.ycor()<-330):
        game_over_pen.write(f"GAME OVER\nScore {score}", align="center", font=("Calibri", 20))
        game_over=True
        bird.goto(1000, 1000)
        pipe_u.goto(-1000, -1000)
        pipe_l.goto(-1000, -1000)
        pen.clear()
    


    if pipe_u.xcor()<-260 and game_over==False:
        pipe_u.goto(300, random.randint(50, 500))
        pipe_l.goto(300, (pipe_u.ycor()-600))
        score+=1
        pen.clear()
        pen.write(f"score: {score}", align="center", font=("Calibri", 20))
        
    
    
