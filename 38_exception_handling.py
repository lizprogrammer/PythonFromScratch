while True:
    try:
        open('z.txt', 'r'),
    except FileNotFoundError:
        print('This file is not available')

    a = 10
    try:
        nos = int(input("Please enter the number you want \n"))
        b = a / nos
        print(b)
        break

    except Exception:
        print('Something is not right')
    except TypeError:
        print('Please enter a number')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a non-zero value')
    finally:
        print('Code has finished executing')
    print('Did you get here?')

