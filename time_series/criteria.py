import numpy as np


def turning_points(sample: np.array):
    cnt = 0
    for i in range(1, len(sample) - 1):
        if sample[i - 1] < sample[i] and sample[i] > sample[i + 1]:
            cnt += 1
            continue
        if sample[i - 1] > sample[i] and sample[i] < sample[i + 1]:
            cnt += 1
    return cnt


def turning_points_theory(sample: np.array):
    return 2 * (len(sample) - 2) / 3, (16 * len(sample) - 29) / 90


def kendall(sample: np.array):
    p = 0
    for i in range(0, len(sample)):
        for j in range(i + 1, len(sample)):
            if sample[j] > sample[i]:
                p += 1
    return 4 * p / len(sample) / (len(sample) - 1) - 1


def kendall_theory(sample: np.array):
    return 0, 2 * (2 * len(sample) + 5) / (9 * len(sample) * (len(sample) - 1))
