from __future__ import annotations
from math import fma

from Vector import Vector

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
    
    def determinant(self):
        shape = self.shape()
        if shape[0] != shape[1]:
            raise ValueError("Matrix must be square to compute the determinant")
        
        n = shape[0]
        values = self.values
        
        if n == 1:
            return values[0][0]
        
        if n == 2:
            return values[0][0] * values[1][1] - values[0][1] * values[1][0]
        
        if n == 3:
            return (values[0][0] * values[1][1] * values[2][2] +
                    values[0][1] * values[1][2] * values[2][0] +
                    values[0][2] * values[1][0] * values[2][1] -
                    values[0][2] * values[1][1] * values[2][0] -
                    values[0][1] * values[1][0] * values[2][2] -
                    values[0][0] * values[1][2] * values[2][1])
        
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
            det += sign * values[0][j] * self.determinant(Matrix(submatrix))
        return det

    def row_echelon_form(self):
        shape = self.shape()
        rows, cols = shape[0], shape[1]
        values = [row[:] for row in self.values]
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
    
    def transpose(self):
        res = []
        shape = self.shape()
        values = self.values
        for i in range(shape[1]):
            row = []
            for j in range(shape[0]):
                row.append(values[j][i])
            res.append(row)
        return Matrix(res)

    def trace(self):
        shape = self.shape()
        if shape[0] != shape[1]:
            raise ValueError("Provided matrix must be squared in order to compute its trace")
        res = 0
        for i in range(shape[0]):
            res += self.values[i][i]
        return res
    
    def mul_vec(self, v: Vector):
        m_shape = self.shape()
        v_size = v.size()
        if v_size != m_shape[1]:
            raise ValueError("The number of columns in the matrix must match the size of the vector")
        v_values = v.values
        m_values = self.values
        coordinates = []
        for j in range(m_shape[0]):
            coordinate = 0
            for i in range(v_size):
                coordinate = fma(v_values[i], m_values[j][i], coordinate)
            coordinates.append(coordinate)
        return Vector(coordinates)

    def mul_mat(self, other: Matrix):
        m1_shape = self.shape()
        m2_shape = other.shape()
        if m1_shape[1] != m2_shape[0]:
            raise ValueError("The number of columns in the first matrix must match the number of rows in the second matrix")
        m1_values = self.values
        m2_values = other.values
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
