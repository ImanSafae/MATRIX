from Vector import Vector
from math import sqrt

def norm(v: Vector): # Euclidian norm
    values = v.values
    size = v.size()
    return sqrt(sum(values[i] ** 2 for i in range(size)))

def angle_cos(v1: Vector, v2: Vector):
    v1_size = v1.size()
    v2_size = v2.size()
    if (v1_size != v2_size):
        raise ValueError("Vectors must be of the same size")
    return v1.dot(v2) / (norm(v1) * norm(v2))


if __name__ == "__main__":
    v1 = Vector([1, 1, 1])
    v2 = Vector([1, 0, 0])
    cos_angle = angle_cos(v1, v2)
    print(f"Cosine of the angle between {v1} and {v2} is: {cos_angle}")