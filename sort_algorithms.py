# just trying to learn sort algorithms

# Selection sort.
# Bubble sort.
# Insertion sort.
# Merge sort.
# Quicksort.

import timeit
import numpy as np
from random import randint

# O(n^2) average, worst
# O(n)
def selection_sort(array):

    for i in range(len(array)):
        min_val = array[i]
        min_index = i
        
        # look for smallest after i
        for j in range(i, len(array)):
            if array[j] < min_val:
                min_val = array[j]
                min_index = j
        
        # swap the current i with smallest from i to end
        print("min_val ", min_val)
        temp = array[min_index]
        array[min_index] = array[i]
        array[i] = temp
        print("  after swap with i", i, "  ", array)

    return array

# O(n^2) average, worst
# O(n) best
def bubble_sort1(array):
    
    # pass loop, this can be less though
    for i in range(len(array)):
        # now each pass
        for j in range (1, len(array)):
            # swap
            if array[j]<array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array
    
  
# a better implementation
def bubble_sort2(array):
    
    # pass loop,
    # until there're not more swaps
    swap_flag = True
    while swap_flag==True:
        print(array)
        swap_flag = False
        
        # now each pass
        for j in range (1, len(array)):
            # swap
            if array[j]<array[j-1]:
                
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
                swap_flag = True
                print(" swap ", array[j], array[j-1], " -> ", array)
                
    return array
    
    
    
 
 
 

# O(n^2) average, worst
# O(n) best
def insertion_sort(array):
    
    # first pass, everythin is sorted before i
    for i in range(1, len(array)):
        # now insert j(or i) in the sorted [0:i] subarray
        j = i
        while j>0 and array[j-1]>array[j]:
            
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j -= 1
    return array

 
 
# unfortunately, recursive
# O(n log n) best, average, worst
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # Find the middle point and devide it
    middle = len(unsorted_list) // 2

    return merge(merge_sort(unsorted_list[:middle]), merge_sort(unsorted_list[middle:]))

# Merge the sorted halves
def merge(left_half,right_half):
    print(left_half, " - ", right_half)
    res = []
    
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res






def quick_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    print(array, " pivot ", pivot)
    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quick_sort(low) + same + quick_sort(high)
    
    
# exp_num = 100000
# exp_repeat = 5 
    
# print("timeit, bubble1", np.mean(timeit.repeat(stmt='bubble_sort1([8, 2, 6, 4, 5])', number=exp_num, repeat=exp_repeat, globals=globals()))/exp_num*1000)
# print("timeit, bubble ",np.mean(timeit.repeat(stmt='bubble_sort([8, 2, 6, 4, 5])', number=exp_num, repeat=exp_repeat, globals=globals()))/exp_num*1000)
array = [8, 2, 6, 4, 5]
print(selection_sort(array))