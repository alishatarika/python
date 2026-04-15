import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,8])
y=np.array([0,250])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x,y)
plt.show()

plt.plot(x,y,'o')
plt.show()


x1=np.array([2,3,4,5,7])
y1=np.array([5,7,8,3,6])
plt.plot(x1,y1)
plt.show()


ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints,marker='o')
plt.show()


x2 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y2 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x2, y2)
plt.show()