#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initializing the attributes"""

        self.integer_validator("size", size)
        super().__init__(size, size)  # Call super() after the validation
        self.__size = size

    def area(self):
        """Calculate square area"""

        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
