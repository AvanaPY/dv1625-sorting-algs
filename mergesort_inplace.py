# Written by  Emil Karlström and yoinked from stackoverflow I think
#             Blekinge Tekniska Högskola
#             DVAMI19
# Code for Assignment 1 of course DV1625
# No steal code P L O X 

def __merge(lst, left, middle, right):
    left2 = middle + 1 # Start of "right" part

    # This checks if it's already sorted
    if lst[middle] <= lst[left2]:
        return
    
    # Loop over the sections until done
    while left <= middle and left2 <= right:

        # if sections are equal just increment left
        if lst[left] <= lst[left2]:
            left += 1
        else:
            num = lst[left2]
            idx = left2

            # Shift everything by 1 to the left and move left2 to left
            while idx != left: 
                lst[idx] = lst[idx -1]
                idx -= 1

            lst[left] = num

            # Change all pointers so they match their respective data once again
            left += 1
            middle += 1
            left2 += 1

def __merge_sort(lst, left, right):
    if left < right:
        middle = (left + right) // 2

        __merge_sort(lst, left, middle)
        __merge_sort(lst, middle + 1, right)

        __merge(lst, left, middle, right)

def mergesort_inplace(lst):
    __merge_sort(lst, 0, len(lst)-1)
    return lst