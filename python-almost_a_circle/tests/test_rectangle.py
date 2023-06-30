#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_area(self):
        """Test the area() method."""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        """Test the display() method."""
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_out:
            rectangle.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__() method."""
        rectangle = Rectangle(4, 5, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 4/5\n"
        self.assertEqual(str(rectangle), expected_output)

    def test_update(self):
        """Test the update() method."""
        rectangle = Rectangle(2, 3)
        rectangle.update(5, 10, 1, 2, 7)
        expected_output = "[Rectangle] (5) 1/2 - 10/7\n"
        self.assertEqual(str(rectangle), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        rectangle = Rectangle(3, 4, 2, 1, 15)
        expected_output = {
            "id": 15,
            "width": 3,
            "height": 4,
            "x": 2,
            "y": 1
        }
        self.assertEqual(rectangle.to_dictionary(), expected_output)


if __name__ == '__main__':
    unittest.main()
