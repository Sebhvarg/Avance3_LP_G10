// Archivo de prueba para validación semántica
// Prueba de reglas semánticas del analizador

// REGLA 1 y 6: Declaración de variables
let x = 10;
let mut y = 20;
const PI = 3.14;

// REGLA 2, 3, 4: Pruebas de reasignación
y = 25;
x = 15;

// REGLA 3: Intento de modificar constante (ERROR)
PI = 3.1416;

// REGLA 9: Uso de variable no declarada (ERROR)
let resultado = z + 5;

// REGLA 10, 11, 12: Operaciones aritméticas
let suma = 5 + 3;
let multiplicacion = 4 * 2;

// REGLA 11: Operación con tipo no numérico (ERROR)
let cadena = "hola";
let error_tipo = cadena + 5;

// REGLA 5, 12: Incompatibilidad de tipos
let entero = 42;
let flotante = 3.14;
let mezcla = entero + flotante;

// REGLA 14: Declaración de función
fn calcular() {
    let temp = 100;
}

// REGLA 16: Llamada a función
calcular();

// REGLA 16: Llamada a función no declarada (ERROR)
funcion_inexistente();

// REGLA 21: Variable no usada (ADVERTENCIA)
let no_usada = 999;
