# character_to_store = "examplesfsfsefwfmasdalwwraleemfakenmeglsksnmdlfkamnlfkanmglskemgglsrkjsjliejrlaefstring"
# character_to_check = "afzlmxyz"

# hashmap=[0]*26
# for char in character_to_store:
#     index=ord(char)-97
#     hashmap[index]+=1

# for char in character_to_check:
#     index=ord(char)-97
#     if index<0 or index>25:
#         print(f'{char} occurs 0 times')
#     else:
#         print(f'{char} occurs {hashmap[index]} times')


#we can also use dictionary to solve the same problem   

character_to_store = "examplesfsfsefwfmasdalwwraleemfakenmeglsksnmdlfkamnlfkanmglskemgglsrkjsjliejrlaefstring"
character_to_check = "afzlmxyz"

hashmap={}
for char in character_to_store:
    hashmap[char]=hashmap.get(char,0)+1

for char in character_to_check:
    count=hashmap.get(char,0)
    print(f'{char} occurs {count} times')    


#by using this we can save space and instead of creating large list  we can just occupy a space for those which are present
