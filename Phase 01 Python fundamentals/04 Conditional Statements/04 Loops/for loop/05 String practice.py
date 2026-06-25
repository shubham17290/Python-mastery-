"""#  Reverse the string manually
# palindrome check
a = input(" enter your string (word) ")
rev = ""
for i in range(len(a) - 1, -1, -1):
    rev = rev + a[i]
if rev == a:
    print("Yes palindrome")
else:
    print("no not a palindrome")
"""
"""
#  Count the letter , digit , and special character in the given string

#  approach 01 
a = "pdoew653745@#$woer200293774 4r0990 @7 &% (^$)"


char = 0
spchar = 0
digits = 0
for i in a:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        char = char + 1
    else:
        spchar = spchar + 1

print(f"characters {char} , special characters - {spchar}, digits - {digits}") """

# in approach two we use the concept of the unicode 

