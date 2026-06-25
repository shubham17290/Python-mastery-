"""# Print help world n times

n = int(input("enter your number : - "))

for i in range(n):
    print("Hello world")"""

"""
#  Print natural number from 1-n

n = int(input(" Enter number "))


for i in range(1, n + 1):
    print(i)
"""

"""
#  Reverse the natural number !

n = int(input("enter your number :- "))

for i in range(n,0,-1):
    print(i)"""

"""
 Print the multiplication table for n number


n = int(input("Enter your number here :- "))

for i in range(1, 11):
    print(f"{n}*{i} = {n * i}")


"""
"""
# Print the sum of n natural number

a = 0
sum = int(input("till where you want your sum :  "))

for i in range(1, sum + 1):
    a = a + i

print(a)
"""

"""
#  print the Factorial of the n number
fact = 1
n = int(input("enter your number here : "))
for i in range(1, n + 1):
    fact = fact * i

print(fact)

"""
"""
#  do the sum of the even and odd numbers

n = int(input(" enter your number : "))
odd_sum = 0
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(f"your even sum is {even_sum} and odd_sum is {odd_sum}")"""

"""
# Q: print all factors of the number !

n = int(input("enter your number here :- "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        
        """


#  Q : Check if a number is perfect (sum of factors = the number itself).
"""
n = int(input(" Enter your number :- "))
s = 0
for i in range(1, n):  # last factor excluded
    if n % i == 0:
        s = s + i

if s == n:
    print("perfect number ")
else:
    print("Not a perfect number ")

"""

# find out the number is prime number or composite number !

"""n = int(input(" Enter your number :- "))

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("composite number")
"""