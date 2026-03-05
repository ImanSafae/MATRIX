from __future__ import annotations

class Matrix:
    values: list[list[float]]

    def __init__(self, values: list[list[float]]):
        self.values = values

    def shape(self) -> tuple[int, int]:
        return len(self.values), len(self.values[0]) if self.values else 0
    
    def __str__(self):
        result = "["
        shape = self.shape()
        height = shape[0]
        width = shape[1]
        for i in range(height):
            for j in range(width):
                result += str(self.values[i][j])
                if j < width - 1:
                    result += ", "
            if i < height - 1:
                result += "\n"
        result += "]"
        return result
    
    def __add__(self, other: Matrix):
        shape_m1 = self.shape()
        shape_m2 = other.shape()
        if (shape_m1 != shape_m2):
            raise ValueError("Matrices must be of the same shape")
        result = []
        for i in range(shape_m1[0]):
            col = []
            for j in range(shape_m1[1]):
                col.append(self.values[i][j] + other.values[i][j])
            result.append(col)
        return Matrix(result)

    def __sub__(self, other: Matrix):
        shape_m1 = self.shape()
        shape_m2 = other.shape()
        if (shape_m1 != shape_m2):
            raise ValueError("Matrices must be of the same shape")
        result = []
        for i in range(shape_m1[0]):
            col = []
            for j in range(shape_m1[1]):
                col.append(self.values[i][j] - other.values[i][j])
            result.append(col)
        return Matrix(result)

    def __mul__(self, scalar: float):
        result = []
        shape = self.shape()
        for i in range(shape[0]):
            col = []
            for j in range(shape[1]):
                col.append(scalar * self.values[i][j])
            result.append(col)
        return Matrix(result)
    


