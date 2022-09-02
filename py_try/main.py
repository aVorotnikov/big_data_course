import numpy as np
from norm import *
from factorial import *
from vec_input import *

x = np.arange(-10, 6)
print("x: ", x)
y = np.arange(-5, 11)
print("y: ", y)

z = np.zeros(2 * min(x.size // 2, y.size // 2) + y.size % 2)
for i in range(0, z.size // 2):
    z[2 * i] = y[2 * i]
    z[2 * i + 1] = x[2 * i + 1]
if y.size >= z.size:
    z[z.size - 1] = y[z.size - 1]
print("z unsorted: ", z)
z.sort()
print("z sorted: ", z)

if x.size != y.size or x.size != z.size or y.size != z.size:
    raise ArithmeticError("Incorrerct dimensions")

p = int(input("Input p for norm: "))
print("Input weights for norm: ")
weights = read_vec(x.size)
norms = {
    "euclidean": norm_2,
    "p": lambda vec: norm_p(vec, p),
    "weighted": lambda vec: norm_weighted(vec, weights)
}
vectors = {
    "x": z,
    "y": y,
    "z": z
}
for vec in vectors.items():
    for norm in norms.items():
        try:
            print("{} norm of {} vector: {}".format(norm[0], vec[0], norm[1](vec[1])))
        except ArithmeticError as error:
            print("Error while evaluatin norm: {}".format(error))

n = int(input("Input a number for factorial: "))
print("{}!: {}".format(n, factorial(n)))

print("Input 5 dimensional vector")
vec = read_vec(5)
print("max coordinate: ", vec.max())
print("min coordinate: ", vec.min())
print("sum of coordinates: ", vec.sum())
