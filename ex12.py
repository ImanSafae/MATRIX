from Matrix import Matrix
from math import fma

def inverse(m: Matrix):
    shape = m.shape()
    if shape[0] != shape[1]:
        raise ValueError("Matrix must be square to compute the inverse")
    n = shape[0]
    augmented = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(m.values)]
    for i in range(n):
        pivot_row = None
        for row in range(i, n):
            if augmented[row][i] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            raise ValueError("Matrix is singular and cannot be inverted")
        if pivot_row != i:
            augmented[i], augmented[pivot_row] = augmented[pivot_row], augmented[i]
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot
        for row in range(n):
            if row != i and augmented[row][i] != 0:
                factor = augmented[row][i]
                for j in range(2 * n):
                    augmented[row][j] = fma(-factor, augmented[i][j], augmented[row][j])
    inverse_values = [row[n:] for row in augmented]
    return Matrix(inverse_values)

if __name__ == "__main__":
    m1 = Matrix([[1, 0], [0, 1]])
    print("Matrix 1:")
    print(m1)
    print("\nInverse:")
    print(inverse(m1))
    
    m2 = Matrix([[2, 0], [0, 2]])
    print("\nMatrix 2:")
    print(m2)
    try:
        print("\nInverse:")
        print(inverse(m2))
    except ValueError as e:
        print(f"Error: {e}")
    
    m3 = Matrix([[0.5, 0], [0, 0.5]])
    print("\nMatrix 3:")
    print(m3)
    print("\nInverse:")
    print(inverse(m3))

    m4 = Matrix([[0, 1], [1, 0]])
    print("\nMatrix 4:")
    print(m4)
    print("\nInverse:")
    print(inverse(m4))

    m5 = Matrix([[1,2], [3, 4]])
    print("\nMatrix 5:")
    print(m5)
    print("\nInverse:")
    print(inverse(m5))

    m6 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("\nMatrix 6:")
    print(m6)
    print("\nInverse:")
    print(inverse(m6))