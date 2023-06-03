#!/usr/bin/python3

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    import sys

    # Obtiene el número de argumentos pasados al programa
    num_args = len(sys.argv) - 1

    # Verifica si no se han pasado argumentos
    if num_args == 0:
        print(f"{num_args} arguments.")
    # Verifica si se ha pasado un único argumento
    elif num_args == 1:
        print(f"{num_args} argument:")
        print(f"{num_args}: {sys.argv[num_args]}")
    # Si se han pasado múltiples argumentos
    else:
        print(f"{num_args} arguments:")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
