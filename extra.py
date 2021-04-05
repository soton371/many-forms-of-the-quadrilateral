import turtle
import math


class quadrilateral:
    dimension = 1

    if dimension < 0:
        print('Required dimension greater than zero for quadrilateral.')
    else:
        window = turtle.Screen()
        class Parallelogram():            
            turtle.penup()  
            turtle.goto(-300, 100) 
            turtle.color("black","red")
            turtle.pendown()
            turtle.begin_fill()    
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.left(120)
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(60)
            turtle.end_fill()                              
            

            def Area(self):
                pA = 100*60
                print("\nArea of Parallelogram = ",pA)
            def Perimeter(self):
                pP = 2*100+2*60
                print("Perimeter of Parallelogram = ",pP)

        class Square(): 
            turtle.penup() 
            turtle.goto(-180, 100)
            turtle.color("black","magenta")
            turtle.pendown()
            turtle.begin_fill()           
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.end_fill()          

            def Area(self):
                sA = 100*100
                print("\nArea of Square = ",sA)
            def Perimeter(self):
                sP = 4*100
                print("Perimeter of Square = ",sP)

        class Rectangle(): 
            turtle.penup() 
            turtle.goto(-20, 100)
            turtle.color("black","orange")
            turtle.pendown()
            turtle.begin_fill()           
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(70)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(70)
            turtle.end_fill()                                         

            def Area(self):
                rA = 100*70
                print("\nArea of Rectangle = ",rA)
            def Perimeter(self):
                rP = 2*(100+70)
                print("Perimeter of Rectangle = ",rP)

        class Rhombus(): 
            turtle.penup() 
            turtle.goto(0, 100)
            turtle.color("black","blue")
            turtle.pendown()
            turtle.begin_fill()           
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(100)
            turtle.left(120)
            turtle.forward(100)
            turtle.left(60)
            turtle.forward(100)
            turtle.end_fill()                              

            def Area(self):
                rhA = 100**2 * math.sin(math.radians(60))
                print("\nArea of Rhombus = ",rhA)
            def Perimeter(self):
                rhP = 4*100
                print("Perimeter of Rhombus = ",rhP)

        class Trapezoid(): 
            turtle.penup() 
            turtle.goto(20, 100)
            turtle.color("black","green")
            turtle.pendown()
            turtle.begin_fill()           
            turtle.forward(250)
            turtle.left(125)
            turtle.forward(100)
            turtle.left(55)
            turtle.forward(155)
            turtle.left(65)
            turtle.forward(90)
            turtle.end_fill()
            turtle.done()                               

            def Area(self):
                tA = (250+155)*155/2
                print("\nArea of Trapezoid = ",tA)
            def Perimeter(self):
                tP = 250+100+155+90
                print("Perimeter of Trapezoid = ",tP)
    
    px = Parallelogram()
    px.Area()
    px.Perimeter()
    
    sx = Square()
    sx.Area()
    sx.Perimeter()

    rx = Rectangle()
    rx.Area()
    rx.Perimeter()

    rhx = Rhombus()
    rhx.Area()
    rhx.Perimeter()

    tx = Trapezoid()
    tx.Area()
    tx.Perimeter()




