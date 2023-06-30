#!/usr/bin/python3
"""
rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle instance.
        """
        self.validate_attributes(width, height, x, y)
        self._width = width
        self._height = height
        self._x = x
        self._y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """
        self.validate_attribute(value, "width")
        self._width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """
        self.validate_attribute(value, "height")
        self._height = value

    @property
    def x(self):
        """
        Getter for the x attribute.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.
        """
        self.validate_attribute(value, "x")
        self._x = value

    @property
    def y(self):
        """
        Getter for the y attribute.
        """
        return self._y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.
        """
        self.validate_attribute(value, "y")
        self._y = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle.
        """
        return self._width * self._height

    def display(self):
        """
        Displays the Rectangle instance using '#' character.
        """
        for _ in range(self._y):
            print()
        for _ in range(self._height):
            print(" " * self._x + "#" * self._width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self._x, self._y, self._width, self._height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance.
        """
        if args:
            self.update_with_args(*args)
        else:
            self.update_with_kwargs(**kwargs)

    def update_with_args(self, *args):
        """
        Updates the attributes using arguments.
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

    def update_with_kwargs(self, **kwargs):
        """
        Updates the attributes using keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle instance.
        """
        return {
            "id": self.id,
            "width": self._width,
            "height": self._height,
            "x": self._x,
            "y": self._y
        }

    @staticmethod
    def validate_attributes(*args):
        """
        Validates the attributes of the Rectangle instance.
        """
        attribute_names = ["width", "height", "x", "y"]
        for i, value in enumerate(args[:2]):
            if not isinstance(value, int):
                raise TypeError(f"{attribute_names[i]} must be an integer")
            if value <= 0:
                raise ValueError(f"{attribute_names[i]} must be > 0")
        for i, value in enumerate(args[2:]):
            if not isinstance(value, int):
                raise TypeError(f"{attribute_names[i + 2]} must be an integer")
            if value < 0:
                raise ValueError(f"{attribute_names[i + 2]} must be >= 0")

    @staticmethod
    def validate_attribute(value, attribute_name):
        """
        Validates a single attribute of the Rectangle instance.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")
