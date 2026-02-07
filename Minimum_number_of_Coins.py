class Solution:
    def findMin(self, n):
       # code here 
        coins=[10,5,2,1]
        total_coins=0
        for coin in coins:
            if n>=coin:
                total_coins+=n//coin
                n=n%coin
                if n==0:
                    break
        return total_coins