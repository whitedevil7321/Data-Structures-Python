number=1635
number_copy=number
sum=0

while number_copy>0:
    last_digit=number_copy%10
    sum+=last_digit**len(str(number))
    number_copy=number_copy//10


print("Armstrong number" if sum==number else "Not an Armstrong number")    