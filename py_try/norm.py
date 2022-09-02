import numpy as np
import math as m


def norm_2(vec : np.array):
    res = 0
    for num in vec:
        res += num * num
    return np.sqrt(res)


def norm_p(vec : np.array, p: int):
    res = 0
    for num in vec:
        res += num ** p
    return m.pow(res, 1 / p)


def norm_weighted(vec : np.array, weights : np.array, eps = 1e-9):
    if weights.size != vec.size:
        raise ArithmeticError("Incorrect weights size")
    sum = 0
    for weight in weights:
        if weight < 0:
            raise ArithmeticError("Weight less than 0")
        sum += weight
    if abs(sum - 1) > eps:
        raise ArithmeticError("Weights sum is not 1")
    res = 0
    for i in range(0, vec.size):
        res += weights[i] * abs(vec[i])
    return res
