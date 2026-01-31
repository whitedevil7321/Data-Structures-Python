class solution:
    def solve(self,nums:list,target:int)->list:
        result=[]
        def func(index,subset,target):
            if index>=len(nums):
                if sum(subset)==target:
                    result.append(subset.copy())
                return
            subset.append(nums[index])
            func(index+1,subset,target)
            subset.pop()
            func(index+1,subset,target) 
        func(0,[],target)   
        return result    
        

s=solution()
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
target=20
print(s.solve(nums,target))
