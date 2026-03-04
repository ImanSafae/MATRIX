from __future__ import annotations

class Vector:

    values: list[float]

    def __init__(self, values: list[float]):
        self.values = values

    def size(self) -> int:
        return len(self.values)
    
    def __str__(self):
        result = "["
        for i, val in enumerate(self.values):
            if i > 0:
                result += ", "
            result += str(val)
        result += "]"
        return result
    
    def __add__(self, other):
        len_v1 = self.size()
        len_v2 = other.size()
        if (len_v1 != len_v2):
            raise ValueError("Vectors must be of the same size")
        
        result = []
        for i in range(len_v1):
            result.append(self.values[i] + other.values[i])
        return Vector(result)

    def __sub__(self, other):
        len_v1 = self.size()
        len_v2 = other.size()
        if (len_v1 != len_v2):
            raise ValueError("Vectors must be of the same size")
        
        result = []
        for i in range(len_v1):
            result.append(self.values[i] - other.values[i])
        return Vector(result)

    def __mul__(self, scalar: float):
        result = []
        size = self.size()
        for i in range(size):
            result.append(scalar * self.values[i])
        return Vector(result)
    
    def dot(self, other: Vector):
        size = self.size()
        other_size = other.size()
        if (size != other_size):
            raise ValueError("Vectors must be of the same size")
        return sum(self.values[i] * other.values[i] for i in range(size))