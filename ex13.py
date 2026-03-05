from Matrix import Matrix

def rank(m: Matrix):
    shape = m.shape()
    rows, cols = shape[0], shape[1]
    values = [row[:] for row in m.values]
    rank = 0
    for col in range(cols):
        pivot_row = None
        for row in range(rank, rows):
            if values[row][col] != 0:
                pivot_row = row
                break
        if pivot_row is not None:
            if pivot_row != rank:
                values[rank], values[pivot_row] = values[pivot_row], values[rank]
            pivot = values[rank][col]
            for j in range(col, cols):
                values[rank][j] /= pivot
            for row in range(rows):
                if row != rank and values[row][col] != 0:
                    factor = values[row][col]
                    for j in range(col, cols):
                        values[row][j] -= factor * values[rank][j]
            rank += 1
    return rank

if __name__ == "__main__":
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print("Matrix 1 (2x2):")
    print(m1)
    print(f"Rank: {rank(m1)}\n")
    
    m2 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    print("Matrix 2 (3x3 singular):")
    print(m2)
    print(f"Rank: {rank(m2)}\n")
    
    m3 = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print("Matrix 3 (identity 3x3):")
    print(m3)
    print(f"Rank: {rank(m3)}\n")
    
    m4 = Matrix([[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]])
    print("Matrix 4 (2x3, dependent rows):")
    print(m4)
    print(f"Rank: {rank(m4)}\n")
    
    m5 = Matrix([[0.0, 0.0], [0.0, 0.0]])
    print("Matrix 5 (zero matrix):")
    print(m5)
    print(f"Rank: {rank(m5)}")