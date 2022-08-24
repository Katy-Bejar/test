
from turtle import*
#t = turtle.Turtle()


class Instruccion:
    '''This is an abstract class'''
    
class Avanzar(Instruccion):
    def __init__(self, avanzar):
        self.avanzar = avanzar
        
    def turtleA(self):
        self.avanzar = forward(100)
        return self.avanzar 

    #def av(t):
    #    avanzar = t.forward(100)
    #    return avanzar
#class TurtleAvanzar(Avanzar):
#    def __init__(self, t):
#        #t = turtle.Turtle()
#        self.avanzar = forward(100)



class Girar_derecha(Instruccion):
    def __init__(self, girarderecha):
        self.girarderecha = girarderecha
        
    def turtleD(self):
        self.girarderecha = right(90)
        return self.girarderecha 

    #def girarderecha(t):
    #    self.girarderecha = t.right(90)


class Girar_izquierda(Instruccion):
    def __init__(self, girarizquierda):
        self.girarizquierda = girarizquierda

    def turtleI(self):
        self.girarizquierda = left(90)
        return self.girarizquierda 

#
    #def girarizquierda(t):
    #    self.girarizquierda = t.left(90)

