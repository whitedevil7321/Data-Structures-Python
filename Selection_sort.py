import numpy as np

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

n = len(arr)
for i in range(n - 1):
    min_index = i + 1 + np.argmin(arr[i + 1:n]) if i + 1 < n else i
    if arr[min_index] < arr[i]:
        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:", arr)
