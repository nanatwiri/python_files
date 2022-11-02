#input in python
# used to capture input and stored input in the application

print("User profile Application")

# for the below code to work you just need to remove the hash where necessary
first_name = input("enter your first name")
# the prompt is make the user aware of what information they are being asked for
last_name = input("enter your last name")
Occupation = input("what do you do for a living?")

print("Your first name is, " + first_name)
print("Your last name is, " + last_name)
print("Your Occupation is, " + Occupation)

# another way of outputing in python is through formatted  strings

print(f"Your First name is, {first_name} and your Job is, {Occupation}")

# you put f right before the txt in brackets

# handling non string input
age = int(input("please enter your age:"))

# include the data type before the input section to inform the application that computations are likely to occur like calculating age and so on and so on

print(f"In two years, your age will be : {age+2}")
