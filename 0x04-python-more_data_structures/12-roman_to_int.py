#!/usr/bin/python3
def roman_to_int(roman_string):
    dictRoman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

    if (roman_string is None) or (roman_string == ""):
        return (0)
    elif (isinstance(roman_string, str) is False):
        return (0)
    N = 0
    for i in range(len(roman_string)):
        N += dictRoman.get(roman_string[i])
        if (i + 1 < len(roman_string)):
            if (dictRoman.get(roman_string[i + 1])
                    > dictRoman.get(roman_string[i])):
                N -= (dictRoman.get(roman_string[i])) * 2
    return (N)
