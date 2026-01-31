<<<<<<< HEAD
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def func(index,subset):
            if index>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[index])
            func(index+1,subset)
            subset.pop()
            func(index+1,subset) 
        func(0,[])    
        return result       

=======
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        total_subsets=1<<n
        for num in range(0,total_subsets):
            lst=[]
            for i in range(0,n):
                if num &(1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result    


        
>>>>>>> 4bdd06052ea18076f31978d17975aff985232d62
