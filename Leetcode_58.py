class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string=s.split(" ")
        new_list=[x for x in new_string if(x!='') and(x!="\t")]

        return len(new_list[-1])
        
        