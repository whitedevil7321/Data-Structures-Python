# using the While Loop and Recurrsion
def RecurrsionUsingWhileLoop(nums,l,r):
    while l<=r:
        nums[l],nums[r]=nums[r],nums[l]
        return RecurrsionUsingWhileLoop(nums,l+1,r-1)
        
        
    



#now using the recurrsion only
def RecurrsionWithoutUsingWhileLoop(nums,l,r):
    if l>=r:
        return
    nums[l],nums[r]=nums[r],nums[l]
    RecurrsionWithoutUsingWhileLoop(nums,l+1,r-1)



nums=[1,2,3,4,5,6]
RecurrsionUsingWhileLoop(nums,0,len(nums)-1)
print(nums)


nums=[1,2,3,4,5,6]
RecurrsionWithoutUsingWhileLoop(nums,0,len(nums)-1)
print(nums)


#in this way we used recurrsion to reverse a sting without using and extra space and by swapping the elements
#so the Time Comlexity of this code will be O(n/2) but 1/2 is a constant so we will ignore it and the time complexity of this will be O(n)
#the space complexity of this code will be O(n) because of the recurrsion stack