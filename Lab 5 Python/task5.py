year = eval(input("Enter year to check whether it is a leap year or not "))
if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Year u entered is a leap year")
else:
    print("Year u entered is not a leap year")