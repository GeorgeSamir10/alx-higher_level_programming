#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            if all(isinstance(x, int) for x in (my_list_1[i], my_list_2[i])):
                result = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            res.append(res)
    return res
