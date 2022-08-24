from enum import Enum
import turtle

class TIPO_DATO(Enum) :
    AVANZAR = 1
    GIRARDERECHA = 2
    GIRARIZQUIERDA = 3
    

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, PR, tipo, val) :
        self.PR = PR
        self.tipo = tipo
        self.val = val
     

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos
        
    #def ava(self, simbolo) :
    #    self.simbolos[simbolo.tipo] = simbolo
#
    def agregar(self, simbolo) :
        self.simbolos[simbolo.PR] = simbolo
        
    #def Ava(self, simbolo, t) :
    #    self.simbolos[simbolo.PR] = simbolo
    #    self.simbolo = t.forward(t)
    #
    
    def obtener(self, PR) :
        if not id in self.simbolos :
            print('Error: variable ', PR, ' no definida.')

        return self.simbolos[PR]

    def actualizar(self, simbolo) :
        if not simbolo.PR in self.simbolos :
            print('Error: variable ', simbolo.PR, ' no definida.')
        else :
            self.simbolos[simbolo.PR] = simbolo
