import lexer

tests = [
    # 1. Función de diapositivas de clase. 
    (
        "1. Código de diapositiva de Clase",
        """
        int x = 5;
        bool bandera = true;
        
        int suma ( int a , int b ) {
            return a + b;
        }
        
        int main ( ) {
            int y = suma ( x , 3 );
            if ( y > 10 ) {
                print ( y );
            } else {
                print ( 0 );
            }
            
            while ( y > 0 ) {
                y = y - 1;
            }
            
            for ( y = 0 ; y < 10 ; y = y + 1 ) {
                print ( y );
            }
        }
        """,
    ),

    # 2. Palabras reservadas restantes (float, void, false, read)
    (
        "2. Palabras reservadas restantes",
        """
        bool inicializar_valores() {
            float n;
            bool flag = false;

            if (!flag) {
                read(n);
                flag = true;
            }

            return n == 3.14;
        }
        """
    ),
    # 3. Operadores relacionales (==, !=, <=, >=, <, >)
    (
        "3. Operadores relacionales",
        """
        int comparar_numeros(int a, int b) {
            int aux;

            if (a == b) { 
                aux = a;
            }

            if (a != b) {
                if (a >= b) {
                    if (a > b) {
                        aux = a;
                    }
                }

                if (a <= b) {
                    if (a < b) {
                        aux = b;
                    }
                }
            }

            return aux;
        }
        """
    ),
    # 4. Operadores lógicos (&&, ||, !)
    (
        "4. Operadores lógicos",
        """
        bool funcion_and(int a, int b){
            if (a == 1 && b == 1){
                return true;
            }
            
            return false;
        }

        bool funcion_or(int a, int b){
            if (a == 1 || b == 1){
                return true;
            }

            return false;
        }

        bool funcion_not(int a) {
            if (a != 0) {
                return 0;
            } else {
                return 1;
            }
        }
        """
    ),
    # 5. Operadores aritméticos (+, -, *, /)
    (
        "5. Operadores aritméticos",
        """
        void operaciones(float a, float b){
            print("Suma");
            print(a + b);

            print("Resta");
            print(a - b);

            print("Multiplicación");
            print(a * b);

            print("División");
            print(a / b);
        }
        """
    ),
    # 6. Sucesión de Fibonacci
    (
        "6. Sucesión de Fibonacci",
        """
        int fibonacci(int n) {
            if (n <= 1) {
                return n;
            }

            return fibonacci(n-1) + fibonacci(n-2);
        }
        """
    ),

    # 7. Raíz cuadrada (algoritmo babilónico)
    (
        "7. Raíz cuadrada",
        """
        float raiz_cuadrada(float x){
            float b = x;

            while (b != x/b) {
                b = (1/2)*(x/b + b);
            }

            return b;
        }
        """
    ),
    # 8. Algoritmo de emparejamiento de Cantor.
    (
        "8. Emparejamiento de Cantor",
        """
        int emparejamiento(int k1 , int k2) {
            int suma = k1 + k2;
            int factor = suma + 1;
            int n = suma * factor;
            
            int resultado = ( n / 2 ) + k2;

            return resultado;
        }
        """
    ),

    # 9. ERROR — String sin cerrar
    (
        "str sin cerrar",
        """
        print("Ah muy bien);
        print("Ah muy mal");
        """
    ),

    # 10. ERROR — caracter inválido
    (
        "Caracter inválido",
        """
        int = 5 @ 3;
        """,
    ),
]

# ============================================================

for nombre, codigo in tests:
    print(f"\n{'='*60}")
    print(f"TEST: {nombre}")
    print(f"{'='*60}")
    try:
        print(lexer.lexer_multiples_afds(codigo))
    except ValueError as e:
        print(e)
