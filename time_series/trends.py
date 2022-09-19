import numpy as np


def SMA(sample: np.array, width):
    if len(sample) < width:
        raise RuntimeError(f'Sample is too small for {width} width')
    sum = 0
    for i in range(width):
        sum += sample[i]
    res = np.zeros(len(sample) - width + 1)
    res[0] = sum / width
    for j in range(1, len(res)):
        sum -= sample[j - 1]
        sum += sample[j + width - 1]
        res[j] = sum / width
    return res


def SMM(sample: np.array, width):
    if len(sample) < width:
        raise RuntimeError(f'Sample is too small for {width} width')
    res = np.zeros(len(sample) - width + 1)
    for j in range(0, len(res)):
        part = sample[j:j+width]
        part = part.copy()
        part.sort()
        res[j] = part[(width + 1) // 2]
    return res
