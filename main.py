# Names: Brianna Barrentine     Date Assigned: 10/18/2018
#        Cameron Broome
#
# Course: CSE 1284 Sec 12      Date Due:10/18/2018
#
# File name: CSELab#6
#
# Program Description: The following program uses user input to create shapes using turtle

#allows the code to interpret functions from turtly
import turtle

#creates seperate sprites for each shape/drawing
turtCircle = turtle.Turtle()
turtRectangle = turtle.Turtle()
turtLine = turtle.Turtle()
turtPoint = turtle.Turtle()
turtTriangle = turtle.Turtle()

#the drawCircle function creates a maroon circle based on the starting points and radius provided by the user
def drawCircle(x,y,radius):
  turtCircle.color("maroon")
  turtCircle.penup()
  turtCircle.setposition(x,y)
  turtCircle.pendown()
  turtCircle.circle(radius)

#the drawRectangle function creates a gray rectangle based on the starting point, width, and height provided by the user
def drawRectangle(x,y,width,height):
  a = int(y + height)
  b = int(x + width)
  turtRectangle.color("gray")
  turtRectangle.penup()
  turtRectangle.setposition(x, y)
  turtRectangle.pendown()
  turtRectangle.goto(x,a)
  turtRectangle.pendown()
  turtRectangle.goto(b,a)
  turtRectangle.pendown()
  turtRectangle.goto(b,y)
  turtRectangle.pendown()
  turtRectangle.goto(x,y)
  turtRectangle.pendown()

#the drawPoint function creates a blue point based on the given coordinates  
def drawPoint(x,y,size):
  turtPoint.color("blue")
  turtPoint.pensize(size)
  turtPoint.penup()
  turtPoint.goto(x,y)
  turtPoint.dot()
  turtPoint.pendown()

#the drawLine function creates a green line based on the starting points and given end points 
def drawLine(x,y,x2,y2):
  turtLine.color("green")
  turtLine.penup()
  turtLine.setposition(x,y)
  turtLine.pendown()
  turtLine.goto(x2,y2)
  turtLine.pendown()

#the drawTriangle function creates a purple right triangle
def drawTriangle(x,y,side):
  z = int(x + side)
  w = int(y + side)
  turtTriangle.color("purple")
  turtTriangle.penup()
  turtTriangle.setposition(x,y)
  turtTriangle.pendown()
  turtTriangle.goto(z,y)
  turtTriangle.pendown()
  turtTriangle.goto(x,w)
  turtTriangle.pendown()
  turtTriangle.goto(x,y)
  turtTriangle.pendown()

#the main() function runs all the user code as well as draws all the shapes
def main():
  x = int(input("Enter the x coordinate of the starting poisition:"))
  y = int(input("Enter the y coordinate of the starting poisition:"))
  radius = int(input("Enter the radius of the circle:"))
  height = int(input("Enter the height of the rectangle:"))
  width = int(input ("Enter the width of the rectangle:"))
  size = int(input("Enter the size of the point:"))
  x2 = int(input("Enter the x coordinate of the ending point for the line:"))
  y2 = int(input("Enter the y coordinate of the ending point for the line:"))
  side = int(input("Enter the side length of the triangle:"))
  drawCircle(x,y,radius)
  drawRectangle(x,y,width,height)
  drawPoint(x,y,size)
  drawLine(x,y,x2,y2)
  drawTriangle(x,y,side)

#runs the code
main()