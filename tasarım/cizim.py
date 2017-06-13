import turtle

konum = [-400, 100]

def direnc(tosbaga):
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

def opamp(tosbaga):
    tosbaga.forward(20)
    tosbaga.left(90)
    tosbaga.forward(20)
    for i in range(2):
        tosbaga.right(120)
        tosbaga.forward(60)
    tosbaga.right(120)
    tosbaga.forward(40)
    tosbaga.backward(20)

def gnd(tosbaga):
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

def geribes1(tosbaga):
    global konum
    tosbaga.penup()
    tosbaga.setposition(konum[0] + 41,konum[1])
    tosbaga.right(180)
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

def geribes2(tosbaga):
    global konum
    tosbaga.penup()
    tosbaga.setposition(konum[0] + 41,konum[1])
    tosbaga.pendown()

    for i in range(2):
        tosbaga.right(90)
        tosbaga.forward(50)
    direnc(tosbaga)
    tosbaga.forward(50)
    tosbaga.right(90)
    tosbaga.forward(60)
    tosbaga.right(90)
    tosbaga.forward(30)
    tosbaga.backward(80)
    tosbaga.right(180)

def integral_alan(tosbaga):
    global konum
    tosbaga.penup()
    tosbaga.setposition(konum[0],konum[1])
    tosbaga.pendown()
    direnc(tosbaga)
    opamp(tosbaga)
    gnd(tosbaga)
    geribes1(tosbaga)

    tosbaga.penup()
    tosbaga.setposition(konum[0]+67, konum[1]-10)
    tosbaga.pendown()
    tosbaga.write("+", font=("arial",14,"bold"))
    tosbaga.penup()
    tosbaga.setposition(konum[0]+69, konum[1]-30)
    tosbaga.pendown()
    tosbaga.write("-", font=("arial", 14, "bold"))
    tosbaga.penup()
    tosbaga.setposition(konum[0] + 15, konum[1] + 10)
    tosbaga.pendown()
    tosbaga.write("R", font=("arial", 14, "bold"))

    tosbaga.penup()
    tosbaga.setposition(konum[0] + 81, konum[1] + 75)
    tosbaga.pendown()
    tosbaga.write("C", font=("arial", 14, "bold"))

    tosbaga.penup()
    tosbaga.setposition(konum[0]+170,konum[1]-10)
    tosbaga.pendown()

    konum[0] = konum[0]+169
    konum[1] = konum[1]-10

def toplayici(tosbaga):
    global konum
    tosbaga.penup()
    tosbaga.setposition(konum[0],konum[1])
    tosbaga.pendown()
    direnc(tosbaga)

    knm = konum[1]-50
    for i in range(size):
        tosbaga.penup()
        tosbaga.setx(konum[0])
        tosbaga.sety(knm)
        tosbaga.pendown()
        direnc(tosbaga)
        knm = knm-50
    tosbaga.left(90)

    for i in range(size):
        tosbaga.forward(50)
    tosbaga.right(90)
    tosbaga.forward(40)
    opamp(tosbaga)
    gnd(tosbaga)
    geribes2(tosbaga)

    tosbaga.penup()
    tosbaga.setposition(konum[0]+108, konum[1]-10)
    tosbaga.pendown()
    tosbaga.write("+", font=("arial", 14, "bold"))

    tosbaga.penup()
    tosbaga.setposition(konum[0]+109, konum[1]-30)
    tosbaga.pendown()
    tosbaga.write("-", font=("arial", 14, "bold"))

    tosbaga.penup()
    tosbaga.setposition(konum[0] + 105, konum[1] + 60)
    tosbaga.pendown()
    tosbaga.write("R", font=("arial", 14, "bold"))

    tosbaga.penup()
    tosbaga.setposition(konum[0] + 15, konum[1] + 10)
    tosbaga.pendown()

    knm1 = konum[1] + 10
    for i in range(size+1):
        tosbaga.penup()
        tosbaga.setposition(konum[0] + 15, knm1)
        tosbaga.pendown()
        tosbaga.write("R", font=("arial", 14, "bold"))
        knm1 = knm1 - 50

    tosbaga.penup()
    tosbaga.setposition(konum[0] + 233,konum[1] - 10)
    tosbaga.pendown()

    konum[0] = konum[0] + 232
    konum[1] = konum[1] - 10


