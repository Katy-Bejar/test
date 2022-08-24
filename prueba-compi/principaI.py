import turtle


wn = turtle.Screen()
#wn = bgcolor("red")
wn.bgcolor("blue")
def avanzar(t, sz):
    t.pendown()
    t.forward(sz)

def girarderecha(t):
    t.pendown()
    t.right(90)

def girarizquierda(t):
    t.pendown()
    t.left(90)

def f(t):
    datos2 = []
    with open("program.txt") as fname:
        for lineas in fname:
            datos2.extend(lineas.split())
            #print("i", datos2)
    #print(datos2)
    #print("*")
    return datos2

tortuga = turtle.Turtle()
def comprobation(t):
    datos2 = f(t)
    print(datos2)
    for i in range(len(datos2)):
        if datos2[i] == "avanzar;":
            avanzar(tortuga, 100)
        elif datos2[i] == "girarderecha;":
            girarderecha(tortuga)
        else:
            girarizquierda(tortuga)



#tortuga = turtle.Turtle()
tortuga.speed(1)
comprobation(tortuga)
wn.mainloop()