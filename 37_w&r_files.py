def writing():
    with open('jkl.txt', 'w') as fw:
        fw.write('I love python\n')
        fw.write('I love JavaScript')


def reading():
    with open('jkl.txt', 'r') as rw:
        print(rw.read())


reading()

