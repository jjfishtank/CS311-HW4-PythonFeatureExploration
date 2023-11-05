# Preamble

Each of the below features have been explored with the following methodology:
```
Write a short program or programs to investigate its use. You may combine more than one feature into a single program.

Explain how the feature works in Python and compare it to one or more languages with which you are familiar.

Critique the implementation or use of the feature or construct.
```
The bulk of my experience programming has been through C++. Thus, the feature evaluations are made in comparison to C++.

# Features

### Interpretation
Python runs the code line by line rather than compiling the entire file like C++. This is very noticeable when there are errors because it will run until the exact line it encounters a problem. I found this very convenient for debugging because partially running the program and stopping at the problem line usually lead to finding the problem faster.

### Boolean Expressions
Booleans behaved similarly to what I am used to other than the absence of the '!' operator.

### Short Circuit Evaluation
Logical operators terminate when left hand side is enough to determine the result. Tested this by creating a function that prints when it is called and put it on the right hand side of an or operation. The function is not called as the left hand side evaluates true first. This is the same behavior as C++.

### Numeric Types
Python has quite a few built in data types with standouts being Sets, Touples, Dictionaries, and Complex Numbers. These are not specified at variable declaration, but are deduced from the formatting of literals. Notably missing are sub-type keywords like short, unsigned, double.

### Strings
Tested string manipulation. Noticed that when printing string literals, either quotes or apostrophes can be used. If one is used, the other doesn't need to be escaped to print it. There are several built in functions for Python strings like lower(), swapcase(). Operators are robust--including repetition "*", slicing "[]", and placeholders "%". Very powerful tools for formatting and placeholders. Allows for changing things like precision, numerical system (decimal/hex) within the print line.

### Arrays
Cannot find built in array support, instead lists are used.

### Lists
Lists can contain any value type and are dynamically sized. Can put as many different types as needed in the same list as well as other lists and even a reference to itself. It is definitely convenient and time-saving not having to worry about types for storing variables. It seems like this kind of flexibility might make things more bug prone though.

### Tuples
Set of elements that can't be modified, but can be of any number of types. This type is in C++ standard library, but is type dependent.

### Slices
Built in support for subsets and sequences. In C++, this would need to be done using iterators and a loop--more code. Another time saver and less verbose code.

### Index Range Checking
Errors are given for going out of range for container types. This is not done for C++ arrays (allowing for runtime bugs with no errors) but is done for most other containers like vectors. Noticed that negative values can be used as indices to start from the end of a container.

### Dictionaries
Hash map data type. Keys must be immutable. Not much different here other than the syntax and dynamic typing. Printing the dictionary can be done without needing to create a helper function.

### If Statement
Works as expected with different syntax. Not sure if I like or dislike the elif shorthand.

### Switch Statement
Does not exist by default.

### For Loop
Works similarly to the range based for loop in C++11. More flexible in terms of what objects can be iterated over. An else block can be added after the loop to run only after the loop completes successfully. For loops can be used when defining a container. C++ range for loop feels much more restricted than in Python.

### While Loop
This loop type is much more similar to its C++ counterpart, but also has the else block functionality.

### Indentation to Denote Code Blocks
Whitespace is used for denoting code blocks rather than curly braces. When writing C++, code blocks are also generally indented, but this is for legibility and not as a matter of function. Modern IDEs trivialize the formatting for us, so the ease of use is similar. After getting used to Python's use of whitespace, I am not swayed one way or the other. I think the consistency of the individual programmer's style is what matters for legibility.

### Type Binding
This is one of the most--if not THE most--significant difference between Python and C++, which was apparent through most of the other features. The lack of static typing reduces the amount of needed code significantly and adds to the flexibility of variables and functions. This is what made it difficult for me to read Python code. The lack of types and lack of verbose code actually made it harder for me to understand Python at first. More is left to the programmer for ensuring documentation and legibility. I can see lots of potential for runtime errors coming from dynamic typing.

### Type Checking
Variable types are checked with the type() and isinstance() functions. C++ is strictly typed, so everything is explicitly defined and checked at compile time. Checking the type of a variable is seldom needed because of this. I would imagined checking object types is more common in Python due to dynamic types.

### Functions
* Python allows for assigning default values to parameters.
* All arguments passed by reference--no pass by value. The caller needs to backup data if it needs to be preserved from a function that might modify it.
* Functions themselves are objects that can be returned or assigned.
Once again Python favors flexibility while C++ favors safety and efficiency. This is highlighted by the lack of pass by reference and the lack of const member functions. Being able to use functions like other objects is a huge boon for flexibility.

### Other - Exception Handling
Python supports error handling with the try, except, finally blocks. Works similarly to try, catch blocks. There is the additional option of the finally clause which always executes if there was an exception or not.
