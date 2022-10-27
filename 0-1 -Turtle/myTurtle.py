import turtle 

Creatie = turtle.Turtle()

Creatie.speed(200)
Creatie.pencolor("#e733f1")

for i in range(60):
    Creatie.forward(170)
    Creatie.right(120)
    Creatie.forward(110)
    Creatie.left(190)
    Creatie.forward(150)
    Creatie.right(130)
    
    Creatie.penup()
    Creatie.setposition(0, 0)
    Creatie.pendown()
    
    Creatie.right(4)

Creatie.pencolor("#84f542")
for i in range(60):
    Creatie.forward(70)
    Creatie.right(20)
    Creatie.forward(10)
    Creatie.left(90)
    Creatie.forward(50)
    Creatie.right(30)
    
    Creatie.penup()
    Creatie.setposition(0, 0)
    Creatie.pendown()
    
    Creatie.right(4)

    
turtle.done()