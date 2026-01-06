from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return False
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1    
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1

        return False                

nums=[2,5,6,0,0,1,2]
target=0
solution=Solution()
result=solution.search(nums,target)
print("Target found:",result)
