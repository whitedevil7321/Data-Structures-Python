# class Solution:
# 	def subsetSums(self, arr):
# 		# code here
# 		result=[]

# 		def solve(index,total):
# 		    if index==len(arr):
# 		        result.append(total)
# 		        return

# 		    solve(index+1,total+arr[index])
# 		    solve(index+1,total)
#         solve(0,0)
#         return result