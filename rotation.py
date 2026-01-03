def rotation(nums,k):
    if len(nums)==0:
        return None
    if len(nums)==1:
        return nums
    k=k%len(nums)
    for i in range(k):
        last=nums[-1]
        for i in range(len(nums)-1,0,-1):
            
            nums[i]=nums[i-1]
        nums[0]=last
    return nums

# Example usage:
numbers = [1, 2, 3, 4, 5]
k = 101
result = rotation(numbers, k)
print("The rotated list is:", result)  # Output: The rotated list is: [4, 5, 1, 2, 3]

    
