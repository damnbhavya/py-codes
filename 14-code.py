import numpy as np
import matplotlib.pyplot as plt
# Generate sample data
x = np.random.randn(10000)
y = np.random.randn(10000)
# Create hexbin plot
plt.hexbin(x, y, gridsize=30, cmap='')
# Add color bar to show the count in each hexagon
plt.colorbar(label='Count')
# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Hexagonal Bin Plot')
plt.show()