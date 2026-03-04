from Vector import Vector
from math import sqrt

def norm_1(v: Vector): # Manhattan norm
    values = v.values
    size = v.size()
    return sum(abs(values[i]) for i in range(size))

def norm(v: Vector): # Euclidian norm
    values = v.values
    size = v.size()
    return sqrt(sum(values[i] ** 2 for i in range(size)))

def norm_inf(v: Vector): # Supremum norm
    values = v.values
    size = v.size()
    return max([abs(values[i]) for i in range(size)])

if __name__ == "__main__":
    v = Vector([1, -2, 3])
    print(" ---- MANHATTAN NORM ----")
    print(f"Manhattan norm of {v} is: {norm_1(v)}")
    print(" ---- EUCLIDIAN NORM ----")
    print(f"Euclidian norm of {v} is: {norm(v)}")
    print(" ---- SUPREMUM NORM ----")
    print(f"Supremum norm of {v} is: {norm_inf(v)}")