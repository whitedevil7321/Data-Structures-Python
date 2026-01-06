def binary_search(nums,target):

    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1    

nums=[1,2,3,4,5,6,7,8,9]
target=3
result=binary_search(nums,target)
print("Element found at index:",result+1)


#now We wille be using the Recursive version of it
def recursive_binary_search(nums,tager,low,high):
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif low>high:
        return -1
    if nums[mid]>target:
        return recursive_binary_search(nums,target,low,mid-1)
    else:
        return recursive_binary_search(nums,target,mid+1,high)    
    

result_recursive=recursive_binary_search(nums,target,0,len(nums)-1)
print("Element found at index(using recursion):",result_recursive+1)
