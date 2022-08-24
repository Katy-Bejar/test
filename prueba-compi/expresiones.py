from enum import Enum
from turtle import*


#class TURTLE(Enum) :
#    AVANZAR = 1
#    GIRARDERECHA = 2
#    GIRARIZQUIERDA = 3
#    

class ExpresionDireccion:
    '''
        Esta clase representa una expresión numérica
    '''
#class ExpresionTurtle(ExpresionDireccion):
#    def __init__(self, t, ) :
#        self.t = t
#
    
    
class ExpresionA(ExpresionDireccion) :
    def __init__(self, A) :
        self.A = A

class ExpresionGD(ExpresionDireccion) :
    def __init__(self, GD) :
        self.GD = GD
        
class ExpresionGI(ExpresionDireccion) :
    def __init__(self, GI) :
        self.GI = GI


#class ExpresionConcatenar(ExpresionCadena) :
#    '''
#        Esta clase representa una Expresión de tipo cadena.
#        Recibe como parámetros las 2 expresiones a concatenar
#    '''
#
#    def __init__(self, exp1, exp2) :
#        self.exp1 = exp1
#        self.exp2 = exp2