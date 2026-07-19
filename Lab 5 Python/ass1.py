def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

num1= int(input("Enter 1st number"))
num2= int(input("Enter 2nd number"))

print("Which operation do u want to choose")
print("1_Addition")
print("2_Subtraction")
print("3_Multiplication")
print("4_Division")
choice= int(input("Enter ur choice "))
if choice == 1:
    result = add(num1 , num2)
elif choice == 2:
    result = subtract(num1 , num2)
elif choice == 3:
    result = multiply(num1 , num2)
elif choice == 4:
    result = divide(num1 , num2)
else:
    print("Invalid Operation")
    
print("Result ", result)