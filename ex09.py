from Matrix import Matrix

def transpose(m: Matrix):
    res = []
    shape = m.shape()
    values = m.values
    for i in range(shape[1]):
        row = []
        for j in range(shape[0]):
            row.append(values[j][i])
        res.append(row)
    return Matrix(res)

if __name__ == "__main__":
    m: Matrix = Matrix([[1, 2, 3], [4, 5, 6]])
    print("------- TRANSPOSE ----------")
    print("Matrix:\n", m)
    print("Transpose:\n", transpose(m))