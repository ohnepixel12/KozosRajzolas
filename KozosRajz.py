import turtle

i=0
turtle.penup()
turtle.setposition(0, -100)
turtle.fillcolor("brown")
turtle.pencolor("brown")

while i<2:
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill()
    i+=1

turtle.done()
