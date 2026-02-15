from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []

        data = {}
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, line = queue.popleft()

            if line not in data:
                data[line] = node.data

            if node.left:
                queue.append((node.left, line - 1))
            if node.right:
                queue.append((node.right, line + 1))

        result = []
        for key in sorted(data):
            result.append(data[key])

        return result
