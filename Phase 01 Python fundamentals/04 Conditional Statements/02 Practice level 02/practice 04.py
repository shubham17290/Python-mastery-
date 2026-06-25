# Q 04 : Find the greater of two numbers .

num1 = int(input("enter your first number :  "))
num2 = int(input("enter your second number :  "))

if num1 > num2:
    print(f"number {num1} , is greatest")

elif num2 > num1:
    print(f"number {num2} , is greatest")
elif num1 == num2:
    print(f"number {num1 & num2} , both are same ")
else:
    print(" you might have entered the wrong vale")
