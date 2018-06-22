from turtle import * 
canh = int(input("so canh cua da giac deu"))

speed(0)
shape("turtle")
color("green")

for i in range(canh):
    forward(100)
    left(360 / canh)

mainloop()