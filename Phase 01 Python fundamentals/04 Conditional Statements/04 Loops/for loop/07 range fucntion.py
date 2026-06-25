"""seq = range(10)
for i in seq:
    print(i)"""

from jinja2.utils import pass_context
from pickletools import int4

# method 01
"""range(start ? , stop , step?)

here :
start : (Included )optional to include , because by default it has value of : 01 
stop : (excluded)it's mandatory hai ye : if n then it will print upto (n-1)
step : (excluded) it is also not mandatory field it is by default step by 1 by 1 value , one after another 

and there is mainly 3 way's to write the range functions , for the for loop ,

and they are as follows:

"""
"""# method 01
for i in range(5):
    print(i)"""

"""# method 02 
for i in range(1,5):
    print(i)"""

"""#  method 03
for i in range(1, 5 , 2):
    print(i)
"""

"""# practice 01 ; Even number printing from the 0 to 100 
for i in range(0, 101, 2):
    print(i)
"""
"""#  for the odd numbers 
for i in range(1, 100, 2):
    print(i)"""


"""#  1 to 100
for i in range (1, 101,1):
    print(1)"""

"""for i in range(100, 0 , -1):
    print(i)"""

"""#  multiplication table for the number n
n = int(input("enter the number for the table:- "))
for i in range(1, 11, 1):
    print(f"{i}*{n}={i*n}")
"""

"""#  let's understand the pass statement inside the range function !
for i in range(5):
    pass

    
print("some useful work")
    """


"""# WAP to find the sum of n natural numbers
n = int(input("enter your number:- "))
sum = 0
for i in range(1, n+1):
    sum += i # will store the total sum 

print("total sum is ", sum) # and when it will exit then it will print the sum it's summed 
"""
"""
# WAP to find the factorial of the n numbers ,

n = int(input("Enter your numbers here "))
fact = 1
for i in range(1, n + 1):  # condition to check !
    fact = fact * i  # logic for the factorial of the number
print(f"factorial of number {n} is = {fact} ")
"""