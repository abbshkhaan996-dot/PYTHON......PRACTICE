Actualemail ="abc@gmail.com"
Actualpass = "abc"
email = (input("Enter your Email: "))
password = (input("Enter your password: "))

if email == Actualemail and password == Actualpass:
    print("User is logged in")
elif email != Actualemail and password != Actualpass:
    print("Enter correct email and password")
elif email != Actualemail and password == Actualpass:
    print("Your email is not correct. Please enter correct email.")
elif email == Actualemail and password != Actualpass:
    print("Your password is not correct. Please enter correct password.")