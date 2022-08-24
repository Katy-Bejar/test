reservadas = {
    #'begin': 'BEGIN',
    #'end': 'END',
    'avanzar': 'AVANZAR',
    'girarderecha': 'GIRARDERECHA',
    'girarizquierda': 'GIRARIZQUIERDA' 
}

tokens  = [
    #'LLAVEIZQ',
    #'LLAVELDER',
    'PTCOMA',
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Definición de la gramática

from expresiones import *
from instrucciones import *


def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : avanzar_instr
                        | girarderecha_instr
                        | girarizquierda_instr '''
    t[0] = t[1]


def p_instruccion_avanzar(t):
    'avanzar_instr  : AVANZAR PTCOMA'
    t[0] = Avanzar(t[1]) #falta procesar

def p_instruccion_girarderecha(t):
    'girarderecha_instr : GIRARDERECHA PTCOMA'
    t[0] = Girar_derecha(t[1]) #falta procesar

def p_instruccion_girarizquierda(t):
    'girarizquierda_instr : GIRARIZQUIERDA PTCOMA'
    t[0] = Girar_izquierda(t[1]) #falta procesar






def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)

