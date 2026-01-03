number=5111117
count=0

while number>0:
    last_digit=number%10
    count+=1
    number=number//10

print("Total digits:",count)