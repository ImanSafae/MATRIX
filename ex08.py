from Matrix import Matrix

def trace(m: Matrix):
    shape = m.shape()
    if shape[0] != shape[1]:
        raise ValueError("Provided matrix must be squared in order to compute its trace")
    res = 0
    for i in range(shape[0]):
        res += m.values[i][i]
    return res

if __name__ == "__main__":
    m: Matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("------- TRACE ----------")
    print("Matrix:\n", m)
    print("Trace:", trace(m))