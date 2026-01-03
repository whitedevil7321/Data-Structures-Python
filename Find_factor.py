# number =10
# for i in range(1,number+1):
#     if number%i==0:
#         print(i)

#this is not optimized code

#Optimized approach
from math import sqrt
number=36
result=[]
for i in range(1, int(sqrt(number))+1):
    if number%i==0:
        result.append(i)
        if i!=number//i:
            result.append(number//i)
print(result)
