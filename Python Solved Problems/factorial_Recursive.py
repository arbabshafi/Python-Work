def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
num=6
print("The Factorial of",num,"is",factorial(num)) 