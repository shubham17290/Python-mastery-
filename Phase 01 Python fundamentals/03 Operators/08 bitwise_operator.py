"""
The Bitwise Operators  :
1. & {and}
2. | {or}
3. ^ {xor}


"""

from fontTools.merge.util import bitwise_and

x = 10  # 1010 binary of 10
y = 7  # 0111 binary of 7
bitwise_or = x | y
print(f"{x}|{y} = {bitwise_or}")

bitwise_and = x & y
print(f"{x} & {y} = {bitwise_and}")

bitwise_xor = x ^ y
print(f"{x} ^ {y} = {bitwise_xor}")

bitwise_not = ~x
print(f"~{x} = {bitwise_not}")

bitwise_not0 = ~y
print(f"~{y} = {bitwise_not0}")

left_shift = x << 1   # 1010 =  10100
print(f"{x} left shift value = {left_shift}")

right_shift = x >> 1 # 1010 = 101

print(f"{x} right_shift value = {right_shift}")
