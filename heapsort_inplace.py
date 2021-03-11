# Written by  Emil Karlström
#             Blekinge Tekniska Högskola
#             DVAMI19
# Code for Assignment 1 of course DV1625
# No steal code P L O X 

def __heapify(lst, n, i):
    mx = i                  # Default "max" value to the root 'i'
    child_l = 2 * i + 1     # Left child  = 2 * index + 1
    child_r = 2 * i + 2     # right child = 2 * index + 2

    # If left child is bigger and exists, consider it "max"
    if child_l < n and lst[mx] < lst[child_l]:
        mx = child_l

    # Consider right child equally
    if child_r < n and lst[mx] < lst[child_r]:
        mx = child_r

    # Change the root if necessary and re-heapify from the new "max"
    if mx != i:
        lst[i], lst[mx] = lst[mx], lst[i]

        __heapify(lst, n, mx)

def __make_max_heap(lst, n):
    for i in range(n//2-1, -1, -1):
        __heapify(lst, n, i)

def __extract(lst, n):
    # Loop backwards and extract elements by replacing index 0 with last item
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        __heapify(lst, i, 0)
        
def heapsort_inplace(lst):
    n = len(lst)            # Length of list to consider as "heap"
    __make_max_heap(lst, n) # Transform the list into a heap
    __extract(lst, n)       # Fully sort the list by "extracting" items in order
    return lst