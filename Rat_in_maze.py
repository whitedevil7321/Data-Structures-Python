class Solution:
    def ratInMaze(self, maze):
   
        n=len(maze)
        result=[]
        def solve(row,col,subset):
            if row < 0 or col < 0 or row >= n or col >= n or maze[row][col]==0:
                return
          
            if row==n-1 and col==n-1:
                result.append("".join(subset))
                return
            maze[row][col]=0
            
            subset.append("U")
            solve(row-1,col,subset)
            subset.pop()
            
            subset.append("D")
            solve(row+1,col,subset)
            subset.pop()
            
            subset.append("L")
            solve(row,col-1,subset)
            subset.pop()
            
            subset.append("R")
            solve(row,col+1,subset)
            subset.pop()
            
            maze[row][col]=1
        if maze[0][0]==1:
            solve(0,0,[])
        return sorted(result)
            
            
            
                