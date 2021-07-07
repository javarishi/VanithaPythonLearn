# Functions can return functions

def calculator(number, function_name):
    retrun_function_name = None
    def square():
        square_value = number*number
        print(square_value)

    def cube():
        cube_value = number*number*number
        print(cube_value)

    if function_name=="square":
        retrun_function_name = square
    else:
        retrun_function_name = cube

    return retrun_function_name

square_value = calculator(5, "square")
square_value()

cube_value = calculator(5, "cube")
cube_value()