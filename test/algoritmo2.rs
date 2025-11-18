fn main() {
    // ================================
    // Variables válidas
    // ================================
    let nombre = "hola";
    let saludo: String = "buen dia".to_string();
    let edad = 20;
    let precio: f32 = 10.5;
    let mut contador = 0;

    // Métodos válidos de String
    nombre.len();
    saludo.to_uppercase();
    saludo.contains("dia");

    // ================================
    // Errores de variable NO declarada
    // ================================
    no_existe.len();           // ERROR: variable no declarada
    texto.to_uppercase();      // ERROR: variable no declarada

    // ================================
    // Errores por tipo incorrecto
    // ================================
    edad.len();                // ERROR: entero no tiene método len
    precio.contains(10.5);     // ERROR: método no existe para f32
    contador.to_uppercase();   // ERROR: entero no tiene métodos de String

    // ================================
    // Errores por método inexistente
    // ================================
    nombre.unknown();          // ERROR: método no existe en String
    saludo.pepito();           // ERROR: método inexistente

    // ================================
    // Errores por número incorrecto de argumentos
    // ================================
    nombre.len(1);             // ERROR: len no recibe argumentos
    saludo.contains();         // ERROR: falta argumento
    saludo.contains("a", "b"); // ERROR: demasiados argumentos

    // ================================
    // Mutabilidad y reasignaciones
    // ================================
    contador = contador + 1;   // OK: contador es mutable

    nombre = "adios";          // ERROR: nombre NO es mutable
    edad = "hola";             // ERROR: reasignación tipo distinto
    precio = "texto";          // ERROR: reasignación tipo incorrecto

    // ================================
    // Shadowing correcto e incorrecto
    // ================================
    let edad = edad + 1;       // OK: shadowing, nueva variable edad

    let edad = "texto";         // OK (shadowing), pero luego:
    edad.len(10);               // ERROR: método incorrecto + argumentos

    // ================================
    // Llamadas encadenadas válidas
    // ================================
    saludo.to_uppercase().len();

    // ================================
    // Llamadas encadenadas inválidas
    // ================================
    edad.to_uppercase().contains("a");  // ERROR: edad es string → OK to_uppercase, pero es &str?
                                        // tu analizador puede decidir

    20.to_uppercase();                  // ERROR: tipo numérico no tiene métodos

    // ================================
    // Errores combinados
    // ================================
    nombre.contains(123).len();         // ERROR: argumento incorrecto
                                        // ERROR: return type mal manejado
}
