import turtle

a=0
turtle.penup()
turtle.setposition(0, -100)
turtle.fillcolor("brown")
turtle.pencolor("brown")

while a<2:
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill()
    a+=1

turtle.done()
