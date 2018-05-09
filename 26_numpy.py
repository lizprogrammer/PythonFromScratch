import numpy as np

a = np.array([1,2,3,4,5])
#print(a)

b = np.array([1,2,3,4,5])

c = np.array([[-3,4.9,5],[-5,6.9,7]])
d = np.array([[1,2,3],[7,8,9]])

e = c+d
#print(e)

a = np.abs(a)
#print(a)

a = np.abs(c)
#print(a,"\n")

a = np.floor(c)
#print(a,"\n")

a = np.ceil(c)
#print(a,"\n")

a = np.array([[-1,2],[2,-5],[7,5],[9,1]])
b = np.array([[2,4],[6,9]])

#print(a.shape)
#print(a.reshape(4,2))

print(np.zeros(([2,3])),"\n")
print(np.ones([2,3]),"\n")

