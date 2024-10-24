import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data = [np.random.normal(0, 1, 100),
    np.random.normal(1, 2, 100),
    np.random.normal(2, 0.5, 100)]

plt.boxplot(data,
        notch=True,
        patch_artist=True,
        boxprops=dict(facecolor='lightblue'),
        medianprops=dict(color='red', linewidth=2),
        whiskerprops=dict(color='green', linewidth=1.5),
        capprops=dict(color='yellow', linewidth=1.5),
        flierprops=dict(marker='o', color='orange', markersize=8))

plt.title('Customized Boxplot in Matplotlib')
plt.xlabel('Data Sets')
plt.ylabel('Values')
plt.show()
