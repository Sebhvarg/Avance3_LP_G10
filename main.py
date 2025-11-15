# ------------------------------------------------------------ 
# parser.py
# Analizador Semantico usando PLY.Yacc
# Grupo 10
# ------------------------------------------------------------
import ply.yacc as yacc
import sys
import datetime
import os
from Lexicon.lexer import tokens, get_git_user
from Syntax.syntax import *
# ------------------------------------------------------------
# Integrantes:
#   Derian Baque Choez (fernan0502)
#   Sebastian Holguin (Sebhvarg)
#   Carlos Ronquillo (carrbrus)
# ------------------------------------------------------------

# ------------------------------------------------------------
# Tabla de Símbolos
tabla_simbolos = {
    "variables": {},
    "funciones": {},
    "tipos": {
        "str-funciones": ["len", "push", "contains", "starts_with", 
                          "ends_with", "index_of", "to_uppercase", 
                          "to_lowercase", "replace", "substring",
                          "split", "trim", "chars", "is_empty"
                          "concat", "parse", "count"
                          ],
        
        },
    "clases": {}    
}

def p_asignacion(p):
    '''asignacion : VARIABLE IDENTIFICADOR IGUAL valor PUNTOCOMA
                    | IDENTIFICADOR IGUAL valor PUNTOCOMA                    
    '''
    if len(p) == 6:
        nombre = p[2]
        tipo_var = p[4]
        tabla_simbolos["variables"][nombre] = tipo_var
        print(f"Variable '{nombre}' asignada con valor de tipo '{tipo_var}'")
    else:
        nombre = p[2]
        tipo_var = None

def p_valor(p):
     '''valor : CADENA
             | CARACTER
             | BOOLEANO
             | IDENTIFICADOR
             | asignacion 
             | valor_numerico
             | operacion_aritmetica
             | tupla
             | matriz
             | llamada_funcion_sin_puntocoma
             | bloque_con_retorno'''
     if isinstance(p[1], str) and p.slice[1].type == 'CADENA':
         p[0] = "str"
     elif isinstance(p[1], bool) and p.slice[1].type == 'BOOLEANO':
            p[0] = "bool"
     elif p.slice[1].type == 'CARACTER':
         p[0] = "char"
     elif isinstance(p[1], int):
         p[0] = "int"
     elif isinstance(p[1], float):
            p[0] = "float"
     elif p.slice[1].type == 'IDENTIFICADOR':
         nombre = p[1]
         if nombre in tabla_simbolos["variables"]:
             p[0] = tabla_simbolos["variables"][nombre]
         else:
             print(f"Error semántico: Variable '{nombre}' no declarada.")
             p[0] = "undefined"
     else:
         p[0] = "unknown"
            
                                        
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
parser = yacc.yacc(module=sys.modules[__name__])

while True:
   try:
       s = input('arust > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
   print(tabla_simbolos)