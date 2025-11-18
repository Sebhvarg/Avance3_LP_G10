fn main() {
    //  Error semántico 1: variable no definida
    // Intentamos usar una variable "nombre" que nunca fue declarada.
    // Análogo a: "la variable {nombre} no ha sido definida"
    let resultado1 = nombre.len();
    println!("Resultado: {}", resultado1);

    // ----------------------------------------------

    //  Error semántico 2: variable definida pero de tipo incorrecto
    // "edad" es un i32, intentamos usar un método propio de String
    // Análogo a: "la variable {nombre} no es un str"
    let edad: i32 = 25;
    let resultado2 = edad.to_uppercase(); 
    println!("Resultado: {:?}", resultado2);

    // ----------------------------------------------

    //  Error semántico 3: método no existente para String
    // Análogo a: "el metodo {metodo} no es parte de las funciones de string"
    let nombre2 = String::from("Fernando");
    let resultado3 = nombre2.invertir(); // método inexistente
    println!("Resultado: {:?}", resultado3);

    // ----------------------------------------------

    //  Error semántico 4: método mal llamado en String (argumentos incorrectos)
    let texto = String::from("hola");
    let resultado4 = texto.replace(123, 456); 
    println!("Resultado: {:?}", resultado4);
}
:heart:
Haz clic para reaccionar
:laughing:
Haz clic para reaccionar
:rofl:
Haz clic para reaccionar
Agregar reacción
Responder
Reenviar
Más

Mensaje @Fernan B.
