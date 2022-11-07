"""
This file holds basic operations using Vector such as,
0) __repr__
1) __str__
2) __add__
3) __mul__
4) __getitem__
5) dot_product
6) magnitude
7) normalise

"""

import math


class Vector:
    """
    This class holds methods for defining Vector

    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __str__(self):
        return "{}i + {}j + {}k".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.y)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

    def dot_product(self, other):
        """
        Calculates the dot product of the two vectors

        :param other: other vector
        :return: scalar value - dot product
        """
        return (self.x*other.x) + (self.y+other.y) + (self.z*other.z)

    def magnitude(self):
        """
        Calculates the magnitude of the vector

        :return: magnitude of the vector
        """
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2))

    def normalise(self):
        """
        Normalises the vector

        :return: normalised vector
        """
        mag_value = self.magnitude()
        return Vector(self.x/mag_value, self.y/mag_value, self.z/mag_value)
