fn main() {
    // Variables numéricas
    let x = 10;
    let mut y = 3.14;

    // Métodos válidos sobre números
    x.abs();
    x.pow(2);
    x.to_string();
    y.sqrt();
    y.sin();
    y.round();

    // Errores: método no existe
    x.unknown();

    // Error: número de argumentos incorrecto
    x.abs(1);
    x.pow();

    // Error: no es numérico
    let nombre = "hola";
    nombre.abs();
}