from Vector import Vector
from math import fma

def norm_1(v: Vector): # Manhattan norm
    values = v.values
    size = v.size()
    res = 0
    for i in range(size):
        value = values[i] if values[i] >= 0 else -values[i]
        res += value
    return res

def norm(v: Vector): # Euclidian norm
    values = v.values
    size = v.size()
    res = 0
    for i in range(size):
        res = fma(values[i], values[i], res)
    return pow(res, 0.5)

def norm_inf(v: Vector): # Supremum norm
    values = v.values
    size = v.size()
    res = 0
    for i in range(size):
        value = values[i] if values[i] >= 0 else -values[i]
        res = max(res, value)
    return res

if __name__ == "__main__":
    v1 = Vector([0])
    v2 = Vector([1])
    print(" ---- MANHATTAN NORM ----")
    print(f"Manhattan norm of {v} is: {norm_1(v)}")
    print(" ---- EUCLIDIAN NORM ----")
    print(f"Euclidian norm of {v} is: {norm(v)}")
    print(" ---- SUPREMUM NORM ----")
    print(f"Supremum norm of {v} is: {norm_inf(v)}")