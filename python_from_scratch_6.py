#dictionaries

a = {'name':'Elizabeth','language':'Python','number':1}
print(a['name'])
print(a['language'])
a['language'] = 'cython'
print(a)
del a['number']
print(a)
a.clear()
print(a)

#del a
#print(a)
print(len(a))

a = {1: 'python',2: 'cython',3: 'java'}

print(str(a))
b=a.copy()
print(b)

print(type(a))
print(a.get(1))

print(1 in a)
print(66 in a)

del a
del b

a = [1,2,3]
b = 'python','cython','ruby'
ab = zip(a,b)
abu = dict(ab)
print(abu)

