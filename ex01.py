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
    vec1 = Vector([-42, 42])
    vec2 = Vector([-42])
    vec3 = Vector([1, 3])
    vec4 = Vector([10, 20])
    vec5 = Vector([-42, 100, -69.5])
    vec6 = Vector([1, 3, 5])
    print("Linear combination of " + str(vec1) + " with -1:", linear_combination([vec1], [-1]))
    print("Linear combination of " + str(vec2) + ", " + str(vec2) + " , " + str(vec2) + " with [-1, 1, 0]:", linear_combination([vec2, vec2, vec2], [-1, 1, 0]))
    print("Linear combination of " + str(vec1) + ", " + str(vec3) + " , " + str(vec4) + " with [1, -10, -1]:", linear_combination([vec1, vec3, vec4], [1, -10, -1]))
    
    