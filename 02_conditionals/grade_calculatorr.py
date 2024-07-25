marks = 700

if marks >= 101:
    print("OOPS! wrong input")
    exit()

if marks >= 90:
    print("Grade: A, Excellent")
elif marks >= 80:
    print("Grade: B, Very Good")
elif marks >= 70:
    print("Grade: C, Nice work")
elif marks >= 60:
    print("Grade: D, you can do better")
else:
    print("Grade F, you really need to work hard")