
from random import randrange

def quicksort2(lst, start_idx, end_idx):

    #setting the base case of a len = 1 or 0 sublist
    if start_idx > end_idx:
        return

    #defining the pivot and swapping it to the end of the list
    pivot_idx = randrange(end_idx)
    print(pivot_idx)
    pivot_element = lst[pivot_idx]

    pivot_element, lst[end_idx] = lst[end_idx], pivot_element


    #logic to swap fromstart and fromend pointers
    #fromstart = start_idx
    from_end = end_idx

    for idx in range(len(lst[start_idx:end_idx])):
        if lst[idx] >= pivot_element:

            lst[idx], lst[pivot_idx]= lst[pivot_idx], lst[idx]
            from_end -= 1

    return quicksort2(lst, start_idx, pivot_idx-1) + lst[pivot_idx] + quicksort2(lst, pivot_idx + 1, end_idx)



unsorted_list = [2, 54, 12, 34, 9, 1]

quicksort2(unsorted_list, 0, len(unsorted_list)-1)
