class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        sum=0
        def backtracking(index,total):
            if total==K:
                return True
            elif total>K or index==N:
                return False
            if index>len(arr):
                return False
            sum=total+arr[index]
            pick=backtracking(index+1,sum)
            if pick==True:
                return True
            sum=total
            notpick=backtracking(index+1,sum)
            return notpick
        return backtracking(0,0)
            
            
            
                
                