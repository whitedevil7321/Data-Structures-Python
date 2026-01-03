
from pyparsing import nums


def Bubble_Sort(num):
    counter=0   
    n=len(num)
    for i in range(n-2,-1,-1):
        is_swapped=False
        counter+=1
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                is_swapped=True
        if not is_swapped:
            break        
    print("Number of passes:",counter)
    return num

arr=[64,25,12,22,11,1,23,4,2,4,2,4,224,7653,1,2,41]
print("Unsorted array:",arr)
sorted_arr=Bubble_Sort(arr)
print("Sorted array:",sorted_arr)



arr1=[1,2,3,4,5,6,7,8,9,10]
print("Unsorted array:",arr1)
sorted_arr1=Bubble_Sort(arr1)
print("Sorted array:",sorted_arr1)



