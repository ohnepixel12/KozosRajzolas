import turtle

a=0
turtle.penup()
turtle.setposition(0, -100)
turtle.fillcolor("brown")
turtle.pencolor("brown")

while a<2:            #Bogdán a  fa törzs
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.end_fill()
    a+=1

turtle.penup()

#Maria, fa lombkorona megrajzolasa
turtle.setposition(20, 70)
turtle.pendown()
turtle.fillcolor("green")
turtle.pencolor("green")
turtle.setheading(-90)
i = 0
while i < 3:
    turtle.begin_fill()
    turtle.circle(60)
    turtle.left(90)
    turtle.end_fill()
    i += 1

turtle.done()


