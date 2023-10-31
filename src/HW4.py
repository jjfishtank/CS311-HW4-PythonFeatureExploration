# interpretation
print("Interpretation")
x = 5.5 # floating point
x = "Hello World!" # string
print(x)

# Boolean expressions
print("\nBoolean Expressions")
x = 5
y = 10
print(x < y and y > 0)  # True
print(x > y or y > 0)  # True
print(not x < y)  # False

# short circuit evaluation
print("\nShort Circuit Evaluation")
def test():
    print("Function was called")
    return True

print(True or test())  # "Function was called" is not printed because the function is not called due to short circuiting.

# numeric types
print("\nNumeric Types")
x = 5  # integer
y = 5.5  # floating point number
z = 1 + 2j  # complex number
print("x =", x)
print("y =", y)
print("z =", z)

print("x + y =", x + y)  # addition
print("y - x =", y - x)  # subtraction
print("x * y =", x * y)  # multiplication
print("y / x =", y / x)  # division
print("abs(z) =", abs(z))  # magnitude of a complex number

# strings
print("\nStrings")
s = "Hello"
t = "World"

print(s + " " + t)  # concatenation
print(s * 3)  # repetition
print(s.lower())  # built-in function

# arrays
print("\nArrays")

# lists
print("\nLists")

# tuples
print("\nTuples")

# slices
print("\nSlices")

# index range checking
print("\nIndex Range Checking")

# dictionaries
print("\nDictionaries")

# if statement
print("\nIf Statement")

# switch statement
print("\nSwitch Statement")

# for loop
print("\nFor Loop")

# while loop
print("\nWhile Loop")

# indentation to denote code blocks
print("\nIndentation Code Blocks")
for i in range(5):
    if i%2 == 0:  # start of if block
        print(f"{i} is even")  # end of if block
    else:  # start of else block
        print(f"{i} is odd")  # end of else block

# type binding
print("\nType Binding")

# type checking
print("\nType Checking")

# functions
print("\nFunctions")

# one other feature - your choice
print("\nOther")