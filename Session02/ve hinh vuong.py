from turtle import *

shape("turtle")
speed(0)
color("red")

for i in range(20):
    for j in range(4):
        forward(i*8)
        left(90)
    left(10)
    forward(10)

mainloop()