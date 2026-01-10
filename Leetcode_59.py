
from typing import Optional
from typing import ListNode
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top=0
        left=0
        right=n-1
        result=[[0]*n for _ in range(n)]
        bottom=n-1
        val=1
        while left<=right and top<=bottom:
            for c in range(left,right+1):
                result[top][c]=val
                val+=1    
            top+=1
            for j in range(top,bottom+1):
                result[j][right]=val
                val+=1
            right-=1

            if top<=bottom:
                for k in range(right,left-1,-1):
                    result[bottom][k]=val
                    val+=1
                bottom-=1


            if left<=right:
                for l in range(bottom,top-1,-1):
                    result[l][left]=val
                    val+=1
                left+=1
            




        return result



        