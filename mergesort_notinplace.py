# Written by  Emil Karlström
#             Blekinge Tekniska Högskola
#             DVAMI19
# Code for Assignment 1 of course DV1625
# No steal code P L O X 

def __merge_arrays(a, b):
    result = []

    # Loop over the lists until we finish with one
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Here we're done with either a or b
    # so we fill the result array with all leftover elements
    while i < len(a):
        result.append(a[i])
        i+=1
    
    while j < len(b):
        result.append(b[j])
        j+=1

    return result

def mergesort_notinplace(lst):
    if len(lst) > 1:    
        mid = len(lst) // 2
        a, b = lst[:mid], lst[mid:]
        a = mergesort_notinplace(a)
        b = mergesort_notinplace(b)
        merge = __merge_arrays(a, b)
        return merge
    return lst