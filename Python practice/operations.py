num_1 = float(input("Enter number 1 = " ))
num_2 = float(input("Enter number 2=  "))
choice = input("Enter ur choice + - * / // % ** = ")
if choice == '+':
    print('Addition: ' , {num_1 + num_2})
elif choice == '-':
    print('Subtraction: ' , {num_1 - num_2})
elif choice == '*':
    print('Multiplication: ' , {num_1 * num_2})
elif choice == '/':
    print('Division: ' , {num_1 / num_2})
elif choice == '//':
    print('Floor Division: ' , {num_1 // num_2})
elif choice == '%':
    print('Modulus: ' , {num_1 % num_2})
elif choice == '**':
    print('Exponentiation: ' , {num_1 ** num_2})
else:
    print('Invalid choice')