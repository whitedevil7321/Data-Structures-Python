# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dictionary={}
        queue=deque()
        result=[]

        queue.append((root,0))
        while queue:
            node,level=queue.popleft()
            dictionary[level]=node.val
            if node.left:
                queue.append((node.left,level+1))

            if node.right:
                queue.append((node.right,level+1))
        for key in sorted(dictionary):
            result.append(dictionary[key])

        return result

            
                
