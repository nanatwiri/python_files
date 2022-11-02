# python uses "if" statements to evaluate conditions


# applications to determine age to allow one to learn driving
# *driver_age = int(input("Please enter your age"))


# *if (driver_age >= 18):
#print("Eligible to acquire a drivers licence")
# *else:
# *print("Sorry,you are not old enough to register")
# * print("Eligibility is from age 18")
# *print(f"please try again in ,{18-driver_age} years =)")

# if you want to run the above application then remove both the # and * where its been put

# APPLICATION TO COMPUTE STUDENTS AND THEIR GRADES
student_mark = int(input("Enter final Mark: "))

# Here we introduce elif a function in python which is under if functions
if (student_mark >= 70):
    print("CONGRATULATIONS!!")
    print("Pass: Grade A")
elif (student_mark >= 60):
    print("Pass: Grade B")
elif (student_mark >= 50):
    print("Pass: Grade C")
elif (student_mark >= 40):
    print("Pass: Grade D")
else:
    print("FAIL!")
