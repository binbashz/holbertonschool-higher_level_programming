#!/usr/bin/python3

""" 7- Change representation"""


class Rectangle:
    """
    Esta clase representa un rectángulo.

    Atributos:
        width (int): El ancho del rectángulo.
        height (int): La altura del rectángulo.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        Establece el ancho del rectángulo.

        Args:
            value (int): El valor del ancho a establecer.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        Establece la altura del rectángulo.

        Args:
            value (int): El valor de la altura a establecer.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcula el área del rectángulo.

        Returns:
            int: El área del rectángulo.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcula el perímetro del rectángulo.

        Returns:
            int: El perímetro del rectángulo.
            Si el ancho o la altura es igual a 0, devuelve 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Devuelve una representación del rectángulo
        como una cadena de caracteres.

        Returns:
            str: El rectángulo representado como una cadena de caracteres con
            el símbolo de impresión.
            Si el ancho o la altura es igual a 0, devuelve una cadena vacía.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
        Devuelve una representación en forma de cadena del objeto rectángulo.

        Returns:
            str: La representación en forma de cadena del objeto rectángulo.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Imprime el mensaje "Bye rectangle..." cuando se elimina una
        instancia de Rectangle.
        Decrementa el número de instancias.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
