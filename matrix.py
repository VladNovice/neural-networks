import numpy as np

A = np.array([[1, 2 ,3], [4, 5, 6]]) # [[1 2 3] [4 5 6]

B = np.array([[1, 1 ,1], [2, 2, 2]]) # [[0 1 2] [2 3 4]] (A - B)


mA1 = np.array([[1, 2], [5, 6]])

mA2 = np.array([[1, 1], [2, 2]])



res = mA1.dot(mA2)
print(res)


mA1_inv = np.linalg.inv(mA1)
print(mA1_inv) 