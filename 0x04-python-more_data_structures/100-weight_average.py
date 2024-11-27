#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list == [] or my_list is None):
        return (0)
    sum_weighted = 0
    product = []
    for i in range(len(my_list)):
        sum_weighted += my_list[i][1]
        product.append(my_list[i][0] * my_list[i][1])
    weightaverage = sum(product) / sum_weighted
    return (weightaverage)
