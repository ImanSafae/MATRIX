from Vector import Vector
from Matrix import Matrix

def lerp(a, b, t: float):
    if not isinstance(a, (int, float, Vector, Matrix)):
        raise TypeError("a must be a number, Vector, or Matrix")
    if not isinstance(b, (int, float, Vector, Matrix)):
        raise TypeError("b must be a number, Vector, or Matrix")
    if type(a) != type(b):
        raise ValueError("a and b must be of the same type")
    if (t < 0 or t > 1):
        raise ValueError("t must be between 0 and 1")
    if isinstance(a, Vector) and isinstance(b, Vector):
        if (a.size() != b.size()):
            raise ValueError("Vectors must be of similar size")
    elif isinstance(a, Matrix) and isinstance(b, Matrix):
        if (a.shape() != b.shape()):
            raise ValueError("Matrices must be of similar shape")
    result = a + (b - a) * t
    return result

# def linear_interpolation_vector(v1: Vector, v2: Vector, t: float):
#     if (v1.size() != v2.size()):
#         raise ValueError("Vectors must be of similar size")
#     if (t < 0 or t > 1):
#         raise ValueError("t must be between 0 and 1")
#     result = v1 + (v2 - v1) * t
#     return result

# def linear_interpolation_matrix(m1: Matrix, m2: Matrix, t: float):
#     if (m1.shape() != m2.shape()):
#         raise ValueError("Matrices must be of similar shape")
#     if (t < 0 or t > 1):
#         raise ValueError("t must be between 0 and 1")
#     result = m1 + (m2 - m1) * t
#     return result

if __name__ == "__main__":
    print(" ------ LERP: VECTOR TESTS ------")
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])
    print("Vectors:")
    print(vec1)
    print(vec2)
    print("Linear interpolation (t=0.5):")
    print(lerp(vec1, vec2, 0.5))
    print(" ----- ")
    print("Vectors: [-42, 42], [42, -42]")
    print("Linear interpolation (t=0.5):", lerp(Vector([-42, 42]), Vector([42, -42]), 0.5))

    print(" ------ LERP: MATRIX TESTS ------")
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6], [7, 8]])
    print("Matrices:")
    print(mat1)
    print(mat2)
    print("Linear interpolation (t=0.5):")
    print(lerp(mat1, mat2, 0.5))

    print(" ------ LERP: POINT TESTS ------")
    print("Points: 0, 1")
    print("Linear interpolation (t=0):", lerp(0, 1, 0))
    print("Linear interpolation (t=1):", lerp(0, 1, 1))
    print(" ---- ")
    print("Points: 0, 42")
    print("Linear interpolation (t=0.5):", lerp(0, 42, 0.5))
