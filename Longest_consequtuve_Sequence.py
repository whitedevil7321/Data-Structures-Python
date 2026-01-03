# def longest_sequence(nums):
#     nums_set=set(nums)
#     max_length=0
#     for num in nums_set:
#         if num-1 not in nums_set:
#             current_num=num
#             current_length=1
#             while current_num+1 in nums_set:
#                 current_num+=1
#                 current_length+=1
#             max_length=max(max_length,current_length)
#     return max_length

# nums=[100,4,200,1,3,2]
# result=longest_sequence(nums)
# print("The length of the longest consecutive sequence is:",result)

#this was the bruteforce approach now we will be using the optimal approach
def merge_array(left,right):
    result=[]
    i,j=0,0
    n=len(left)
    m=len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    if len(arr )<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge_array(left,right)        


def longest_sequence(nums):
    longest_length=0
    count=0
    nums=merge_sort(nums)
   
    for i in range(0,len(nums)):
        if i==0:
            count=1
               
        elif nums[i]==nums[i-1]:
            continue
        elif nums[i]-nums[i-1]==1:
            count+=1

        else:
            count=1
            
        longest_length=max(longest_length,count)        
    return longest_length   

nums=[102,101,10,9,100,4,200,1,3,2,5,6,7,8,102,103,104,105,106,107,108,109,110,111,112,113,114,115]
result=longest_sequence(nums)
print("The length of the longest consecutive sequence is:",result)
