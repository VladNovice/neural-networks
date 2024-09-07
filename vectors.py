import numpy as np
import matplotlib.pyplot as plt
import math

vector_a = np.array([1, 1, 32])
vector_b = np.array([2, 10, 132])
vector_c = np.array([2, 299, 14])

vector_sum = vector_a + vector_b + vector_c

vector_diff = vector_a - vector_b

vector_product = vector_a * vector_b

vector_division = vector_a / vector_b


v = vector_a + vector_b + vector_c

plt.grid()
plt.plot(v[0], v[1], 'o')
plt.xlim(0,5)
plt.ylim(0,5)

result = np.dot(vector_a,vector_b)

lenvector_a = math.sqrt(vector_a[0]**2 + vector_a[1]**2)

lenvector_b = math.sqrt(vector_a[0]**2 + vector_b[1]**2)

cos = result / (lenvector_a * lenvector_b)

print(cos)