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
mensajes = []
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
        
        if tipo_var != None:
            tabla_simbolos["variables"][nombre] = tipo_var
            
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
             mensajes.append(f"Error semántico: Variable '{nombre}' no declarada.")
            
            
                                        
# Error rule for syntax errors
def p_error(p):
    print("Error semántico")
    if p:
        mensaje = f"Error semántico en la línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'"
        log_token(mensaje)
    else:
        mensaje = "Error semántico: Fin de archivo inesperado"
        log_token(mensaje)
parser = yacc.yacc(module=sys.modules[__name__])

def log_token(mensaje):
    usuario_git = get_git_user()
    fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, f"semántico-{usuario_git}-{fecha_hora}.txt")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(mensaje + "\n")

if __name__ == "__main__":
    print("Analizador Semántico: ")
    if len(sys.argv) > 1:
        archivo_entrada = sys.argv[1]
    else:
        archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
        
    try:
        with open(archivo_entrada, 'r') as file:
            data = file.read()
        
        parser.parse(data)
        
        while True:
            if not mensajes:
                
                log_token(str(tabla_simbolos))
                break
            else:
                mensaje = mensajes.pop(0)
                log_token(mensaje)
        print("Tabla de Símbolos:")
        for var, tipo in tabla_simbolos["variables"].items():
            print(f"Variable: {var}, Tipo: {tipo}")
            
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo_entrada}")
        log_token(f"Archivo no encontrado: {archivo_entrada}")
    