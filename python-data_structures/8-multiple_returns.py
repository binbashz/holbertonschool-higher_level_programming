#!/usr/bin/python3
def multiple_returns(sentence):
    # Verificar si la cadena está vacía
    if len(sentence) == 0:
        return (None,)

    # Obtener la longitud de la cadena y el primer carácter
    length = len(sentence)
    first_char = sentence[0]

    # Retornar la tupla con la longitud y el primer carácter
    return (length, first_char)
