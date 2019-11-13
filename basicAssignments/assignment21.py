#  Write a program to demonstrate the use of try, except and finally  keywords and demonstrate the following points in the program.
# a) Multiple except blocks.
# b) try-except finally combination.
# c) try-finally combination.


try:
    print('Present in the try block')
    a = [1,2,3]
    n = int(input('Enter a number'))
    print('Element of index', n, 'of an array is', (a[n]))
    a = 5/n
except IndexError:
    print('In except block: index error')
except ZeroDivisionError:
    print('In except block: zero division error')
else:
    print('In else block: No errors occured')
finally:
    print('In finally block')