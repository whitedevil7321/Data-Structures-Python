def remove_dup(nums):
    lst={}
    val=0
    for n in nums:
        lst[n]=lst.get(n,0)+1
    idx=0    
    for key in lst:
        nums[idx]=key
        idx+=1
    for i in range(idx,len(nums)):
        nums[i]=0
    return nums        
  


        




numbers = [1, 2, 2, 3, 4, 4,4,4,4,4,4,4,4,4,4,4, 5]
result = remove_dup(numbers)
print(result)
