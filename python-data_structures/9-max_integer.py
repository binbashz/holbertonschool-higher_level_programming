#!/usr/bin/python3
def max_integer(my_list=[]):
    # Verificar si la lista está vacía
    if len(my_list) == 0:
        return None

    # Inicializar la variable para almacenar el máximo valor
    max_value = my_list[0]

    # Iterar sobre los elementos de la lista y encontrar el máximo
    for num in my_list:
        if num > max_value:
            max_value = num

    # Retornar el máximo valor encontrado
    return max_value
