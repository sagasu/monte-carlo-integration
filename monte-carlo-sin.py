from scipy import random
import numpy as np
import matplotlib.pyplot as plt

# integral from 0 to pi of sin(x)

a = 0
b = np.pi
N = 1000

def integral_func(x):
    return np.sin(x)


areas = []
for i in range(N):
    xrand = np.zeros(N)

    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral = 0.0

    for i in range(N):
        integral += integral_func(xrand[i])

    answer = (b-a)/float(N)*integral
    areas.append(answer)

plt.title("Distribution of areas")
plt.hist(areas, bins = 30, ec = 'black')
plt.xlabel("Areas")
plt.show()