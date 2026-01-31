class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        no_of_colors=0
        row=len(image)
        cols=len(image[0])
        initial_color=image[sr][sc]
        if initial_color==color:
            return image    
        image_copy=deepcopy(image)
        queue=deque()
        queue.append((sr,sc))
        image_copy[sr][sc]=color
        count_of_initial_color=0
        for r in range(row):
            for c in range(cols):
                if image_copy[r][c]==initial_color:
                    count_of_initial_color+=1
        while len(queue)>0 and count_of_initial_color>0:
            total_len=len(queue)
            for _ in range(total_len):
                i,j=queue.popleft()
                for dx,dy in [(0,-1),(-1,0),(1,0),(0,1)]:
                    new_i=i+dx
                    new_j=j+dy
                    if new_i<0 or new_i==row or new_j<0 or new_j==cols:
                        continue
                    if image_copy[new_i][new_j]==color:
                        continue      
                    if image_copy[new_i][new_j]==initial_color:

                        count_of_initial_color-=1
                        image_copy[new_i][new_j]=color
                        queue.append((new_i,new_j)) 
        return image_copy           


                    
                    

        




