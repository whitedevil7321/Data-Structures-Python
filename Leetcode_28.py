class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0

        m=len(needle)
        i,j=0,m
        n=len(haystack)
        while j<=n:
            if haystack[i:j]==needle:
                return i
            i+=1
            j+=1
        return -1
        