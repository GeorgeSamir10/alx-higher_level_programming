#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None) or (a_dictionary == {}):
        return None
    values_Sorted = list(reversed(sorted(a_dictionary.values())))
    bestScore = values_Sorted[0]
    for i, j in a_dictionary.items():
        if j == bestScore:
            return (i)
