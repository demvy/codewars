#!-*-coding: utf-8 -*-
__author__ = 'valeriy'

import numpy as np


def matrix_creation():
    """
    Creates and returns matrix in shape(10,10,10), filled with random numbers [-9,9]
    """
    matrix = np.random.randint(-9, 10, (10, 10, 10), dtype=int)
    print(matrix)
    return matrix


def multiply(vector):
    """
    This function multiplies all elements in iterable object
    :param vector: iterable object
    :returns: multiplied elements in vector
    """
    return float(reduce(lambda x, y: x*y, vector))


def list_of_multiplied_vectors(matrix):
    """
    Creates list, filled with multiplied orthogonal vectors
    :param matrix: 3-dimensional array - matrix
    :returns: list with multiplied orthogonal vectors
    """
    mul_list = []
    it = np.nditer(matrix, flags=['multi_index'])
    while not it.finished:
        #print it.multi_index
        x, y, z = it.multi_index
        vector1 = [matrix[z, i, y] for i in range(0, 10)]
        vector2 = [matrix[z, x, i] for i in range(0, 10)]
        vector3 = [matrix[i, x, y] for i in range(0, 10)]
        mul1 = multiply(vector1)
        mul2 = multiply(vector2)
        mul3 = multiply(vector3)
        #print(vector1, vector2, vector3)
        #print(mul1, mul2, mul3)
        mul = mul1*mul2*mul3
        #print(mul)
        mul_list.append(mul)
        it.iternext()
    return mul_list


def selecting_minimum(matrix, mul_list):
    """
    This function selects minimal element in mul_list and searches correspondent element in matrix.
    :param matrix: 3-dimensional array - matrix
    :param mul_list: list with multiplied orthogonal vectors
    :return: tuple with coordinates of point in matrix, in which 3 vectors are orthogonal and
     have minimum multiplicative number
    """
    min_in_list = min(mul_list)
    index = mul_list.index(min_in_list)
    it = np.nditer(matrix, flags=['multi_index'])
    while not it.finished:
        x, y, z = it.multi_index
        index_number = x*100 + y*10 + z*1
        if index_number == index:
            print(it.multi_index, min_in_list)
            return it.multi_index
        it.iternext()

if __name__ == "__main__":
    matrix = matrix_creation()
    multiplied_vectors_list = list_of_multiplied_vectors(matrix)
    coordinates = selecting_minimum(matrix, multiplied_vectors_list)