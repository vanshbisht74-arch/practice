def factorial(n):
    if n<0:
        return "INVALID INPUT"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter Number To Find Factorial of "))
result=factorial(n)


if result=="INVALID INPUT":
    print("FACTORIAL of NEGATIVE NO. IS NOT DEFINED PLEASE ENTER ANOTHER VALUE")
else:
    print("Factorial=",result)
    