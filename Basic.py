# Python: Python is a popular programmimg lanagguage. It was created by Guido Van Russum. It was released in 1991.
    # It is widely used in web development, machine learning, software development, Bioinformatics etc. 
    # Python relies on indentation, with whitespaces.
    # Check the installed python version: 
import sys
print(sys.version)
# File extension for python is .py for examaple Basic.py
# Comments can be used to explain Python code. Comments starts with a #.
print("Hello, World!") # Print Hello, World!

# Python Variables:
    # Variables are containers for storing data values.
    # Example
x=5
y="Mostafij"
print(x)
print(y)
# Variables do not need to be declared with any particular type
x=3 #Integer
x="Mostafij" # Now String
print(x)
# If you want to specify the data type of a variable, this can be done with casting.
x=int(3) #Integer
y=str(3) #String
z=float(3) #Float
print(x,y,z)
# You can get the data type of a variable with the type() function
type(z) # type is float
print(type(z))
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.
# Example 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
myVariableName = "John" # Camel Case (Except first word start with Capital)
MyVariableName = "John" # Pascal Case (Each word start with Capital)
my_variable_name = "John" # Snake Case (Each word seperated with underscore)

# Assign values to multiple variables
x,y,z="Orange", "Banana", "Mango"
print(x)
print(y)
print(z)
# Assign one valu to multiple variables
x=y=z="Orange"
print(x)
print(y)
print(z)
# Unpacking: Python allows you to extract the values into variables from list and  tuple. This is called unpacking.
fruits=["apple", "banana", "orange"] # Unpacking from list
x,y,z=fruits
print(x)
print(y)
print(z)

# Output Variable: Python print() function is often used to output variables.
X="I want to learn python for machine learning and Bioinformatics"
print(X) # Output

# Global Variable: Variables that are created outside of a function are known as global variables.
    # Global variables can be used by everyone, both inside of functions and outside.
# Create a function inside a function and use it in global and inside function
x="Machine Learning and Bioinformatics"
def myfunction():
    print("I want to learn python for "+ x)
myfunction()
# If you create a variable with the same name inside a function, this variable will be local
# The global variable with the same name will remain as it was, global and with the original value.
x="Cancer Research"
def my_function():
    print("I want to learn python programming for ", x)
my_function()
print("I want to learn python programming for ", x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

# Programming has three phase
    # Input phase
num1=int(input("Enter 1st number: ")) # int() function convert input string to integer
num2=int(input("Enter 2nd number: "))
    # Processing phase
result=num1+num2
    # Output phase
print(result)