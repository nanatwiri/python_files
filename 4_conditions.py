# python uses "if" statements to evaluate conditions
# applications to determine age to allow one to learn driving
driver_age = int(input("Please enter your age"))

#
if (driver_age >= 18):
    print("Eligible to acquire a drivers licence")
else:
    print("Sorry,you are not old enough to register")
    print("Eligibility is from age 18")
    print(f"please try again in ,{18-driver_age} years =)")
