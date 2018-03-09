import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')
plt.show()