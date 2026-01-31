class Solution:
    def binstr(self, n):
        # code here
        def solve(index,numbers,result):
            if index==len(numbers):
                result.append(''.join(numbers))
                return 
            numbers[index]="0"
            solve(index+1,numbers,result)
            numbers[index]="1"
            solve(index+1,numbers,result)
        
        
        result=[]
        numbers=["0"]*n
        solve(0,numbers,result)
        return result