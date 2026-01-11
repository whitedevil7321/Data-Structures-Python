class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        right=0
        left=0
        n=len(nums)
        if n==1 and nums[0]==1:
            return 1
        count_of_zeros=0
        while right<n:
            if nums[right]==0:
                count_of_zeros+=1
            if count_of_zeros>k:
                if nums[left]==0:
                    count_of_zeros-=1
                left+=1
            if count_of_zeros<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi    



            
        