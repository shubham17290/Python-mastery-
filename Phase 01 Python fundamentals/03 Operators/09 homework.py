#  PRACTICE Questions on the :  Predict the Output
# Q : 01
print(10 + 5 * 2)  # 20

# Q : 02
print((10 + 5) * 2)  # 30

# Q : 03
print(20 / 5 + 3)  # 7.0

# Q : 04
print(2**3 * 2)  # 16
# Q : 05

print(10 % 3 + 2)  # 5

#  PRACTICE Questions on the : Conditional Operators

# Q: 06
print(10 > 5)  # True

# Q : 07
print(10 == 10)  # True


#  Q : 08

print(5 != 5)  # False

# Q : 09

print(10 >= 10)  # True

#  Q: 10

print(7 <= 7)  # True

# PRACTICE Questions on the : Logical operator

# Q : 11

print(True and False)  # False

#  Q: 12

print(True or False)  # True

# Q : 13

print(not True)  # False

# Q: 14

print(10 > 5 or 20 < 10)  # True

# Q : 15
print(10 < 5 or 20 < 10)  # False

#  PRACTICE Questions on the :  Assignment Operators

# Q : 16
x = 10
x += 5
print(x)  # x = x +5 --> 10+5 = 15

# Q : 17

x = 20
x -= 8
print(x)  # x = x - 8 --> 20-8 = 12

# Q :18
x = 5
x *= 3
print(x)  # x = x * 3 --> 5 * 3 = 15

# Q : 19

x = 20
x /= 4
print(x)  # x = x / 4 --> 5.0

# Q : 20

x = 2
x **= 4
print(x)  # x = x^4 --> 2^4 = 16

# Level 5: Membership Operators

# Q : 21

print("a" in "Shubham")  # True

# Q : 22


print("z" in "Python")  # False

#  Q: 23 : on the list

print(5 in [1, 2, 3, 4, 5])  # True

#  Q : 24 : On the list

print(10 not in [1, 2, 3])  # True

#  Level 6: Identity Operators
#  Q : 25
a = [1, 2]
b = a

print(a is b)  # True

# Q: 26

a = [1, 2]
b = [1, 2]

print(a is b)  # False : memory location can not be same for the storing two variables


# Level 7: Operator Precedence

#  Q : 27
print(2 + 3 * 4)  # 14

# Q : 28

print((2 + 3) * 4)  # 20


#  Q : 29
print(10 - 2**2)  # 6


#  Q  : 30
print(100 / 10 * 2)  # 20.0(because of the /(division operator))

# Q: 31

print(5 + 2 > 6 and 10 < 20)  # True

#  Q : 32

print(not 5 > 2)  # ~(True) = False

# Q  : 33


print(10 == 10 or 5 > 20 and 2 < 4)  # True

# Challenge Questions
# Q 34

x = 5

print(x + 2 * 3**2)  # 23
# Q : 35
print((10 > 5) and (5 < 3 or 8 > 2))  # True

#  Q : 36

print(not (10 > 5 and 2 < 1))  # True


#  Face the real challenge my dear self :

print(
    not (((2 + 3 * 2) ** 2 // 5 % 4) == 1) and (15 / 3 + 2 * 4 >= 13) or (10 != 5 * 2)
)

#  Buddy i have got the answer that is : --> True


print(
    not ((((3 + 2) ** 3 // 10) % 4 + 1) == 2)
    and ((20 / 5 * 2 - 3) >= 5)
    or (8 < 3 + 6 and 10 != 2 * 5)
)
#  buddy the output is : True
