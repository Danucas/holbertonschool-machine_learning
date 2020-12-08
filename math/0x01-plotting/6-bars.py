#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

r = [0, 1, 2]
names = ['Farrah', 'Fred', 'Felicia']
p1 = plt.bar(
    r,
    fruit[0],
    color='red',
    width=0.5,
    label='apples'
)
p2 = plt.bar(
    r,
    fruit[1],
    bottom=fruit[0],
    color="yellow",
    width=0.5,
    label='bananas'
)
p3 = plt.bar(
    r,
    fruit[2],
    bottom=fruit[0] + fruit[1],
    color='#ff8000',
    width=0.5,
    label='oranges'
)
p4 = plt.bar(
    r,
    fruit[3],
    bottom=fruit[0] + fruit[1] + fruit[2],
    color='#ffe5b4',
    width=0.5,
    label='peaches'
)
plt.ylim(0, 80)
plt.legend(loc='upper right')
plt.xticks(r, names)
plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
plt.show()
