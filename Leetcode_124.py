# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def solve(root):
            if root is None:
                return 0
            left_sum= max(0,solve(root.left ))
            right_sum=max(0,solve(root.right))
                  
            self.maxi=max(self.maxi,left_sum+root.val+right_sum)    
            return root.val+max(left_sum,right_sum)
        solve(root)        
        return self.maxi        
                