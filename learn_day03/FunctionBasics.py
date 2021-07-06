'''
def function_name(parameters: input:optional):
    indendented block - reusable
    return output : optional
'''
# kw parameter - key - value
def say_hello(name="Guest"):
    print("Hello", name)

# * args should always be last
def addition(*args):
    total = 0
    for eachValue in args:
        total = total + eachValue
    return total


say_hello("Neil Armstrong")
say_hello()
value = addition(2,3,5, 6,7,8,9)
print(value)