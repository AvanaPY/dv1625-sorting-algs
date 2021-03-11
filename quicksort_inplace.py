# Written by  Emil Karlström
#             Blekinge Tekniska Högskola
#             DVAMI19
# Code for Assignment 1 of course DV1625
# No steal code P L O X 

def __partition(lst, frm, to):
    piv = lst[to]
    i = frm

    for j in range(frm, to):
        if lst[j] < piv:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[to], lst[i] = lst[i], lst[to]    
    return i

def __quicksort(lst, frm, to):
    if frm < to:
        p = __partition(lst, frm, to)
        __quicksort(lst, frm, p-1)
        __quicksort(lst, p+1, to)

def quicksort_inplace(lst):
    __quicksort(lst, 0, len(lst) - 1)
    return lst