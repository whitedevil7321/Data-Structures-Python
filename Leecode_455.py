class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        n=len(g)
        s.sort()
        m=len(s)
        left=0
        right=0
        count=0
        while left<n and right<m:
            if g[left]<=s[right]:
                count+=1
                left+=1
                right+=1
            else:
                right+=1
        return count
