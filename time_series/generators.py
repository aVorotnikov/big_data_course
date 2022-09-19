import numpy as np


def sample1(n : int, h = 0.05):
    return np.array([np.sqrt(k * h) + np.random.normal() for k in range(n)])

def sample2(n : int, h = 0.1):
    return np.array([0.5 * np.sin(k * h) + np.random.normal() for k in range(n)])
