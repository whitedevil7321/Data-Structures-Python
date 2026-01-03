def buy_and_sell(nums):
    max_amount=float('-inf')
    min_amount=float('inf')
    
    for i in range(len(nums)):
        if nums[i]<min_amount:
            min_amount=nums[i]
        elif nums[i]-min_amount>max_amount:
            max_amount=nums[i]-min_amount
    return max_amount if max_amount!=float('-inf') else 0


prices=[7,1,5,3,6,4]
result=buy_and_sell(prices)
print("The maximum profit from buying and selling is:",result)
