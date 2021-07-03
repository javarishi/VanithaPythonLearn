'''
age >= 18
buy alcohol

if condition:
    block of code when condition is true
else:
    block of code when condition is false
'''

age = input("Enter Customer Age:")
int_age = 0
if age.isdigit():
    int_age = int(age)
    if (int_age >= 18) and (int_age < 121):
        print("Alcohol Purchase is Allowed")
    elif int_age > 15:
        print("Check for Valid Parents permission")
    else:
        print("Alcohol purchase is not allowed")
else:
    print("Invalid Input Provided")
print("Thank You")