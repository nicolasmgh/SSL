import afds

def lexer_multiples_afds(codigo_fuente):
    tokens = []
    pos_actual = 0
    n = len(codigo_fuente)

    while pos_actual < n:  # recorremos todos los caracteres del código fuente
        longitud_mejor_match = 0
        tipo_mejor_match = None
        lexema_mejor_match = ""

        for (
            afd
        ) in (
            afds.lista_afds
        ):  # en este ciclo interno, alimentamos el lexema actual a todos los afds
            tipo, estado_inicial, delta, estados_aceptados = afd
            estado_actual = estado_inicial
            pos_lexema_actual = pos_actual  # por cada afd, comenzamos desde la posición actual en el código fuente
            # después del último token aceptado
            ultima_pos_aceptada = -1

            while pos_lexema_actual < n:
                clave = (estado_actual, codigo_fuente[pos_lexema_actual])
                if clave not in delta:
                    break  # salimos por el estado trampa
                estado_actual = delta[clave]
                pos_lexema_actual += (
                    1  # avanzamos hasta llegar al estado trampa del afd actual
                )
                if estado_actual in estados_aceptados:
                    ultima_pos_aceptada = pos_lexema_actual

            if ultima_pos_aceptada > pos_actual:
                longitud_lexema_actual = ultima_pos_aceptada - pos_actual
                if (
                    longitud_lexema_actual > longitud_mejor_match
                ):  # principio maximal munch, lexema más largo gana
                    # si son iguales, se mantiene el actual
                    # por eso importa el orden en lista_afds
                    longitud_mejor_match = longitud_lexema_actual
                    tipo_mejor_match = tipo
                    lexema_mejor_match = codigo_fuente[pos_actual:ultima_pos_aceptada]

        # en caso de no haber armado un token válido...
        if longitud_mejor_match == 0:
            char = codigo_fuente[pos_actual]

            # arrancó un string pero no fue aceptada, asumo que es un string sin comilla de cierre
            if char == '"':

                # busco salto de línea para hacer de tope y mostrar el contenido (ya que el salto de línea no está incluido en el string)
                fin = codigo_fuente.find('\n', pos_actual)
                if fin == -1:
                    fin = n # si no hay otro salto de línea, el string corta en el EOF

                raise ValueError(f"ERROR: String sin cerrar en posición {pos_actual}: '{codigo_fuente[pos_actual:fin]}'")
            else:
                # cualquier otro caracter que ningun AFD reconoce
                raise ValueError(f"ERROR: Carácter inesperado en posición {pos_actual}: '{char}'")

        tokens.append((tipo_mejor_match, lexema_mejor_match))
        pos_actual += longitud_mejor_match  # se avanza lo que se consumió

    tokens = [t for t in tokens if t[0] != "whitespace"]
    tokens.append(("EOF", "EOF"))
    return tokens