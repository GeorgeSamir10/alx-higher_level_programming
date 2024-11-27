#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_N = my_list.copy()
    for i in range(len(list_N)):
        if (list_N[i] == search):
            list_N[i] = replace
    return list_N
