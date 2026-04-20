from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)              #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#drawing a roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a windows

penup()
goto(20,180)
pendown()

color("blue")
begin_fill()
left(30) 
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180,180)
pendown()

begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

color("lightblue")
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
left(90)
forward(40)
left(180)
forward(20)
right(90)
forward(20)

penup()
goto(20,180)
pendown()

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
left(180)
forward(20)
right(90)
forward(20)
left(180)
forward(40)

#end of windows

#end of painting house



exitonclick()