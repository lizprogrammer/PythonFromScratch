#lists in depth

a = [1,2,3,4]
a += [4,5,7,3]
a.append(144)
print(a)

print(a[2])

print(a[:2])

a[:2] = 99,55
a[:2] = []

print(a)

a[:] = []
print(a)

a = [1,44,35,77,8]
print(a)

print(len(a))
print(max(a))
print(min(a))

my_strings = ['python', 'cython','php','php']
my_list= list('python')
print(my_list)
del(my_list[2])
print(my_list)

a.append(77)
print(a)

print(a.count(77))
print(my_strings.count('php'))

b = ['c++']
my_strings.extend(b)
print(my_strings)
print(my_strings.index('cython'))

my_strings.remove('c++')
print(my_strings)
print(my_strings.reverse())
print(my_strings)
print(my_strings.sort())
print(my_strings)