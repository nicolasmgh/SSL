digitos = []
abc = []
whitespace = [" ", "\t", "\n"]

for i in range(10):
    digitos.append(str(i))

i = 65

while i <= 122:
    if i == 91:
        i = 97
    else:
        abc.append(chr(i))
        i += 1

# ("NOMBRE_AFD", ESTADO_INICIAL, {(ORIGEN, SÍMBOLO): DESTINO, (ORIGEN, SÍMBOLO): DESTINO}, {ACEPTADO/S})

lista_afds = [
    # keywords
    ("kw_int", 0, {(0, "i"): 1, (1, "n"): 2, (2, "t"): 3}, {3}),
    (
        "kw_float",
        0,
        {(0, "f"): 1, (1, "l"): 2, (2, "o"): 3, (3, "a"): 4, (4, "t"): 5},
        {5},
    ),
    ("kw_bool", 0, {(0, "b"): 1, (1, "o"): 2, (2, "o"): 3, (3, "l"): 4}, {4}),
    ("kw_void", 0, {(0, "v"): 1, (1, "o"): 2, (2, "i"): 3, (3, "d"): 4}, {4}),
    ("kw_if", 0, {(0, "i"): 1, (1, "f"): 2}, {2}),
    ("kw_else", 0, {(0, "e"): 1, (1, "l"): 2, (2, "s"): 3, (3, "e"): 4}, {4}),
    (
        "kw_while",
        0,
        {(0, "w"): 1, (1, "h"): 2, (2, "i"): 3, (3, "l"): 4, (4, "e"): 5},
        {5},
    ),
    ("kw_for", 0, {(0, "f"): 1, (1, "o"): 2, (2, "r"): 3}, {3}),
    (
        "kw_return",
        0,
        {(0, "r"): 1, (1, "e"): 2, (2, "t"): 3, (3, "u"): 4, (4, "r"): 5, (5, "n"): 6},
        {6},
    ),
    (
        "kw_print",
        0,
        {(0, "p"): 1, (1, "r"): 2, (2, "i"): 3, (3, "n"): 4, (4, "t"): 5},
        {5},
    ),
    ("kw_read", 0, {(0, "r"): 1, (1, "e"): 2, (2, "a"): 3, (3, "d"): 4}, {4}),
    ("kw_true", 0, {(0, "t"): 1, (1, "r"): 2, (2, "u"): 3, (3, "e"): 4}, {4}),
    ("kw_false", 0, {(0, "f"): 1, (1, "a"): 2, (2, "l"): 3, (3, "s"): 4, (4, "e"): 5}, {5}),
    ("kw_string", 0, {(0, "s"): 1, (1, "t"): 2, (2, "r"): 3, (3, "i"): 4, (4, "n"): 5, (5, "g"): 6}, {6}),
    
    # literales
    (
        "id",
        0,
        {
            **{(0, e): 1 for e in abc + ["_"]},
            **{(1, e): 1 for e in abc + ["_"] + digitos},
        },
        {1},
    ),
    (
        "num",
        0,
        {
            **{(0, e): 1 for e in digitos},
            **{(1, e): 1 for e in digitos},
            (1, "."): 2,
            **{(2, e): 3 for e in digitos},
            **{(3, e): 3 for e in digitos},
        },
        {1, 3},
    ),
    (
        "str",
        0,
        {
            (0, '"'): 1,
            **{(1, chr(e)): 1 for e in range(0x110000) if chr(e) != '\n'},
            (1, '"'): 2,
        },
        {2},
    ),
    
    # operadores relaciones
    ("op_eq", 0, {(0, "="): 1, (1, "="): 2}, {2}),
    ("op_neq", 0, {(0, "!"): 1, (1, "="): 2}, {2}),
    ("op_lteq", 0, {(0, "<"): 1, (1, "="): 2}, {2}),
    ("op_gteq", 0, {(0, ">"): 1, (1, "="): 2}, {2}),
    ("op_lt", 0, {(0, "<"): 1}, {1}),
    ("op_gt", 0, {(0, ">"): 1}, {1}),
    
    # operadores lógicos
    ("op_and", 0, {(0, "&"): 1, (1, "&"): 2}, {2}),
    ("op_or", 0, {(0, "|"): 1, (1, "|"): 2}, {2}),
    ("op_not", 0, {(0, "!"): 1}, {1}),
    
    # operadores aritméticos
    ("op_add", 0, {(0, "+"): 1}, {1}),
    ("op_subt", 0, {(0, "-"): 1}, {1}),
    ("op_mult", 0, {(0, "*"): 1}, {1}),
    ("op_div", 0, {(0, "/"): 1}, {1}),
    
    # operador de asignación
    ("op_assign", 0, {(0, "="): 1}, {1}),
    
    # símbolos de puntuación
    ("lparen", 0, {(0, "("): 1}, {1}),
    ("rparen", 0, {(0, ")"): 1}, {1}),
    ("lbrace", 0, {(0, "{"): 1}, {1}),
    ("rbrace", 0, {(0, "}"): 1}, {1}),
    ("semicolon", 0, {(0, ";"): 1}, {1}),
    ("comma", 0, {(0, ","): 1}, {1}),
    
    # especiales
    ("whitespace", 0, {
        ** {(0, e): 1 for e in whitespace},
        ** {(1, e): 1 for e in whitespace}
        }, {1}),
]
