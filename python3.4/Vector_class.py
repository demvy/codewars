__author__ = 'valeriy'
"""
Description:

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
a.add(b) # should return Vector([4,6,8])
a.subtract(b) # should return Vector([-2,-2,-2])
a.dot(b) # should return 1*3+2*4+3*5 = 26
a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
a.add(c) # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals function, so that two vectors who have the same components are equal
The test cases will utilize the user-provided equals method.
"""

from math import sqrt


class Vector:
    def __init__(self, lst):
        self.array = lst

    def equals(self, obj2):
        return self.array == obj2.array

    def __str__(self):
        return '(%s)' % (','.join([str(x) for x in self.array]))

    def add(self, obj2):
        if len(self.array) == len(obj2.array):
            return Vector(map(lambda x: x[0] + x[1], zip(self.array, obj2.array)))
        else:
            raise ValueError('not equal length of vectors')

    def subtract(self, obj2):
        if len(self.array) == len(obj2.array):
            return Vector(map(lambda x: x[0] - x[1], zip(self.array, obj2.array)))
        else:
            raise ValueError('not equal length of vectors')

    def norm(self):
        lst = map(lambda x: x**2, self.array)
        return sqrt(float(sum(lst)))

    def dot(self, obj2):
        if len(self.array) == len(obj2.array):
            lst = map(lambda x: x[0]*x[1], zip(self.array, obj2.array))
            return sum(lst)
        else:
            raise ValueError('not equal length of vectors')

if __name__ == "__main__":
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    c = Vector([7, 8, 9])
    d = Vector([3, 2, 6, 6])
    add = a.add(b)
    sub = a.subtract(b)
    print(a.norm())
    dot = a.dot(b)
    #err = a.add(d)
    print(add)
    print(sub)
    print(dot)