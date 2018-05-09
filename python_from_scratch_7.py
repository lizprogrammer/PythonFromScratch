# functions

'''\
def addition(x,y):
    z = x + y
    print(z)

print(addition(10,20))


def func(x,y):
    print(x,y)

func('python',"Liz")

'''


# tuples and dictionaries can be used
# as parameters


def func(*x, **y):
    print(x, y)


func('python', name="Liz")


def write():
    print("My name is Liz!")


write()

write()
write()
write()


def dollars_to_inr(dollars=int(input("Enter the number of dollars: "))):
    inr = 64.08
    while inr is 64.08:
        inr *= dollars
        print("The current rate of inr w.r.t. dollars is", inr)
        break


dollars_to_inr()
