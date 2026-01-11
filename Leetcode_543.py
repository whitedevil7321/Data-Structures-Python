from typing import Optional
from typing import TreeNode 
class Solution:
    def __init__(self):
        self.diameter = 0

    def solve(self, root):
        if root is None:
            return 0

        left = self.solve(root.left)
        right = self.solve(root.right)

        # update diameter
        self.diameter = max(self.diameter, left + right)

        # return height
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.diameter
