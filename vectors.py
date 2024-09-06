import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([1, 1])
b = np.array([2, 0])
c = np.array([0, 2])

v = a + b + c

plt.grid()
plt.plot(v[0], v[1], 'o')
plt.xlim(0,5)
plt.ylim(0,5)

result = np.dot(a,b)

len_a = math.sqrt(a[0]**2 + a[1]**2)

len_b = math.sqrt(a[0]**2 + b[1]**2)

cos = result / (len_a * len_b)

print(cos)