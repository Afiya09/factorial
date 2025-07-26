#write a program in python to print factorial of a number
#input from user
num = int(input("Enter the number for factorial: "))
factorial=1
if num<0:
    print("Factorial is not defined for negative number")
elif num==0:
    print("Factorial of 0 is always 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print(f"The factorial of {num} is{factorial}")