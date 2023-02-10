import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1, 2, 3, 4,])
fig = plt.figure()
plt.plot(linear_data, '-o')

fig.savefig('line.png')