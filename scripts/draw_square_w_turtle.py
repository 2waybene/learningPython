# Imports always go at the top
import turtle

 # Function definitions go second
def drawSquare(turtle , length ):
   for k in range (4):
      turtle.forward(length)
      turtle.left (90)

 # main function definition goes second to last.

def main():
   t = turtle.Turtle()
   screen = t.getscreen()
   l = int (input ("Please enter a side length:"))
   drawSquare(t,l)
   screen.exitonclick ()

 # the if statement that calls main goes last.
if __name__ == "__main__":
   main ()