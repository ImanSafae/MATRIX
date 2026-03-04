from Vector import Vector

def dot_product(v1: Vector, v2: Vector):
    v1_size = v1.size()
    v2_size = v2.size()
    if (v1_size != v2_size):
        raise ValueError("Vectors must be of the same size")
    return sum(v1.values[i] * v2.values[i] for i in range(v1_size))


if __name__ == "__main__":
    v1 = Vector([2, 2, 2])
    v2 = Vector([1, 5, 8])
    dot = dot_product(v1, v2)
    print(f"Dot product of {v1} and {v2} is: {dot}")