#We will do this Using the Recurrsion
def CheckForPallindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return CheckForPallindrome(s,l+1,r-1)
    

print(CheckForPallindrome("racecar",0,len("racecar")-1))  #True
print(CheckForPallindrome("hello",0,len("hello")-1))      #False

