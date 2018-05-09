from tkinter import *
'''/
something = dir(tkinter)
print(something)
'''

#creates a blank window
root = Tk()

#Label(root,text = "This is a label").pack()
#Button(root,text = "This is a button").pack()


def abc():
    print("My name is Elizabeth")

f = Frame(root)

Label(f, text = "Hi").pack()
Button(f, text = "Hey", command = abc).pack()
f.pack()
root.mainloop()