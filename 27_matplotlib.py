import matplotlib.pyplot as plt
import numpy as np

#plt.plot(np.array([[1,2,3],[3,2,1]]))
#plt.plot(np.array([1,2,3]))

x1 = np.array([1,2,3])
y1 = np.array([4,5,6])
x2 = np.array([4,7,6])
y2 = np.array([5,6,9])

'''/
plt.plot(x1,y1,label="1")
plt.plot(x2,y2,label="2")
plt.title("This is matplotlib tutorial")

plt.scatter(x1,y1,label="1")
plt.scatter(x2,y2,label="2")
plt.title("This is matplotlib tutorial")

plt.bar(x1,y1,label="1")
plt.bar(x2,y2,label="2",color="g")
plt.title("This is matplotlib tutorial")
'''
plt.stackplot(x1,y1)
plt.title("This is matplotlib tutorial")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.legend()

plt.show()
