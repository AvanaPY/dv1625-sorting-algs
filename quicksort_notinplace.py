# Written by  Emil Karlström
#             Blekinge Tekniska Högskola
#             DVAMI19
# Code for Assignment 1 of course DV1625
# No steal code P L O X 

def __partition(lst):
    lows = []
    highs = []
    piv = lst[-1]

    for num in lst:
        if num < piv:
            lows.append(num)
        elif num > piv:
            highs.append(num) 
    return lows, highs, piv

def __quicksort(lst):
    if len(lst) > 0:
        lows, highs, piv = __partition(lst)
        lows = __quicksort(lows)
        highs = __quicksort(highs)
        return lows + [piv] + highs
    return lst

def quicksort_notinplace(lst):
    lst = __quicksort(lst)
    return lst