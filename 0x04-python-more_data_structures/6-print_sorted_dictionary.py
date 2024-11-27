#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keysSorted = sorted(list(a_dictionary))
    for i in keysSorted:
        print("{}: {}".format(i, a_dictionary[i]))
