#!/usr/bin/python3
"""
    rectangle module
"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Llamamos al constructor de la superclase (Base)
         utilizando super().__init__(id).
         Esto asegura que la lógica de creación del atributo 'id'
         en la clase Base se ejecute correctamente.
         """
        super().__init__(id)

        """ Asignamos cada argumento (width, height, x, y)
        a su respectivo atributo.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Getter y setter para el atributo privado __width
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    """ Getter y setter para el atributo privado __height
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    """ Getter y setter para el atributo privado '__x'
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    """ Getter y setter para el atributo privado '__y'
    """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
