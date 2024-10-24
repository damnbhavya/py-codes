# Single Stackplot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
area = [1, 2, 3, 4, 5]
plt.stackplot(x, area)
plt.show()

# Single Stackplot with Different Values:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
area = [2, 3, 2, 5, 4]
plt.stackplot(x, area)
plt.show()

# Multiple Stackplots
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
area1 = [2, 3, 2, 5, 4]
area2 = [2, 3, 2, 5, 4]
area3 = [2, 3, 2, 5, 4]
plt.stackplot(x, area1, area2, area3)
plt.show()

# Multiple Stackplots with Legend, Label, and Colors
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
area1 = [2, 3, 2, 5, 4]
area2 = [2, 3, 2, 5, 4]
area3 = [2, 3, 2, 5, 4]
labels = ["area1", "area2", "area3"]
plt.stackplot(x, area1, area2, area3, labels=labels, colors=["r", "g", "m"])
plt.legend(loc=2)
plt.show()

# Stackplot with Title, X/Y Labels, and Grid
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
area1 = [2, 3, 2, 5, 4]
area2 = [2, 3, 2, 5, 4]
area3 = [2, 3, 2, 5, 4]
labels = ["area1", "area2", "area3"]
plt.stackplot(x, area1, area2, area3, labels=labels, colors=["r", "g", "m"], baseline="zero")
plt.title("PYTHON")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc=2)
plt.show()

# Stackplot with Different Baseline Options
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 1
y2 = np.sin(x + 1) + 1
y3 = np.sin(x + 2) + 1
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].stackplot(x, y1, y2, y3)
axs[0, 0].set_title('Baseline: zero (default)')
axs[0, 1].stackplot(x, y1, y2, y3, baseline='sym')
axs[0, 1].set_title('Baseline: sym')
axs[1, 0].stackplot(x, y1, y2, y3, baseline='wiggle')
axs[1, 0].set_title('Baseline: wiggle')
axs[1, 1].stackplot(x, y1, y2, y3, baseline='weighted_wiggle')
axs[1, 1].set_title('Baseline: weighted_wiggle')
plt.tight_layout()
plt.show()