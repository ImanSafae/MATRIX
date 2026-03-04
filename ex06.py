from Vector import Vector
from math import fma

def cross_product(v1: Vector, v2: Vector):
    size_v1 = v1.size()
    size_v2 = v2.size()
    if (size_v1 != 3) or (size_v2 != 3):
        raise ValueError("Both vectors must be 3-dimensional")
    v1_values = v1.values
    v2_values = v2.values
    # x1 = (v1_values[1] * v2_values[2]) - (v1_values[2] * v2_values[1])
    # x2 = (v1_values[2] * v2_values[0]) - (v1_values[0] * v2_values[2])
    # x3 = (v1_values[0] * v2_values[1]) - (v1_values[1] * v2_values[0])
    x1 = fma(v1_values[1], v2_values[2], fma(v2_values[1], -v1_values[2], 0))
    x2 = fma(v1_values[2], v2_values[0], fma(v2_values[2], -v1_values[0], 0))
    x3 = fma(v1_values[0], v2_values[1], fma(v2_values[0], -v1_values[1], 0))
    result = Vector([x1, x2, x3])
    return result

if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = cross_product(v1, v2)
    print(' ------ CROSS PRODUCT ------ ')
    print(f"v1: {v1.values}")  # Output: [1, 2, 3]
    print(f"v2: {v2.values}")  # Output: [4, 5, 6]
    print(f"result: {result.values}")  # Output: [-3, 6, -3]
