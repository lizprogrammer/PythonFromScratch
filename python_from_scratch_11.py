#inheritence

class parent():
    def __init__(self):
        print('This is the parent class constructor')
    def f1(self):
        print('This is the parent class function')

class child(parent):
    def __init__(self):
        print('This is the child class constructor')
    def f2(self):
        print('This is the child class function')

c = child()
p = parent()
c.f2()
c.f1()

#Multiple inheritence

class mc_learning():
    def f1(self):
        print('\nThis is machine learning')

class web_dev():
    def __init__(self):
        print('Constructor web_dev')
    def f2(self):
        print('\nFlask and Django are Python web frameworks')

class python(mc_learning,web_dev):
    pass

p = python()
p.f1()
p.f2()


