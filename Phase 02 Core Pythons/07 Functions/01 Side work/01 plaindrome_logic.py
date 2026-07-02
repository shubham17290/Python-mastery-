"""a = 123
copy = a
rev = 0
 
while a>0:
    rev = rev *10 + a %10
    a = a/10
    
if copy == rev:
    print("Palindrome number")
else:
    print(" no palindrome number ")"""

# function in the reusable block of  code that can be use any time at anywhere :
# type :
# 1. Implicit function - predefined functions
# 2. Explicit function- user defined function

def hello():
    print("hello how are you")
    print("welcome to fighters club")
    print("hello how are you")
    print("welcome to fighters club")
    print("hello how are you")
    print("welcome to fighters club")

hello()
