# num=[]
# while True:
#     numbers=int(input('Enter a number to store:'))
#     if numbers==0:
#         break
#     num.append(numbers)

# num_to_cekck=set()

# while True:
#     numbers1=int(input('Enter a number to Check:'))
#     if numbers1==0:
#         break
#     num_to_cekck.add(numbers1)



# frequency_map={}
# for n in num:
#     frequency_map[n]=frequency_map.get(n,0)+1

# for i in num_to_cekck:
#     count=frequency_map.get(i,0)
#     print(f'{i} occurs {count} times')

#This approach is using the frequency map to store the count of each number in the initial list.
#now we will use list as the range will be given and if the range is given then in such case we can createa a list
#but if the range is not given then we have to use dictionary as we dont know the range of numbers


Hash_map=[0]*11
num_to_store=[1,2,3,4,5,6,7,8,9,10,1,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3]
num_to_check=[2,3,5,11,-1,-10,0,1,4,6,7,8,9,10]
for i in num_to_store:
    Hash_map[i]+=1

for i in num_to_check:
    if i<0 or i>10:
        print(f'{i} occurs 0 times')
    else:
        print(f'{i} occurs {Hash_map[i]} times')