from Vector import Vector
from math import fma

def dot_product(v1: Vector, v2: Vector):
    v1_size = v1.size()
    v2_size = v2.size()
    if (v1_size != v2_size):
        raise ValueError("Vectors must be of the same size")
    res = 0
    for i in range(v1_size):
        res = fma(v1.values[i], v2.values[i], res)
    return res


if __name__ == "__main__":
    v1 = Vector([0, 0])
    v2 = Vector([1, 0])
    v3 = Vector([0, 1])
    v4 = Vector([1, 1])
    v5 = Vector([4, 2])
    v6 = Vector([2, 1])
    dot = dot_product(v1, v1)
    print(f"Dot product of {v1} and {v1} is: {dot}")
    print(f"Dot product of {v2} and {v1} is: {dot_product(v2, v1)}")
    print(f"Dot product of {v2} and {v2} is: {dot_product(v2, v2)}")
    print(f"Dot product of {v2} and {v3} is: {dot_product(v2, v3)}")
    print(f"Dot product of {v4} and {v4} is: {dot_product(v4, v4)}")
    print(f"Dot product of {v5} and {v6} is: {dot_product(v5, v6)}")