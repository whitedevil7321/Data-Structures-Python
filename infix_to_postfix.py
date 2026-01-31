class Solution:
    def priority(self,s):
        if s=="+" or s=="-":
            return 1
        if s=="*" or s=="/":
            return 2
        if s=="^":
            return 3
        else:
            return 0

    def infix_to_postfix(self,s):
        if len(s)==0:
            return []
        result=[]
        stack=[]
        for char in s:
            if ("A"<=char<="Z") or ("a"<=char<="z") or ("0"<=char<="9"):
                result.append(char)
            elif char=="(":
                stack.append(char)
            elif char==")":
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.priority(stack[-1])>=self.priority(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)    


s=Solution()
print(s.infix_to_postfix("a+b*(c^d-e)"))