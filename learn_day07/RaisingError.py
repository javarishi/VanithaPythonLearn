from learn_day07.BusinessError import InvalidAgeError

def validate_age(age):
    int_age = int(age)
    if int_age >= 18:
        print("Customer age is valid")
    else:
        raise InvalidAgeError("Invalid Age Entered", age)

try:
    validate_age(12)
except InvalidAgeError as ie:
    print("Message", ie)