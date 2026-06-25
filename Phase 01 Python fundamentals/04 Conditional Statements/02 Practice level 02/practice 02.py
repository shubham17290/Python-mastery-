"""# Q 02 : Check whether a number is positive or negative
number = float(input(" Enter your number here sir :  "))

if number > 0:
    print(f" number {number} is literally even ")
elif number < 0:
    print(f" Number {number} is literally odd ")
elif number == 0:
    print(f"Number {number} is Zero sir ")
else:
    print(" you might have entered the Wrong number or complex number ! ")
"""

while True:
    # 1. User se input lein
    user_input = input("\nEnter your number here sir (ya exit ke liye 'q' dabayein): ")

    # 2. Exit condition
    if user_input.lower() == "q":
        print("Program closed. Have a great day sir!")
        break

    # 3. Seedha float mein convert kar rahe hain (bina kisi try-except ke)
    number = float(user_input)

    # 4. Positive/Negative logic
    if number > 0:
        print(f"Number {number} is Positive.")
    elif number < 0:
        print(f"Number {number} is Negative.")
    elif number == 0:
        print(f"Number {number} is Zero sir.")
