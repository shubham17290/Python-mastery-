"""
Q11
Assign grades:
90+  → A
75+  → B
60+  → C
Else → D"""

while True:
    # 1. User se marks input lena
    user_input = input("\nEnter marks (To stop the program please 'q'): ")

    # 2. Exit condition
    if user_input.lower() == "q":
        print("Program closed!")
        break

    # 3. String ko number (float) mein badalna
    marks = float(user_input)

    # 4. Grading Logic
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    else:
        print("Grade: D")
