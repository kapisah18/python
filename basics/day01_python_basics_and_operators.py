"""
========================================
DAY 1 — PYTHON BASICS & OPERATORS
========================================

This file explains:
- Variables & keywords
- Data types
- Input & casting
- Arithmetic, comparison, bitwise operators

Read comments carefully — they explain WHAT and WHY.
"""

# -------------------------------------
# 1. OUTPUT FUNCTION
# -------------------------------------

# print() → built-in function to display output on screen
print("Hello Arsh")


# -------------------------------------
# 2. VARIABLES & ASSIGNMENT
# -------------------------------------

# =  → assignment operator (stores value in variable)

name = "Arsh"        # str  → text
age = 26             # int  → whole number
height = 5.9         # float → decimal number
is_student = True    # bool → True / False

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# -------------------------------------
# 3. DATA TYPES
# -------------------------------------

# type() → tells the data type of a variable
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>


# -------------------------------------
# 4. USER INPUT & TYPE CASTING
# -------------------------------------

# input() → takes input from user
# ALWAYS returns string (str)

username = input("Enter your name: ")
print("Welcome", username)

# int() → type casting (string → integer)
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)


# -------------------------------------
# 5. BASIC ARITHMETIC OPERATORS
# -------------------------------------

x = 10
y = 3

# +  → addition
print("Sum =", x + y)

# -  → subtraction
print("Difference =", x - y)

# *  → multiplication
print("Product =", x * y)

# /  → division (always returns float in Python 3)
print("Division =", x / y)


# -------------------------------------
# 6. ARITHMETIC WITH USER INPUT
# -------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition (+) =", num1 + num2)
print("Subtraction (-) =", num1 - num2)
print("Multiplication (*) =", num1 * num2)
print("Division (/) =", num1 / num2)

# // → floor division (drops decimal)
print("Floor Division (//) =", num1 // num2)

# % → modulus (remainder after division)
print("Modulus (%) =", num1 % num2)

# ** → exponent (power)
print("Exponentiation (**) =", num1 ** num2)

print("Average =", (num1 + num2) / 2)


# -------------------------------------
# 7. BUILT-IN MATH FUNCTIONS
# -------------------------------------

# max() → returns larger value
print("Max =", max(num1, num2))

# min() → returns smaller value
print("Min =", min(num1, num2))

# abs() → absolute value (removes negative sign)
print("Absolute num1 =", abs(num1))

# round() → rounds number
print("Rounded num1 =", round(num1))

# pow(a, b) → a raised to power b
print("Power using pow() =", pow(num1, num2))

# ** 0.5 → square root trick
print("Square root num1 =", num1 ** 0.5)

# divmod(a, b) → returns (quotient, remainder)
print("Divmod result =", divmod(num1, num2))


# -------------------------------------
# 8. COMPARISON OPERATORS
# (Return Boolean: True / False)
# -------------------------------------

# == → equal to
print("num1 == num2 :", num1 == num2)

# != → not equal to
print("num1 != num2 :", num1 != num2)

# >  → greater than
print("num1 > num2 :", num1 > num2)

# <  → less than
print("num1 < num2 :", num1 < num2)

# >= → greater than or equal to
print("num1 >= num2 :", num1 >= num2)

# <= → less than or equal to
print("num1 <= num2 :", num1 <= num2)


# -------------------------------------
# 9. BITWISE OPERATORS (LOW-LEVEL LOGIC)
# -------------------------------------
# Mostly used in flags, permissions, networking, security

# & → AND (both bits must be 1)
print("Bitwise AND (&) =", num1 & num2)

# | → OR (any bit is 1)
print("Bitwise OR (|) =", num1 | num2)

# ^ → XOR (bits must be different)
print("Bitwise XOR (^) =", num1 ^ num2)

# ~ → NOT (bit inversion)
print("Bitwise NOT (~) num1 =", ~num1)

# << → left shift (multiply by 2^n)
print("Left Shift (<<) num1 =", num1 << 1)

# >> → right shift (divide by 2^n)
print("Right Shift (>>) num1 =", num1 >> 1)


print("\nEnd of Day 1 — Python Basics & Operators")
