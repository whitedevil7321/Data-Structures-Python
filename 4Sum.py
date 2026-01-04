
# This Solution takes O(n^3) time and O(1) space
#But this solution is more optimal than the previous one
#approach is similar to 3sum problem
# in this we use 2 fix pointers and two veriable pointers so if asked 
# for 5 pointers then we can use 3 fix pointers and 
# 2 veriable pointers and so on

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result=[]
        nums.sort()
        n=len(nums)

        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=n-1
                while k<l:
                    total=nums[i]+nums[j]+nums[k]+nums[l]
                    if total==target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1

                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while l<k and nums[l]==nums[l+1]:
                            l+=1
                    elif total<target:
                        k+=1
                    else:
                        l-=1

        return result






# #this solution takes O(n^3) time and O(n) space
# class Solution:
#     def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
#         if len(nums)<4:
#             return []
#         nums.sort()
#         results=[]
#         n=len(nums)
       
#         for i in range(n):
#             for j in range(i+1,n):
#                 hash_set=set()
#                 for k in range(j+1,n):
#                     fourth=target-(nums[i]+nums[j]+nums[k])
#                     if fourth in hash_set:
#                         quad=[nums[i],nums[j],nums[k],fourth]
#                         quad.sort()
#                         if quad not in results:
#                             results.append(quad)
#                     hash_set.add(nums[k])
#         return results

c=Solution()
print(c.fourSum([1,0,-1,0,-2,2,2,2,2],8))
