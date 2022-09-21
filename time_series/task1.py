import numpy as np
import matplotlib.pyplot as plt
import csv
from math import sqrt
from criteria import *

from generators import *
from trends import *


n = 1000
x = np.arange(n)
y = sample1(n)
y_trend = sample1_trend(n)

sma_params = [21, 51, 111]
smas = [SMA(y, param) for param in sma_params]
sma_args = [np.linspace(param // 2, n - param // 2, n - param + 1) for param in sma_params]
sma_colors = ['r', 'g', 'b']

fig1, ax1 = plt.subplots()
line_disrib1 = ax1.plot(x, y, 'm', label='sqrt(h*k) + N(0, 1)')
line_trend1 = ax1.plot(x, y_trend, 'k--', label='sqrt(h*k)')
sma_lines = [ax1.plot(args, sma, color, label=f'SMA, width={param}')
    for param, sma, args, color in zip(sma_params, smas, sma_args, sma_colors)]
plt.legend()
plt.grid(True)
plt.show()
# plt.savefig('images/sma_trends.png')

fig1a, ax1a = plt.subplots()
trend_lines = [ax1a.plot(args, sma - y[(param // 2):-(param // 2)], color, label=f'remainder - SMA, width={param}')
    for param, sma, args, color in zip(sma_params, smas, sma_args, sma_colors)]
plt.legend()
plt.grid(True)
plt.show()
# plt.savefig('images/sma_remainders.png')

with open('data/sma.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Width',
        'Turning points', 'Turning points (theory)', 'Turning points (3 sigma interval)', 'Turning points - entry',
        'Kendall', 'Kendall (theory)', 'Kendall (3 sigma interval)', 'Kendall - entry'])
    for sma, param in zip(smas, sma_params):
        remainder = sma - y[(param // 2):-(param // 2)]
        tp_value = turning_points(remainder)
        tp_e, tp_d = turning_points_theory(remainder)
        tp_a = tp_e - 3 * sqrt(tp_d)
        tp_b = tp_e + 3 * sqrt(tp_d)
        kendall_value = kendall(remainder)
        kendall_e, kendall_d = kendall_theory(remainder)
        kendall_a = kendall_e - 3 * sqrt(kendall_d)
        kendall_b = kendall_e + 3 * sqrt(kendall_d)
        writer.writerow([
            param,
            tp_value,
            tp_e,
            f'[{tp_a}; {tp_b}]',
            tp_a < tp_value and tp_value < tp_b,
            kendall_value,
            kendall_e,
            f'[{kendall_a}; {kendall_b}]',
            kendall_a < kendall_value and kendall_value < kendall_b])

smm_params = [21, 51, 111]
smms = [SMM(y, param) for param in smm_params]
smm_args = [np.linspace(param // 2, n - param // 2, n - param + 1) for param in smm_params]
smm_colors = ['r', 'g', 'b']

fig2, ax2 = plt.subplots()
line_disrib2 = ax2.plot(x, y, 'm', label='sqrt(h*k) + N(0, 1)')
line_trend2 = ax2.plot(x, y_trend, 'k--', label='sqrt(h*k)')
smm_lines = [ax2.plot(args, smm, color, label=f'SMM, width={param}')
    for param, smm, args, color in zip(smm_params, smms, smm_args, smm_colors)]
plt.legend()
plt.grid(True)
plt.show()
# plt.savefig('images/smm_trends.png')

fig2a, ax2a = plt.subplots()
trend_lines = [ax2a.plot(args, smm - y[(param // 2):-(param // 2)], color, label=f'trend - SMM, width={param}')
    for param, smm, args, color in zip(smm_params, smms, smm_args, smm_colors)]
plt.legend()
plt.grid(True)
plt.show()
# plt.savefig('images/smm_remainders.png')

with open('data/smm.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Width',
        'Turning points', 'Turning points (theory)', 'Turning points (3 sigma interval)', 'Turning points - entry',
        'Kendall', 'Kendall (theory)', 'Kendall (3 sigma interval)', 'Kendall - entry'])
    for smm, param in zip(smms, smm_params):
        remainder = smm - y[(param // 2):-(param // 2)]
        tp_value = turning_points(remainder)
        tp_e, tp_d = turning_points_theory(remainder)
        tp_a = tp_e - 3 * sqrt(tp_d)
        tp_b = tp_e + 3 * sqrt(tp_d)
        kendall_value = kendall(remainder)
        kendall_e, kendall_d = kendall_theory(remainder)
        kendall_a = kendall_e - 3 * sqrt(kendall_d)
        kendall_b = kendall_e + 3 * sqrt(kendall_d)
        writer.writerow([
            param,
            tp_value,
            tp_e,
            f'[{tp_a}; {tp_b}]',
            tp_a < tp_value and tp_value < tp_b,
            kendall_value,
            kendall_e,
            f'[{kendall_a}; {kendall_b}]',
            kendall_a < kendall_value and kendall_value < kendall_b])
