from Matrix import Matrix
from Vector import Vector
from math import fma

def mul_vec(m: Matrix, v: Vector):
    m_shape = m.shape()
    v_size = v.size()
    if v_size != m_shape[1]:
        raise ValueError("The number of columns in the matrix must match the size of the vector")
    v_values = v.values
    m_values = m.values
    coordinates = []
    for j in range(m_shape[0]):
        coordinate = 0
        for i in range(v_size):
            coordinate = fma(v_values[i], m_values[j][i], coordinate)
        coordinates.append(coordinate)
    return Vector(coordinates)

def mul_mat(m1: Matrix, m2: Matrix):
    m1_shape = m1.shape()
    m2_shape = m2.shape()
    if m1_shape[1] != m2_shape[0]:
        raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix")
    m1_values = m1.values
    m2_values = m2.values

    result = []
    for i in range(m1_shape[0]):
        row = []
        for j in range(m2_shape[1]):
            coordinate = 0
            for k in range(m1_shape[1]):
                coordinate = fma(m1_values[i][k], m2_values[k][j], coordinate)
            row.append(coordinate)
        result.append(row)
    return Matrix(result)

if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[7, 8], [9, 10], [11, 12]])
    v = Vector([1, 2, 3])
    result_vec = mul_vec(m1, v)
    result_mat = mul_mat(m1, m2)
    print(' ------ MATRIX-VECTOR MULTIPLICATION ------ ')
    print(f"M1:\n{m1}")  
    print(f"v: {v.values}")  
    print(f"RESULT:\n{result_vec.values}")  
    print(' ------ MATRIX-MATRIX MULTIPLICATION ------ ')
    print(f"M1:\n{m1}")  
    print(f"M2:\n{m2}")  
    print(f"RESULT:\n{result_mat}")