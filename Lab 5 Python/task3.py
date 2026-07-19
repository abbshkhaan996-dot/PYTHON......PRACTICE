s1= eval(input("Enter value for 1st side of triangle "))
s2= eval(input("Enter value for 2nd side of triangle "))
s3= eval(input("Enter value for 3rd side of triangle "))
if(s1==s2 and s2==s3 and s1==s3):
    print("This is Equilateral Triangle")
elif (s1==s2 and s2!=s3):
    print("This is Isosceles Triangle")
elif (s1==s2 and s1!=s3):
    print("This is Isosceles Triangle")
elif (s1==s3 and s1!=s2):
    print("This is Isosceles Triangle")
elif (s1==s3 and s2!=s3):
    print("This is Isosceles Triangle")
elif (s2==s3 and s2!=s1):
    print("This is Isosceles Triangle")
elif (s2==s3 and s3!=s1):
    print("This is Isosceles Triangle")
elif (s1!=s2 and s2!=s3 and s3!=s1):
    print("This is Scalene Triangle")