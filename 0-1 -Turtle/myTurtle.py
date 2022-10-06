import turtle 

Creatie = turtle.Turtle()

Creatie.speed(200)
Creatie.pencolor("#e733f1")

for i in range(180):
    Creatie.forward(70)
    Creatie.right(20)
    Creatie.forward(10)
    Creatie.left(190)
    Creatie.forward(50)
    Creatie.right(30)
    
    Creatie.penup()
    Creatie.setposition(0, 0)
    Creatie.pendown()
    
    Creatie.right(2)
    
turtle.done()