import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("integral_alıcı")

tosbaga = turtle.Turtle()  # kaplumbağa oluşturduk
tosbaga.color("white")
tosbaga.pensize(2)
tosbaga.speed(2)

def direnc():
    tosbaga.forward(10)
    tosbaga.left(60)
    tosbaga.forward(5)
    tosbaga.right(130)
    for i in range(2):
        tosbaga.forward(10)
        tosbaga.left(140)
        tosbaga.forward(10)
        tosbaga.right(140)
    tosbaga.forward(10)
    tosbaga.left(140)
    tosbaga.forward(5)
    tosbaga.right(70)
    tosbaga.forward(10)

def opamp():
    tosbaga.forward(20)
    tosbaga.left(90)
    tosbaga.forward(20)
    for i in range(2):
        tosbaga.right(120)
        tosbaga.forward(60)
    tosbaga.right(120)
    tosbaga.forward(40)
    tosbaga.backward(20)

def gnd():
    tosbaga.left(90)
    tosbaga.forward(20)
    tosbaga.left(90)
    tosbaga.forward(40)
    tosbaga.right(90)
    tosbaga.forward(10)
    tosbaga.backward(20)
    tosbaga.forward(10)

    tosbaga.penup()
    tosbaga.left(90)
    tosbaga.forward(5)
    tosbaga.position()
    tosbaga.right(90)
    tosbaga.forward(5)
    tosbaga.pendown()
    tosbaga.backward(10)

    tosbaga.penup()
    tosbaga.left(90)
    tosbaga.forward(5)
    tosbaga.position()
    tosbaga.right(90)
    tosbaga.forward(2.5)
    tosbaga.pendown()
    tosbaga.forward(5)

def geribes1():
    tosbaga.penup()
    tosbaga.setposition(-256, 120)
    tosbaga.right(180)
    direnc()
    tosbaga.pendown()
    tosbaga.left(90)
    tosbaga.forward(60)
    tosbaga.right(90)
    tosbaga.forward(40)
    tosbaga.left(90)
    tosbaga.forward(10)
    tosbaga.backward(20)
    tosbaga.forward(10)

    tosbaga.penup()
    tosbaga.position()
    tosbaga.right(90)
    tosbaga.forward(10)
    tosbaga.pendown()
    tosbaga.left(90)
    tosbaga.forward(10)
    tosbaga.backward(20)
    tosbaga.forward(10)
    tosbaga.right(90)
    tosbaga.forward(40)
    tosbaga.right(90)
    tosbaga.forward(70)
    tosbaga.right(90)
    tosbaga.forward(20)
    tosbaga.backward(60)
    tosbaga.right(180)
    print(tosbaga.position())
def geribes2():
    tosbaga.penup()
    tosbaga.setposition(-214.69, 119.63)
    tosbaga.pendown()
    tosbaga.right(90)
    tosbaga.forward(50)
    tosbaga.right(90)
    tosbaga.forward(50)
    direnc()
    tosbaga.forward(50)
    tosbaga.right(90)
    tosbaga.forward(60)
    tosbaga.right(90)
    tosbaga.forward(30)
    tosbaga.backward(80)
    tosbaga.right(180)

def integral_alan(tosbaga):
    tosbaga.penup()
    tosbaga.setposition(-256, 120)
    tosbaga.pendown()
    direnc()
    opamp()
    gnd()
    geribes1()

    tosbaga.penup()
    tosbaga.setposition(-190.69, 110.63)
    tosbaga.pendown
    tosbaga.write("+", font=("arial",14,"bold"))
    tosbaga.penup()
    tosbaga.setposition(-187.69, 90.63)
    tosbaga.pendown
    tosbaga.write("-", font=("arial", 14, "bold"))
    tosbaga.penup()
    tosbaga.setposition(-84.69,109.63)
    tosbaga.pendown

#integral_alan(tosbaga)

size = 2
def toplayici(tosbaga):
    tosbaga.penup()
    tosbaga.setposition(-256, 120)
    tosbaga.pendown()
    direnc()

    knm = 70
    for i in range(size):
        tosbaga.penup()
        tosbaga.setx(-256)
        tosbaga.sety(knm)
        tosbaga.pendown()
        direnc()
        knm=knm-50
    tosbaga.left(90)
    for i in range(size):
        tosbaga.forward(50)
    tosbaga.right(90)
    tosbaga.forward(40)
    opamp()
    gnd()
    geribes2()

    tosbaga.penup()
    tosbaga.setposition(-150.69, 110.63)
    tosbaga.pendown
    tosbaga.write("+", font=("arial", 14, "bold"))
    tosbaga.penup()
    tosbaga.setposition(-147.69, 90.63)
    tosbaga.pendown
    tosbaga.write("-", font=("arial", 14, "bold"))
    tosbaga.penup()
    tosbaga.setposition(-23.38,109.26)
    tosbaga.pendown

toplayici(tosbaga)


wn.mainloop()