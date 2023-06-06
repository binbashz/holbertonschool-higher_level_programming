#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Verificar si el índice está dentro de los límites de la lista
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Crear una nueva lista sin el elemento en la posición especificada
    new_list = my_list[:idx] + my_list[idx+1:]

    # Retornar la nueva lista
    return new_list
