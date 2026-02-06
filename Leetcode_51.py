from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board=["."*n for _ in range(n)]
        check_col=[0]*n
        lower_diagonal=[0]*(2*n-1)
        upper_diagonal=[0]*(2*n-1)

        def solve(col):
            if col==n:
                result.append(list(board))
                return 
            for row in range(n):
                if check_col[row]==0 and lower_diagonal[row+col]==0 and upper_diagonal[(n-1)+(col-row)]==0:
                    
                    board[row]=board[row][:col]+"Q"+board[row][col+1:]
                    check_col[row]=1
                    lower_diagonal[row+col]=1
                    upper_diagonal[(n-1)+(col-row)]=1
                    
                    solve(col+1)
                    
                    board[row]=board[row][:col]+"."+board[row][col+1:]
                    check_col[row]=0
                    lower_diagonal[row+col]=0
                    upper_diagonal[(n-1)+(col-row)]=0


        solve(0)
        return result


