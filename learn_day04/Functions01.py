# Functions are objects - First CLass Members
def shout(text):
    return str(text).upper()

test_function = shout

print(shout("This is Test Function"))
print(test_function("This is New Learning for me"))