# num=[]
# while True:
#     numbers=int(input('Enter a number:'))
#     if numbers==0:
#         break
#     num.append(numbers)
    
# frequency={}
# for n in num:
#     if n in frequency:
#         frequency[n]+=1
#     else:
#         frequency[n]=1
    

# for key, value in frequency.items():
#     print(f'{key} occurs {value} times')


# # This is the Time consuming Code

#now will write the optimized code
num=[]
while True:
    numbers=int(input('Enter a number:'))
    if numbers==0:
        break
    num.append(numbers)

frequency={}
for n in num:
    frequency[n]=frequency.get(n,0)+1


for key, value in frequency.items():
    print(f'{key} occurs {value} times')    
