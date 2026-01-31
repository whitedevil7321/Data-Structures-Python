class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh_count=0

        queue=deque()
        grid_copy=deepcopy(grid)
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==1:
                    fresh_count+=1
                if grid_copy[r][c]==2:
                    queue.append((r,c))
                   
        minute=0
        while len(queue)!=0 and fresh_count>0:
            minute+=1
            total_rotten=len(queue)
            for _ in range(total_rotten):
                i,j=queue.popleft()
                for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
                    new_i,new_j=i+dx,j+dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue
                    if grid_copy[new_i][new_j]==2 or grid_copy[new_i][new_j]==0:
                        continue
                    fresh_count-=1    
                    grid_copy[new_i][new_j]=2
                    
                    queue.append((new_i,new_j))

        if fresh_count>0:
            return -1
        return minute        




        