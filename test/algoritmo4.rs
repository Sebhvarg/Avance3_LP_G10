fn main() {
    // Nuevas variables válidas
    let flag = true;
    let letra = 'A';
    let pi_aprox = 3.14159;
    let numeros = [1, 2, 3, 4];
    let palabras = ["hola", "mundo"];
    let mensaje = String::from("Hola desde el test 4");

    // Métodos nuevos de número
    10.is_positive();   // OK
    (-5).is_negative(); // OK
    5.factorial();      // OK

    3.14.factorial();   // ERROR: no aplica a float
    10.is_positive(3);  // ERROR: demasiados args

    // Métodos nuevos de string
    mensaje.reverse();
    mensaje.repeat(3);
    mensaje.slice(1, 3);

    mensaje.repeat();         // ERROR
    mensaje.slice(1);         // ERROR
    mensaje.slice(1, 2, 3);   // ERROR

    // Encadenamientos válidos
    mensaje.to_uppercase().reverse();

    // Encadenamientos inválidos
    10.to_string().is_positive(); // ERROR: método no válido para string

    // Funciones nuevas
    saludar("Carlos");
    sumar(10, 20);
    es_par(7);
    promedio(1.0, 2.0, 3.0);

    sumar(10);            // ERROR: falta argumento
    es_par("hola");       // ERROR: tipo incorrecto
    promedio(1, 2, 3, 4); // ERROR: demasiados argumentos

    let usuario = crear_usuario("Ana", 30);
    usuario.nombre;
    usuario.edad;
    usuario.altura; // ERROR: no existe campo
}
