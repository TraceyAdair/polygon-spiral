#polygon spirals
#by Tracey Adair
#2/25/24

#print ("Hello World!")

import turtle
turtle.color("teal")

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()
    
def move(len):
    turtle.penup()
    turtle.forward(len)
    turtle.pendown()

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360/num)
    
def spiral (len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
  
spiral(75, 45)
move(150)
turtle.color("yellow")
spiral(125, 90)
    
#def square(size):
  #for i in range(4):
    #turtle.forward(size)
    #turtle.left(90)


#for n in range(3, 10):
  #move(20)
  #polygon(n, 100/n)
  #back(50)
  #turtle.right(360/7)
