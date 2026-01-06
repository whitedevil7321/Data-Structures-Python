def lower_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            high=mid-1
            lb=mid
        else:
            low=mid+1

    return lb

nums=[1,2,2,2,3,4,5,6,7,8,9]
target=2
result=lower_bound(nums,target)
print("Lower bound index:",result)            


