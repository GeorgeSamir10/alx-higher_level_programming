#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictN = a_dictionary.copy()
    for i in list(dictN):
        dictN[i] *= 2
    return (dictN)
