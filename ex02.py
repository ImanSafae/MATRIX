from Vector import Vector
from Matrix import Matrix

def linear_interpolation_vector(v1: Vector, v2: Vector, t: float):
    if (v1.size() != v2.size()):
        raise ValueError("Vectors must be of similar size")
    if (t < 0 or t > 1):
        raise ValueError("t must be between 0 and 1")
    result = v1 + (v2 - v1) * t
    return result

def linear_interpolation_matrix(m1: Matrix, m2: Matrix, t: float):
    if (m1.shape() != m2.shape()):
        raise ValueError("Matrices must be of similar shape")
    if (t < 0 or t > 1):
        raise ValueError("t must be between 0 and 1")
    result = m1 + (m2 - m1) * t
    return result

if __name__ == "__main__":
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])
    print("Vectors:")
    print(vec1)
    print(vec2)
    print("Linear interpolation (t=0.5):")
    print(linear_interpolation_vector(vec1, vec2, 0.5))
    
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6], [7, 8]])
    print("Matrices:")
    print(mat1)
    print(mat2)
    print("Linear interpolation (t=0.5):")
    print(linear_interpolation_matrix(mat1, mat2, 0.5))