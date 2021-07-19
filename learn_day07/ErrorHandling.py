'''
except order is Specific first Generic later
'''


try:
    age = input("Enter Your Age:")
    ages = [12,13,14]
    int_age = int(age)
    div = 100/int_age
    print(int_age, div, ages[int_age])
except (ValueError, IndexError) as ve:
    print("ValueError or IndexError Handler", ve)
except ZeroDivisionError as zde:
    print("Zero Division not possible", zde)
except Exception as ex:
    print("Handling Unforeseen situation", ex)
else:
    print("Executes Only when try completes without error")
finally:
    print("Finally executes regardless of error or not")

'''
try:
    risky code block
except ErrorList : optional
    logic for handling error
except (any number):
    logic for particular error block
'''