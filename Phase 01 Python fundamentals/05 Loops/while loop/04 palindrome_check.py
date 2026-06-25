a = int(input(" plz tell you're number sir: "))
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10
if rev == copy:
    print(" palindrome hai bhai ye toh ")
else:
    print(" ye toh palindrome nhi hai bhai ")
