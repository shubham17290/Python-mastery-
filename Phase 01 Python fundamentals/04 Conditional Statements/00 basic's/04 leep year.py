"""# Q04 : FInd the year that you have entered is a leap year or normal years

year = int(input("please enter your year! :  "))
if year % 100 == 0 and year % 400 == 0:
    print("this year is century year and also leap year ! ")
elif year % 100 != 0 and year % 4 == 0:
    print("leap year !")
else:
    print("not a leap year ")
"""

