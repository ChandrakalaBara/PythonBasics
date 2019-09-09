# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = input('Enter a sentence')
letters = 0
digits = 0
for i in sentence:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        letters = letters + 1
print('LETTERS ', letters)
print('DIGITS ', digits)