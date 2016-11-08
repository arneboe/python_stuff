import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("/home/arne/spline.dat")
x = data[:, 0]
y = data[:, 1]
yd = []
ydd = np.array(len(x))


for i in range(len(x)-1):
    yd.append((y[i+1] - y[i]) / (x[i+1] - x[i]))
yd.append(0)

print(yd)

yd = np.asarray(yd)
fig, ax = plt.subplots()

plt.xlim(-2,2)
plt.ylim(-2,2)

circle1 = plt.Circle((1, 0), 1, clip_on=False, fill=False)
plt.plot(x, y, color="r", label="test")
plt.plot(x, yd, color="g")
ax.add_artist(circle1)
plt.show()

