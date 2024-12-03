#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        y = 0
        for i in range(x):
            if type(my_list[i]) != int:
                continue
            print("{:d}".format(my_list[i]), end="")
            y += 1
        print()
        return y
    except IndexError:
        raise
