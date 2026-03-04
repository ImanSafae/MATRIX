from Vector import Vector
from math import fma

def scale_vector(v: Vector, scalar: float):
    result = []
    size = v.size()
    for i in range(size):
        result.append(scalar * v.values[i])
    return Vector(result)

def linear_combination(vectors: list[Vector], scalars: list[float]):
    nb_vectors = len(vectors)
    nb_scalars = len(scalars)
    vector_size = vectors[0].size()
    if nb_vectors != nb_scalars:
        raise ValueError("Vectors and scalars lists must be of similar size")
    result = scale_vector(vectors[0], scalars[0])
    for i in range(1, nb_vectors):
        for j in range(vector_size):
            result.values[j] = fma(scalars[i], vectors[i].values[j], result.values[j])
    return result

if __name__ == "__main__":
    scalars = [2, 2, 2]
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])
    vec3 = Vector([7, 8, 9])
    vectors = [vec1, vec2, vec3]
    print("Vectors:")
    for v in vectors:
        print(v)
    print("Scalars:")
    print(scalars)
    print("Linear combination:")
    print(linear_combination(vectors, scalars))