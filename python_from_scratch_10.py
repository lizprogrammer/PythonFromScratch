class a:

    c = 45

    def __init__(self,y):

        add = self.c + y
        print(add)


b = a(10)


class d:
    my_list = ['python','cython']
    my_dict = {1: 'lisp',2: 'php'}

    def __init__(self):
        if 'python' in self.my_list:
            print(self.my_list)

e = d()

