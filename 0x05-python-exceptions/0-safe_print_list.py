#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        Y = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            Y += 1
        return x
    except IndexError:
        return Y
    finally:
        print()
