def upper_bound(nums,target):
    low=0
    n=len(nums)
    high=n-1
    ub=n
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1           
        else:
            low=mid+1
    return ub

nums=[1,2,2,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,7,8,9]
target=6
result=upper_bound(nums,target)
print("Upper bound index:",result)        