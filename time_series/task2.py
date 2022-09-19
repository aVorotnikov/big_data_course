import numpy as np
import matplotlib.pyplot as plt
import csv
from math import sqrt
from criteria import *

from generators import *
from trends import *


n = 1000
x = np.arange(n)
y = sample2(n)
y_trend = sample2_trend(n)

ema_params = [0.01, 0.05, 0.1, 0.3]
emas = [EMA(y, param) for param in ema_params]

fig1, axs1 = plt.subplots(2, 2)
axs1_list = [axs1[0, 0], axs1[0, 1], axs1[1, 0], axs1[1, 1]]
for param, ema, ax in zip(ema_params, emas, axs1_list):
    ax.plot(x, y, 'b')
    ax.plot(x, y_trend, 'k--')
    ax.plot(x, ema, 'r')
    ax.grid(True)
    ax.set_title(f'EMA, alpha={param}')
plt.show()
# plt.savefig('images/ema_trends.png')

fig2, axs2 = plt.subplots(2, 2)
axs2_list = [axs2[0, 0], axs2[0, 1], axs2[1, 0], axs2[1, 1]]
for param, ema, ax in zip(ema_params, emas, axs2_list):
    ax.plot(x, ema - y, 'r')
    ax.grid(True)
    ax.set_title(f'remainder - EMA, width={param}')
plt.show()
# plt.savefig('images/ema_remainders.png')

with open('data/ema.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Turning points', 'Turning points (theory)', 'Turning points (3 sigma interval)', 'Turning points - entry',
        'Kendall', 'Kendall (theory)', 'Kendall (3 sigma interval)', 'Kendall - entry'])
    for ema in emas:
        remainder = ema - y
        tp_value = turning_points(remainder)
        tp_e, tp_d = turning_points_theory(remainder)
        tp_a = tp_e - 3 * sqrt(tp_d)
        tp_b = tp_e + 3 * sqrt(tp_d)
        kendall_value = kendall(remainder)
        kendall_e, kendall_d = kendall_theory(remainder)
        kendall_a = kendall_e - 3 * sqrt(kendall_d)
        kendall_b = kendall_e + 3 * sqrt(kendall_d)
        writer.writerow([
            tp_value,
            tp_e,
            f'[{tp_a}; {tp_b}]',
            tp_a < tp_value and tp_value < tp_b,
            kendall_value,
            kendall_e,
            f'[{kendall_a}; {kendall_b}]',
            kendall_a < kendall_value and kendall_value < kendall_b])
