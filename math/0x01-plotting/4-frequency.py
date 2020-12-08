#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.title('Project A')
plt.xlabel('Grades')
plt.xlabel('Number of students')
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.hist(
    student_grades,
    range=(0, 100),
    bins=10,
    edgecolor='black',
    linewidth=1
)
plt.show()