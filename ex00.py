from Vector import Vector
from Matrix import Matrix

def add_vectors(v1: Vector, v2: Vector):
    len_v1 = v1.size()
    len_v2 = v2.size()
    if (len_v1 != len_v2):
        raise ValueError("Vectors must be of the same size")
    
    result = []
    for i in range(len_v1):
        result.append(v1.values[i] + v2.values[i])
    return Vector(result)


def add_matrices(m1: Matrix, m2: Matrix):
    shape_m1 = m1.shape()
    shape_m2 = m2.shape()
    if (shape_m1 != shape_m2):
        raise ValueError("Matrices must be of the same shape")
    result = []
    for i in range(shape_m1[0]):
        col = []
        for j in range(shape_m1[1]):
            col.append(m1.values[i][j] + m2.values[i][j])
        result.append(col)
    return Matrix(result)

def substract_vectors(v1: Vector, v2: Vector):
    len_v1 = v1.size()
    len_v2 = v2.size()
    if (len_v1 != len_v2):
        raise ValueError("Vectors must be of the same size")
    
    result = []
    for i in range(len_v1):
        result.append(v1.values[i] - v2.values[i])
    return Vector(result)

def substract_matrices(m1: Matrix, m2: Matrix):
    shape_m1 = m1.shape()
    shape_m2 = m2.shape()
    if (shape_m1 != shape_m2):
        raise ValueError("Matrices must be of the same shape")
    result = []
    for i in range(shape_m1[0]):
        col = []
        for j in range(shape_m1[1]):
            col.append(m1.values[i][j] - m2.values[i][j])
        result.append(col)
    return Matrix(result)

def scale_vector(v: Vector, scalar: float):
    result = []
    size = v.size()
    for i in range(size):
        result.append(scalar * v.values[i])
    return Vector(result)

def scale_matrix(m: Matrix, scalar: float):
    result = []
    shape = m.shape()
    for i in range(shape[0]):
        col = []
        for j in range(shape[1]):
            col.append(scalar * m.values[i][j])
        result.append(col)
    return Matrix(result)

if __name__ == "__main__":
    scalar = 3
    vec0 = Vector([0, 1])
    vec1 = Vector([0, 0])
    vec2 = Vector([1, 0])
    vec3 = Vector([1, 1])
    vec4 = Vector([2, 2])
    vec5 = Vector([21, 21])
    vec6 = Vector([42, 42])
    vec7 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    vec8 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    matrix = Matrix([[0, 0], [0, 0]])
    matrix1 = Matrix([[1, 0], [0, 1]])
    matrix2 = Matrix([[1, 1], [1, 1]])
    matrix3 = Matrix([[21, 21], [21, 21]])

    print(" --- VECTOR SCALING ---")
    scaled_vec = scale_vector(vec1, 1)
    print("Original Vector:")
    print(vec1)
    print("Scaled Vector by " + str(1) + ":")
    print(scaled_vec)
    print(' ---- ')
    scaled_vec = scale_vector(vec2, 1)
    print("Original Vector:")
    print(vec2)
    print("Scaled Vector by " + str(1) + ":")
    print(scaled_vec)
    print(' ---- ')
    scaled_vec = scale_vector(vec3, 2)
    print("Original Vector:")
    print(vec3)
    print("Scaled Vector by " + str(2) + ":")
    print(scaled_vec)
    print(' ---- ')
    scaled_vec = scale_vector(vec5, 2)
    print("Original Vector:")
    print(vec5)
    print("Scaled Vector by " + str(2) + ":")
    print(scaled_vec)
    print(' ---- ')
    scaled_vec = scale_vector(vec6, 0.5)
    print("Original Vector:")
    print(vec6)
    print("Scaled Vector by " + str(0.5) + ":")
    print(scaled_vec)

    print("\n")
    print(" --- MATRIX SCALING ---")
    scaled_matrix = scale_matrix(matrix, scalar)
    print("Original Matrix:")
    print(matrix)
    print("Scaled Matrix by " + str(scalar) + ":")
    print(scaled_matrix)

    print("\n")
    print(" --- VECTOR ADDITION ---")
    print("Vector 1:")
    print(vec1)
    print("Vector 2:")
    print(vec1)
    try:
        sum_vec = add_vectors(vec1, vec1)
        print("Sum of vectors:")
        print(sum_vec)
    except ValueError as e:
        print(e)

    print("\n")
    print(" --- MATRIX ADDITION ---")
    matrix2 = Matrix([[5, 7], [6, 8]])
    print("Matrix 1:")
    print(matrix)
    print("Matrix 2:")
    print(matrix2)
    try:
        sum_matrix = add_matrices(matrix, matrix2)
        print("Sum of matrices:")
        print(sum_matrix)
    except ValueError as e:
        print(e)

    print("\n")
    print(" --- VECTOR SUBSTRACTION ---")
    vec3 = Vector([7, 8, 9])
    print("Vector 1:")
    print(vec3)
    print("Vector 2:")
    print(vec2)
    try:
        diff_vec = substract_vectors(vec3, vec2)
        print("Difference of vectors:")
        print(diff_vec)
    except ValueError as e:
        print(e)

    print("\n")
    print(" --- MATRIX SUBSTRACTION ---")
    matrix3 = Matrix([[9, 11], [10, 12]])
    print("Matrix 1:")
    print(matrix3)
    print("Matrix 2:")
    print(matrix2)
    try:
        diff_matrix = substract_matrices(matrix3, matrix2)
        print("Difference of matrices:")
        print(diff_matrix)
    except ValueError as e:
        print(e)