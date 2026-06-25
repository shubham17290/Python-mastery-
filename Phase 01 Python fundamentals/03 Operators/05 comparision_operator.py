"""
4. Logical Operators:
In Python, logical operators are used to combine conditional statements. They allow you to make decisions based on multiple conditions.
Used in decision making.

syntax for :

and : a and b -> here both a and b both needs to be true to make the overall output is true
or : a or b -> one needs to be true to make the overall result true
not : a not b --> This one is usually used to reverse the output , from true to false and false to true 

"""

# Example: Can you go for a drive?
has_license = True
is_sober = True # catty word with good meaning : one who is not in under the influence of alcohol and , drugs 
has_car = True

# Both must be True
can_drive = has_license and is_sober
print(can_drive)  # Output: True

# This will be True because has_car is True
can_actually_drive = has_license and has_car
print(can_actually_drive)  # Output: true
