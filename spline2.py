import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt("/home/arne/spline2.dat")
x = data[:, 0]
y = data[:, 1]

s = set()
for x,y in data:
    s.add((x,y))
print(len(s), len(data))
assert(len(s) == len(data))


fig, ax = plt.subplots()
plt.plot(x, y, "x")



radius = 50

plt.xlim(-radius-2,radius+2)
plt.ylim(-radius-2,radius+2)

for (x,y) in data:
    rect = plt.Rectangle((x,y), 1, 1)
    ax.add_artist(rect)


circle1 = plt.Circle((0, 0), radius, clip_on=False, fill=False)
ax.add_artist(circle1)

plt.show()