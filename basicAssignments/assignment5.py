# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and print the numbers that are divisible by 5 in a comma separated sequence

numbers = input('Enter sequence of comma separated 4 digit binary numbers')

numbers = numbers.split(',')
result = []
for i in numbers:
    if(int(i,2)%5==0):
        result.append(i)
print(','.join(result))