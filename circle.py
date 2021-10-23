import turtle
import math

def drawCircle(t, x, y, radius):


   t.up()
   t.goto(x + radius, y)
   t.setheading(90)
   t.down()
   for i in range(0, 120):
       t.left(3)
       t.forward(2.0 * math.pi * radius / 120) 

def main():
   x = 50
   y = 75
   radius = 100

   t = turtle.Turtle()

   drawCircle(t, x, y, radius)

if __name__ == '__main__':
   main()
   turtle.mainloop()
