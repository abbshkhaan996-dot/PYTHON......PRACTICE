phy = float(input("Enter physics marks:"))
chem = float(input("Enter chemistry marks:"))
bio = float(input("Enter biology marks:"))
maths = float(input("Enter mathematics marks:"))
comp = float(input("Enter computer marks:"))
sum = phy + chem + bio + maths + comp
total_sub_marks = 250
percentage = (sum/ total_sub_marks)*100
print(percentage,"%")

if percentage >= 90: 
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 50:
    print("Grade E")
else:
    print("Grade F")