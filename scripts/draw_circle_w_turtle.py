from turtle import *
from tkinter import *
import math

noselection = 0
circle = 1

# The Circle class is omitted here.

class DrawApp:

    def __init__(self):
        root = Tk()
        root.title("Draw!")
        self.shapeSelection = noselection
        cv = ScrolledCanvas(root ,600 ,600 ,600 ,600)
        cv.pack(side = LEFT)
        aTurtle = RawTurtle(cv)
        screen = aTurtle.getscreen ()
        aTurtle.ht()
        screen.tracer (0)

    #   bar = tkinter.Menu (root)
    #    fileMenu = tkinter.Menu (bar, tearoff = 0)
    #    fileMenu.add_command (label = "Exit", command = Exit)
    #    bar.add_cascade (label = "Help", menu = fileMenu)
    #    root.config(menu=bar)
        
        fram = Frame(root)
        fram.pack(side = RIGHT ,fill=BOTH)

        def circCommand ():
            print ("in circCommand")
            self.shapeSelection = circle

        radiusEnt = StringVar ()
        radiusLabel = Label(fram ,text="Radius:")
        radiusLabel.grid(row=2,column =1,sticky=E)
        radiusEntry = Entry(fram ,textvariable=radiusEnt)
        radiusEntry.grid(row=2,column =2,sticky=E+W)
        circleButton = Button(fram , text = "Circle", \
                              command=circCommand)
        circleButton.grid(row=1, column =1, columnspan =2)

        def clickHandler(x,y):
            print ("In clickHandler")
            if self.shapeSelection == circle:
                print ("shape selection was circle")
                radius = radiusEnt.get()
                if radius.strip () == "":
                    radius = 50
                else :
                    radius = float (radius)
                shape = Circle(x,y,radius ,edgeWidth =3, \
                               color="red",outline="gray")
                shape.draw(aTurtle)
                screen.update ()
        screen.onclick(clickHandler)

class Shape:
    def __init__(self ,x=0,y=0,color="transparent", \
                 outline="black",width =1):
        self.x = x
        self.y = y
        self.color = color
        self.outline = outline
        self.width = width
      
    def setWidth(self ,width ):
        self.width = width

    def setFill(self ,color ):
        self.color = color

    def setOutline(self ,color ):
        self.outline = color
    
    def getX(self ):
        return self.x

    def getY(self ):
        return self.y

class Circle(Shape ):
    def __init__(self ,x=0,y=0,radius =50, color="transparent", \
                 outline="black",width =1):
        super ().__init__(x,y,color ,outline ,width)
        self.radius = radius
 
    def draw(self ,turtle ):
        Shape.draw(self ,turtle)
        turtle.penup ()
        turtle.goto(self.x,self.y)
        turtle.width(self.width)
        if self.color != "transparent":
            turtle.fillcolor(self.color)
        turtle.color(self.outline)
        turtle.fillcolor(self.color)
        turtle.setheading (0)
        turtle.forward(self.radius)
        if self.color != "transparent":
            turtle.begin_fill ()
        turtle.pendown ()
        for k in range (500):
            radians = (2* math.pi)*(k/500.0)
            turtle.goto(math.cos(radians )* self.radius+self.x, \
                        math.sin(radians )* self.radius+self.y)
        if self.color != "transparent":
            turtle.end_fill ()
        turtle.penup ()
        turtle.goto(self.x,self.y)

    def getRadius(self ):
        return self.radius


def main ():
    app = DrawApp ()
    mainloop ()

if __name__ == "__main__":
    main ()
