#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Crear una lista vacía para almacenar los resultados
    result = []

    # Iterar sobre los elementos de la lista original
    for num in my_list:
        # Verificar si el número es divisible por 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    # Retornar la lista de resultados
    return result
