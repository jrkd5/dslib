import math
from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply every element by c"""
    return [c * v_i for v_i in v]


assert scalar_multiply(5, [1, 2, 3]) == [5, 10, 15]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "Vectors must be the same length"
    return add(v, scalar_multiply(-1, w))


assert subtract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vector is not empty
    assert vectors, "No vectors provided"

    # Check the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Not same size"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2, 3], [1, 0, 1], [3, 3, 3]]) == [5, 5, 7]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    """Computes a dot product of two vectors"""
    assert len(v) == len(w), "Vectors must be the same size"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    """Returns sum of squares of vector components"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14  # 1 + 4 + 9


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of a vector"""
    return math.sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes the squared distance between two vectors"""
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Returns the absolute distance between two vectors"""
    return math.sqrt(squared_distance(v, w))


def shape(a: Matrix) -> Tuple[int, int]:
    """Returns the mxn size of the matrix"""
    num_rows = len(a)
    num_cols = len(a[0]) if a else 0
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(a: Matrix, i: int) -> Vector:
    """Returns -th row of a matrix"""
    return a[i]


assert get_row([[1, 2, 3], [4, 5, 6]], 1) == [4, 5, 6]


def get_column(a: Matrix, j: int) -> Vector:
    """Returns j-th column of a matrix"""
    return [a_i[j] for a_i in a]


assert get_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [3, 6, 9]


def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable) -> Matrix:
    """
    Returns a m_rows x _num_cols matrix
    whose (i, j)-th entry is entry(i, j)
    """
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Creates nxn identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
