#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Crear un conjunto vacío para almacenar los enteros únicos
    unique_integers = set()

    # Recorrer todos los elementos de la lista
    for num in my_list:
        # Verificar si el elemento es un entero y agregarlo al conjunto
        if isinstance(num, int):
            unique_integers.add(num)

    # Sumar todos los enteros únicos en el conjunto
    total = sum(unique_integers)

    # Devolver la suma total de los enteros únicos
    return total
