#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictTotup = list(a_dictionary.items())
    if (value in a_dictionary.values()):
        for i in range(len(dictTotup)):
            if (dictTotup[i][1] == value):
                del a_dictionary[dictTotup[i][0]]
    return (a_dictionary)
