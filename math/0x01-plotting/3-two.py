#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

plt.title('Exponential Decay of Radioactive Elements')
plt.xlim(0, 20000)
plt.ylim(0, 1)
line1, = plt.plot(x, y1, color="#eb473f", label="C-14", linestyle="dashed")
line2, = plt.plot(x, y2, color="#4f9720", label="Ra-226")
plt.legend((line1, line2), (line1.get_label(), line2.get_label()))
plt.show()
