import numpy as np
np1 = np.array([-3, -2, -1, 0, 1, 2, 3])
print(f"np1: {np1}")

# print(np.sqrt(np1))
# print(np.absolute(np1))
# print(np.exp(np1))
# print(np.min(np1))
# print(np.max(np1))
# print(np.sign(np1))
# print(np.sin(np1)) #same with cos, tan, arcsin, arccos, arctan
# print(np.log(np1))

np2 = np1.view()
np1[0] = 100
print(f"np1: {np1}")
print(f"np2: {np2}")

np3 = np1.copy()
np1[0] = -3
print(f"np1: {np1}")
print(f"np3: {np3}")