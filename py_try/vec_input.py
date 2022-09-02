import numpy as np


def read_vec(dim: int):
    res = np.zeros(dim)
    for i in range(0, dim):
        res[i] = float(input("Insert coordinate #{}: ".format(i + 1)))
    return res
