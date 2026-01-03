def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        item=i
        while item>0 and arr[item-1]>arr[item]: 
            arr[item], arr[item-1]=arr[item-1], arr[item]
            item-=1

    return arr

import numpy as np
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = insertion_sort(arr)    
print("Sorted array:", sorted_arr)

