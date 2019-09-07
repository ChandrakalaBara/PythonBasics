# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.

str = input('Enter comma seperated numbers').split(',')

print(type(str))
print(str)
tpl = tuple(str)
print(type(tpl))
print(tpl)
