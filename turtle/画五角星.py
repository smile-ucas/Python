from turtle import Turtle
p=Turtle()
p.speed(3)
p.pensize(5)
p.color("black","yellow")
p.begin_fill()
for i in range(5):
    #乌龟头部方向 向前走200
    p.forward(200)
    #向右转144度
    p.right(144) 
p.end_fill()
