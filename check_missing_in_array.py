# this is Normal Version
def check_missing(nums):
    freq={}

    for i in range(len(nums)):
        freq[i]=0
    for num in nums:
        freq[num]=1
    for key,value in freq.items():
        if value==0:
            return key

# nums=[0,1,2,3,5]
# missing_number=check_missing(nums)
# print("The missing number is:",missing_number)        

#optimized Version
def check_missing_optimized(nums):
   
    n=len(nums)+1
    total_sum=n*(n-1)//2
    
    return total_sum-sum(nums)

nums=[0,1,2,3,5]
missing_number=check_missing_optimized(nums)
print("The missing number is:",missing_number)    