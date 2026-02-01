from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def solve(start, total, path):
            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                solve(i + 1, total + candidates[i], path)
                path.pop()

        solve(0, 0, [])
        return result






# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         result=[]
#         items=set()  
#         def solve(index,total,subset):
#             if total==target:
#                 if tuple(sorted(subset)) not in items:
#                     result.append(subset.copy())
#                     items.add(tuple(sorted(subset)))
#                 return
#             if index>=len(candidates) or total>target:
#                 return
#             subset.append(candidates[index])
#             solve(index+1,total+candidates[index],subset)
#             subset.pop()
#             solve(index+1,total,subset)
#         solve(0,0,[])
#         return result
                

                      