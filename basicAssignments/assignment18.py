# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = input('Enter a sentence')
upperCase = 0
lowerCase = 0
for i in sentence:
    if i.isupper():
        upperCase = upperCase + 1
    elif i.islower():
        lowerCase = lowerCase + 1
print('UPPER CASE ', upperCase)
print('LOWER CASE ', lowerCase)