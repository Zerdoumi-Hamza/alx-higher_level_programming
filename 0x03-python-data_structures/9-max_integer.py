#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return "None"
    else:
        maxi = my_list[0]
        for i in range(len(my_list)):
            if maxi <= my_list[i]:
                maxi = my_list[i]
            else:
                maxi = maxi
    return maxi
