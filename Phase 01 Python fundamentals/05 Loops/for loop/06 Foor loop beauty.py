"""
program 01 :

list = [
    2,
    5,
    56,
    2,
    6,
    41,
    45,
]
for val in list:
    print(val)"""

# # program 02
# veggies = ["potato", "tomato", " bringal", "guwawa", "ledyfinge"]

# for v in veggies:
#     print(v)


"""#  print cha of the string
v = " shubham maurya "
for i in v:
    if i == "y":  # Applying the searching algorithm in this code
        print(" o found ")
        break

    print(i)

else:
    print(" End ")
"""

"""
Q; 01 Printing numbers from the  list 

nums = [4, 45, 4, 543, 5, 435, 4, 22432, 432, 3244, 324, 3, 66, 5, 654, 654, 6]

for i in nums:
    print(i)
"""

# Q :02 Printing the special number at the x


nums = (4, 45, 4, 543, 5, 435, 4, 22432, 432, 3244, 324, 3, 66, 5, 654, 654, 6)
x = 432
idx = 0
for i in nums:
    if i == x:
        print("number found at the index", idx)
        break
    idx += 1
