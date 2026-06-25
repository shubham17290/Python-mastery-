a = "h"
print(ord(a))  # ord() module helps to find the unicode value of the data


# indexing


b = "COLLEGE"
print(b[0], b[4], b[3])
print(b[5])

print(b[6])
print(b[-1])

a = "COLLEGE"
print(a[3:6:1])

print(a[1:7:2])
print(a[::])
print(a[::2])

b = " Hello how are you "
"""
H/W:
# how
# you
# Hello 

"""
print(b[7:11:1])  # how

print(b[15::1])  # you
print(b[1:6:1])  # Hello
