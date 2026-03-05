from Matrix import Matrix

def row_echelon_form(m: Matrix):
    shape = m.shape()
    rows, cols = shape[0], shape[1]
    values = [row[:] for row in m.values]
    current_row = 0
    for col in range(cols):
        pivot_row = None
        for row in range(current_row, rows):
            if values[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is None:
            continue
        if pivot_row != current_row:
            values[current_row], values[pivot_row] = values[pivot_row], values[current_row]
        pivot = values[current_row][col]
        for row in range(current_row + 1, rows):
            if values[row][col] != 0:
                factor = values[row][col] / pivot
                for k in range(cols):
                    values[row][k] -= factor * values[current_row][k]
        current_row += 1
        if current_row >= rows:
            break
    return Matrix(values)

if __name__ == "__main__":
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print("Matrix 1:")
    print(m1)
    print("\nRow echelon form:")
    print(row_echelon_form(m1))
    
    m2 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    print("\nMatrix 2:")
    print(m2)
    print("\nRow echelon form:")
    print(row_echelon_form(m2))
    
    m3 = Matrix([[0.0, 1.0, 2.0], [1.0, 2.0, 3.0], [3.0, 2.0, 1.0]])
    print("\nMatrix 3:")
    print(m3)
    print("\nRow echelon form:")
    print(row_echelon_form(m3))
