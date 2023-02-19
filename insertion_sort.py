

def insertion_sort(A):
    
    for i in range(1, len(A)):
       
        current_one = A[i]
        pos = i
        print("A ", A, " curr ", current_one, " i ", i)
         
        while pos>0 and current_one<A[pos-1]:

            A[pos] = A[pos-1]
            A[pos-1] = current_one
            pos -= 1
            
    return A

print("final A", insertion_sort([85, 12, 59, 45, 72, 51]))