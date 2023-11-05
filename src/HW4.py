# interpretation
print("Interpretation")
x = 5.5 # floating point
x = "Hello World!" # string
print(x)

# Boolean expressions
print("\nBoolean Expressions")
print("5 < 10 and 5.5 > True =", 5 < 10 and 5.5 > True)  # True
print("1 > 2 or 3 > 0 =", 1 > 2 or 3 > 0)  # True
print("not 5 < 10 =", not 5 < 10)  # False

# short circuit evaluation
print("\nShort Circuit Evaluation")
def test():
    print("Function was called")
    return True

print(True or test())  # "Function was called" is not printed because the function is not called

# numeric types
print("\nNumeric Types")
x = 5  # integer
y = 5.5  # floating point number
z = 1 + 2j  # complex number
print("x =", x, "Type:", type(x))
print("y =", y, "Type:", type(y))
print("z =", z, "Type:", type(z))

print("x + y =", x + y)  # addition
print("y - x =", y - x)  # subtraction
print("x * y =", x * y)  # multiplication
print("y / x =", y / x)  # division
print("abs(z) =", abs(z))  # magnitude of a complex number
print("BIG =", 1e10000) # prints inf

# strings
print("\nStrings")
s = "Hello"
t = "World"
print("s =", s, "t =", t)
print('%s + " " + %s =' % (s, t), s + " " + t)  # concatenation + "%" operator 
print("s * 3 =", s * 3)  # repetition
print("s.lower() =", s.lower())  # built-in function
print("%i in hex is %02x" % (99, 99))

# arrays
print("\nArrays")
arr = [1, 2, 3]
print("arr = [1, 2, 3]\ntype(array):", type(arr)) # not an array

# lists
print("\nLists")
class Car:
    def __init__(self, speed):
        self.speed = speed
myList = [1, "apple", Car(200)] # dynamic, mutable
print(myList)
myList.append(myList) # list contains a reference to itself
myList[0] = 1e2
print(myList) # no error

# tuples
print("\nTuples")
myTuple = tuple(myList)
print(myTuple)
#myTuple[1] = 2 # can't change

# slices
print("\nSlices")
print("myList[1:3]:", myList[1:3])
print("myList[::3]:", myList[::3]) # every third element. keeps looking in the same list prints [...]

# index range checking
print("\nIndex Range Checking")
#print(myList[999]) # out of range error
print("this is a string"[-1]) # negative starts from the last element

# dictionaries
print("\nDictionaries")
examGrades = {"Exam 1": 33, "Exam 2": 100, "Exam 3": 99.9}
print("examGrades:", examGrades)
del examGrades["Exam 1"]
examGrades["Exam 1"] = 87 # At the end
print("examGrades:", examGrades)

# if statement
print("\nIf Statement")
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# switch statement
print("\nSwitch Statement")
# no switch keyword. import or function required.

# for loop
print("\nFor Loop")
for i in range(3):
    print(i)
    
for i in range(3):
    print(i)
else:
    print("Loop finished successfully.")
    
# Creating a list of squares using list comprehension
squares = [x**2 for x in range(6)]
print(squares)
    
# while loop
print("\nWhile Loop")
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished successfully.")
    
# indentation to denote code blocks
print("\nIndentation Code Blocks")
for i in range(5):
    if i%2 == 0:  # start of if block
        print(f"{i} is even")  # end of if block
    else:  # start of else block
        print(f"{i} is odd")  # end of else block

# type binding
print("\nType Binding")
# Has been demonstrated throught this file. Dynamic.

x = "5"  # x is a string
y = 3  # y is an integer

# This will not raise an error, but it might not do what you expect
z = x * y

# type checking
print("\nType Checking")
vehicle = Car(300)
print("vehicle: ", type(vehicle))
if type(x) is int:
    print ("x is an integer")
else:
    print("x is not an integer")

# functions
print("\nFunctions")
def mean(*numbers):
    return sum(numbers) / len(numbers)

print("mean(1, 2, 3, 4)", mean(1, 2, 3, 4))  # Call the function with four arguments
print("mean(1, 2, 3)", mean(1, 2, 3))  # Call the function with three arguments

def power(base, exponent=2):
    return base**exponent

print("power(5) =", power(5))  # Call the function without the exponent argument
print("power(5, 3) =", power(5, 3))  # Call the function with the exponent argument
x = power(10)
print(x)


# other feature - Exception Handling
print("\nException Handling")
try:
    file = open("non_existent_file.txt", "r")
    print(file.read())
except FileNotFoundError: # built in error types
    print("file not found")
    
try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally: # always executes
    print("End of program")