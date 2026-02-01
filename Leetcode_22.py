class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def solve(ind,total,brackets,result):
            if ind>=len(brackets):
                if total==0:
                    result.append("".join(brackets))
                return
            n=len(brackets)//2    
            if total>n or total<0:
                return
            brackets[ind]="("

            solve(ind+1,total+1,brackets,result)
            brackets[ind]=")"
            solve(ind+1,total-1,brackets,result)
        brackets=[""]*(2*n)
        result=[]
        solve(0,0,brackets,result)
        return result

        