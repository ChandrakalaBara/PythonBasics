# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class BasicClass:
    def getString(self):
        str = input('Enter a string')
        return str
    def printString(self, str):
        print(str.upper())
def test():
    obj = BasicClass()
    str = obj.getString()
    obj.printString(str)

test()