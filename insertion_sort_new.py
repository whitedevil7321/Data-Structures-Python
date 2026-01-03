def insertion_sort(arr):
    n=len(arr)
    k=0
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            key=arr[i]
            for j in range(i-1,-1,-1):
                if arr[j]>key:
                    arr[j+1]=arr[j]
                    k=j
                else:
                    break
            arr[k]=key
    return arr


arr=[12,11,13,5,6]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
