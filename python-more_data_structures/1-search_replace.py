#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Crear una nueva lista para almacenar los elementos modificados
    new_list = []

    # Recorrer todos los elementos de la lista original
    for item in my_list:
        # Verificar si el elemento coincide con el valor de búsqueda
        if item == search:
            # Si coincide, agregar el elemento de reemplazo a la nueva lista
            new_list.append(replace)
        else:
            # Si no coincide, agregar el elemento original a la nueva lista
            new_list.append(item)

    # Devolver la nueva lista modificada
    return new_list
