def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+(n-2)

n=int(input("Enter the value of n: "))
print(f"The {n}th Fibonacci number is: {fibo(n)}")