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
    """ Getter y setter para el atributo privado '__width'
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ Getter y setter para el atributo privado '__height'
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ Getter y setter para el atributo privado '__x'
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ Getter y setter para el atributo privado '__y'
    """
    @property
    def y(self):
        return self.__y

    """ set y  """

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

        """ public methods: """
    def area(self):
        """ return the area """
        return self.width * self.height

    def display(self):
        """  prints the Rectangle """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x + '#' * self.width)

    """ method  """
    def __str__(self):

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
