#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Obtener los primeros dos elementos de cada tupla
    a = tuple_a[:2]
    b = tuple_b[:2]

    # Rellenar con ceros si las tuplas son más pequeñas que 2 elementos
    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))

    # Sumar los elementos correspondientes y retornar la nueva tupla
    return (a[0] + b[0], a[1] + b[1])
