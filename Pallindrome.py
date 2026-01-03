number=int(input("Enter a number: "))
number_copy=number
new_number=0
while number>0:
    last_digit=number%10
    new_number=new_number*10+last_digit
    number=number//10


print("numbers are palindrom" if new_number==number_copy else "not palindrome")
