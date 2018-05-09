import sys

c = sys.copyright
print(c)

a = sys.executable
print(a)

a = sys.getrecursionlimit()
print(a)


a = sys.getcheckinterval()
print(a)


a = sys.path
print(a)

a = sys.platform
print(a)

a = sys.version
print(a)

a = sys.platform
print('platform: ',a)


#standard functions in stdout and stderr

#sys.stdout.write("Hello world\n")
sys.stderr.write("Error!")




