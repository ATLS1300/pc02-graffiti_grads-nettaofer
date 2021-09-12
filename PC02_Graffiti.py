#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Netta Ofer
September 11, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.left(90)
turtle.setpos(-115, 115)
turtle.down()

turtle.circle(-12, 140) 
turtle.left(30)
turtle.forward(73)

print(turtle.pensize())

turtle.pensize(3)
turtle.circle(20, 470) 
turtle.pensize(1)
 
turtle.right(55)
turtle.forward(15)
turtle.right(70)
turtle.forward(22)

turtle.pensize(3)
turtle.circle(17, 480)
turtle.pensize(1)

turtle.right(14)
turtle.forward(32)
turtle.circle(-8, 170) 

print(turtle.pos())

turtle.up()
turtle.goto(65, -70)
turtle.right(180)
turtle.down()

turtle.begin_fill()
turtle.fillcolor(130, 80, 7)
turtle.fd(100)
turtle.left(90)
turtle.fd(5)
turtle.left(88)
turtle.fd(100)
turtle.goto(65, -70)
turtle.end_fill()

turtle.fillcolor(0,0,0)
turtle.up()
turtle.left(180)
turtle.setpos(-5, 170)
turtle.down()

turtle.fd(20)
turtle.left(125)
turtle.fd(20)
turtle.right(120)
turtle.fd(30)

turtle.up()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.

turtle.done()