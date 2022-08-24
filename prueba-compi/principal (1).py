
import gramatica as g
import turtle
import ts as TS
from expresiones import *
from instrucciones import *
import instrucciones as I
#def procesar_mientras(instr, ts) :
#    while resolver_expreision_logica(instr.expLogica, ts) :
#        ts_local = TS.TablaDeSimbolos(ts.simbolos)
#        procesar_instrucciones(instr.instrucciones, ts_local)
#
###def procesar_avanzar(instr):
###    #print(I.Avanzar)
###    #a = TS.TIPO_DATO.AVANZAR 
###    #return a
###    print('> ', resolver_expreision_logica(instr.cad))
###
###def resolver_expreision_logica(expLog) :
###    if expLog.operador == TS.TIPO_DATO.AVANZAR : return Avanzar
###    if expLog.operador == TS.TIPO_DATO.GIRARDERECHA : return Avanzar
###    if expLog.operador == TS.TIPO_DATO.GIRARIZQUIERDA : return Avanzar
def procesar_avanzar1(instr, ts):
    simbolo = Avanzar.turtleA()
    return simbolo
    
    
def procesar_avanzar(instr, ts):
    simbolo = TS.Simbolo(instr.PR , TS.TIPO_DATO.AVANZAR, 0)
    ts.actualizar(simbolo)
    
def procesar_girarderecha(instr, ts):
    simbolo = TS.Simbolo(instr.PR , TS.TIPO_DATO.GIRARDERECHA)
    ts.agregar(simbolo)
    
def procesar_girarizquierda(instr, ts):
    simbolo = TS.Simbolo(instr.PR , TS.TIPO_DATO.GIRARIZQUIERDA)
    ts.agregar(simbolo)

    
def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        #if isinstance(instr, Avanzar) : procesar_avanzar1()
        if isinstance(instr, Avanzar) : procesar_avanzar(instr, ts)
        elif isinstance(instr,Girar_derecha) : procesar_girarderecha(instr, ts)
        elif isinstance(instr, Girar_izquierda) : procesar_girarizquierda(instr, ts)
        else : print('Error: instrucción no válida')
        
        
tortuga = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")


f = open("program.txt", "r")
input = f.read()

instrucciones = g.parse(input)
ts_global = TS.TablaDeSimbolos()

procesar_instrucciones(instrucciones, ts_global)
wn.mainloop()