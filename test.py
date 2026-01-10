class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string=s.split(" ")
        new_list=[x for x in new_string if(x!='') and(x!="\t")]
        last_word=new_list[-1]
        print(len(last_word))

        
        
s=Solution()
s.lengthOfLastWord("   fly me   to                 the moon  ")