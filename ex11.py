from Matrix import Matrix
from math import fma

def determinant(m: Matrix):
    shape = m.shape()
    if shape[0] != shape[1]:
        raise ValueError("Matrix must be square to compute the determinant")
    
    n = shape[0]
    values = m.values
    
    if n == 1:
        return values[0][0]
    
    if n == 2:
        return fma(values[0][0], values[1][1], -values[0][1] * values[1][0])
    
    if n == 3:
        det = values[0][0] * values[1][1] * values[2][2]
        det = fma(values[0][1] * values[1][2], values[2][0], det)
        det = fma(values[0][2] * values[1][0], values[2][1], det)
        det = fma(-values[0][2] * values[1][1], values[2][0], det)
        det = fma(-values[0][1] * values[1][0], values[2][2], det)
        det = fma(-values[0][0] * values[1][2], values[2][1], det)
        return det
    
    det = 0.0
    for j in range(n):
        submatrix = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(values[i][k])
            submatrix.append(row)
        sign = 1 if j % 2 == 0 else -1
        det = fma(sign * values[0][j], determinant(Matrix(submatrix)), det)
    return det

if __name__ == "__main__":
    m1 = Matrix([[1.0]])
    print("Matrix 1x1:")
    print(m1)
    print(f"Determinant: {determinant(m1)}\n")
    
    m2 = Matrix([[0, 0], [0, 0]])
    print("Matrix 2x2:")
    print(m2)
    print(f"Determinant: {determinant(m2)}\n")

    m2_1 = Matrix([[1, 0], [0, 1]])
    print("Matrix 2x2:")
    print(m2_1)
    print(f"Determinant: {determinant(m2_1)}\n")

    
    m2_2 = Matrix([[2, 0], [0, 2]])
    print("Matrix 2x2:")
    print(m2_2)
    print(f"Determinant: {determinant(m2_2)}\n")

    
    m2_3 = Matrix([[1, 1], [1, 1]])
    print("Matrix 2x2:")
    print(m2_3)
    print(f"Determinant: {determinant(m2_3)}\n")

    
    m2_4 = Matrix([[0, 1], [1, 0]])
    print("Matrix 2x2:")
    print(m2_4)
    print(f"Determinant: {determinant(m2_4)}\n")

    m2_5 = Matrix([[1, 2], [3, 4]])
    print("Matrix 2x2:")
    print(m2_5)
    print(f"Determinant: {determinant(m2_5)}\n")

    m2_5 = Matrix([[-7, 5], [4, 6]])
    print("Matrix 2x2:")
    print(m2_5)
    print(f"Determinant: {determinant(m2_5)}\n")
    
    m3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("Matrix 3x3:")
    print(m3)
    print(f"Determinant: {determinant(m3)}\n")
    
    m4 = Matrix([[2.0, 1.0, 3.0], [1.0, 0.0, 1.0], [1.0, 2.0, 1.0]])
    print("Matrix 3x3 (non-singular):")
    print(m4)
    print(f"Determinant: {determinant(m4)}\n")
    
    m5 = Matrix([[1.0, 2.0, 3.0, 4.0], 
                 [5.0, 6.0, 7.0, 8.0], 
                 [9.0, 10.0, 11.0, 12.0], 
                 [13.0, 14.0, 15.0, 16.0]])
    print("Matrix 4x4:")
    print(m5)
    print(f"Determinant: {determinant(m5)}\n")
    
    m6 = Matrix([[2.0, 1.0, 0.0, 0.0],
                 [1.0, 2.0, 1.0, 0.0],
                 [0.0, 1.0, 2.0, 1.0],
                 [0.0, 0.0, 1.0, 2.0]])
    print("Matrix 4x4 (tridiagonal):")
    print(m6)
    print(f"Determinant: {determinant(m6)}\n")
    
    m7 = Matrix([[1.0, 2.0, 0.0, 0.0, 0.0],
                 [0.0, 1.0, 3.0, 0.0, 0.0],
                 [0.0, 0.0, 1.0, 4.0, 0.0],
                 [0.0, 0.0, 0.0, 1.0, 5.0],
                 [0.0, 0.0, 0.0, 0.0, 1.0]])
    print("Matrix 5x5 (upper triangular):")
    print(m7)
    print(f"Determinant: {determinant(m7)}")
    