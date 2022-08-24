
import gramatica as g
import turtle
import ts as TS
from expresiones import *
from instrucciones import *
import instrucciones as IS

def procesar_avanzar():
    simbolo = IS.Avanzar.turtleA
    return simbolo
    
def procesar_girarderecha(instr, ts):
    simbolo = TS.Simbolo(instr.PR , TS.TIPO_DATO.GIRARDERECHA)
    ts.agregar(simbolo)
    
def procesar_girarizquierda(instr, ts):
    simbolo = TS.Simbolo(instr.PR , TS.TIPO_DATO.GIRARIZQUIERDA)
    ts.agregar(simbolo)

    
def procesar_instrucciones() :
    if TS.TIPO_DATO.AVANZAR:
        procesar_avanzar()
        #if isinstance(instr, Avanzar) : procesar_avanzar(instr, ts)
        #elif isinstance(instr,Girar_derecha) : procesar_girarderecha(instr, ts)
        #elif isinstance(instr, Girar_izquierda) : procesar_girarizquierda(instr, ts)
        #else : print('Error: instrucción no válida')
        
        
tortuga = turtle.Turtle()
tortuga = shape("turtle")
wn = turtle.Screen()
wn.bgcolor("lightgreen")


f = open("program.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones()
wn.mainloop()