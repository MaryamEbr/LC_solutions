# just trying different binary searches, iterative and recursive

def binary_search_iterative(array, target):
    start = 0
    end = len(array)-1
    
    while start<=end:
        
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            start = mid+1
            
        elif array[mid] > target:
            end = mid-1
    return -1


def binary_search_recursive(array, target, start, end):
    
    mid = (start+end)//2
    # print(array[start], array[end], array[mid])
    
    if array[mid] == target:
        return mid
    
    if end < start:
        return -1
    
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, end)
        
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)




# print(binary_search_iterative([1, 3, 5, 6, 7, 8, 9], 9))
arr = [1, 3, 5, 6, 7, 8, 9]
print(binary_search_recursive(arr, 9, 0, len(arr)-1))