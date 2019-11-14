# Write python function with following  arguments
#
# 1. Required arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable-length arguments

# required arguments
def reqArgFunction(a,b):
    print('first required argument ', a)
    print('second required argument ', b)

reqArgFunction(2,1) # calling required argument function

# keyword arguments
def keywordArgFunction(name, id):
    print('Name is ', name)
    print('Id is ', id)

keywordArgFunction(name = 'chandrakala', id = '1')  # calling function with keyword arguments

# default arguments
def defaultArgFunction(name, role = "Associate Software"):
    print('Name is ', name)
    print('Role: ', role)

defaultArgFunction('chandrakala') # calling function and using default value
defaultArgFunction('Sowmya', 'Software') # overriding the default value

# Variable-length arguments
def variableLenArgFunction(*varLenArgs):
    print('values passed are:')
    for value in varLenArgs:
        print(value)

variableLenArgFunction(32) # calling with single value
variableLenArgFunction(2, 5, 7, 9, 15)  # calling with multiple values
