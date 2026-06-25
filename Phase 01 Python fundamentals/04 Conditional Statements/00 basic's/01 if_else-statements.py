# Q  01 : You have to take the input of the age and tell the , person can vote or not

age = int(input("Please enter your age buddy : "))

if age >= 18:
    print("Congratulation Brother 🎉 you can vote !")
else:
    print("you're not eligible to vote buddy ! ")


#  Q 02 : Mom- money triology

money = int(input("Mom is going to give you : "))

if money == 10:
    print(" I will have a chocobar")
elif money == 50:
    print("I am going to have Dahi with Curd")
elif money == 100:
    print(" Now i am going to have Banana shake and roasted peenut")

else:
    print(" i am going to stay hungry for today ! ")

num1 = int(input("first number is : "))
num2 = int(input("second number is : "))

# Check for equality first, or use strictly greater than (>)
if num1 > num2:
    # f-strings allow you to print the actual value of the variable
    print(f"{num1} is the greatest!")
elif num2 > num1:
    print(f"{num2} is the greatest!")
else:
    # If num1 isn't greater, and num2 isn't greater, they MUST be equal.
    print("Both numbers are equal!")


#  Q 01 : priNT the greatest between two of the !
num1 = int(input("enter your number here sir ji ! : "))
num2 = int(input("enter your number here sir ji ! : "))


if num1 > num2:
    print(f"number 1 {num1} is greater than num2")
elif num2 < num2:
    print(f"number 2 {num2} is greater than 1  ")
else:
    print("both numbers are equal !")
