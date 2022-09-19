import numpy as np
import matplotlib.pyplot as plt

from generators import *
from trends import *


n = 1000
x = np.arange(n)
y = sample1(n)

sma_params = [21, 51, 111]
smas = [SMA(y, param) for param in sma_params]
sma_args = [np.linspace(param / 2, n - param / 2, n - param + 1) for param in sma_params]
sma_colors = ['r', 'g', 'b']

fig1, ax1 = plt.subplots()
line_disrib = ax1.plot(x, y, 'm', label='sqrt(h*k) + N(0, 1)')
sma_lines = [ax1.plot(args, sma, color, label=f'SMA, width={param}')
    for param, sma, args, color in zip(sma_params, smas, sma_args, sma_colors)]
plt.legend()
plt.grid(True)
plt.show()

smm_params = [21, 51, 111]
smms = [SMM(y, param) for param in smm_params]
smm_args = [np.linspace(param / 2, n - param / 2, n - param + 1) for param in smm_params]
smm_colors = ['r', 'g', 'b']

fig2, ax2 = plt.subplots()
line_disrib = ax2.plot(x, y, 'm', label='sqrt(h*k) + N(0, 1)')
smm_lines = [ax2.plot(args, smm, color, label=f'SMM, width={param}')
    for param, smm, args, color in zip(smm_params, smms, smm_args, smm_colors)]
plt.legend()
plt.grid(True)
plt.show()

# z = sample2(n)
# line2 = ax.plot(x, z, 'g', label='0.5*sin(h*k) + N(0, 1)')
