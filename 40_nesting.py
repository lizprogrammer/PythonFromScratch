lang = input("Enter your specialized language \n")

if lang == "python" or lang == "c++":
    print("You can continue ")
    fields = input("Enter your field \n")
    if fields == "data science" or fields == "web development" or fields == "graphics":
        print("You are definitely eligible")
        expe = input("Enter how many years of experience that you have: \n ")
        exper = int(expe)
        if exper >= 1:
            print("Great!  Even better")
        else:
            print("Better luck next time")
    else:
        print("This place ain't for you")
else:
    print("You are not eligible")