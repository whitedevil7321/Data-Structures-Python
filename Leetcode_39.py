from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def solve(index,total,subset):
            if index>=len(candidates):
                return
            if total==target:
                result.append(subset.copy())
                return
            if total>target:
                return
            subset.append(candidates[index])

            solve(index,total+candidates[index],subset)
            subset.pop()
            solve(index+1,total,subset)
        solve(0,0,[])    
        return result   
                

        