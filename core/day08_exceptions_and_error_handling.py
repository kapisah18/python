# =====================================================
# Day 8 — Exceptions & Error Handling
# =====================================================
# Exceptions are runtime errors that stop program execution.
# Error handling allows programs to fail safely instead of crashing.
#
# In cybersecurity, exception handling is critical for:
# - input validation
# - preventing crashes
# - secure logging
# - controlled failure
# =====================================================


# -----------------------------------------------------
# 1. Basic exception handling
# -----------------------------------------------------
# try     → wrap risky code
# except  → handle specific errors
# else    → runs only if no error occurs
# finally → always runs (cleanup, logging)

try:
    x = int(input("Enter number: "))
    print(10 / x)

except ValueError:
    print("Input must be a number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("No error occurred")

finally:
    print("Execution finished")


# -----------------------------------------------------
# 2. Catching multiple exceptions together
# -----------------------------------------------------
# Useful when different errors require the same handling

try:
    data = int("abc") / 0
except (ValueError, ZeroDivisionError) as error:
    print("Error occurred:", error)

# as error → stores exception message for logging/debugging


# -----------------------------------------------------
# 3. Raising exceptions manually
# -----------------------------------------------------
# raise → forces an exception when data is logically invalid

try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as error:
    print(error)


# Use raise when bad data must NEVER be accepted


# -----------------------------------------------------
# 4. Custom (user-defined) exceptions
# -----------------------------------------------------
# Custom exceptions improve clarity and security auditing

class WeakPasswordError(Exception):
    pass
# pass → empty class body (inherits behavior from Exception)
# Using the custom exception

password = "123"

try:
    if len(password) < 6:
        raise WeakPasswordError("Password too short")
except WeakPasswordError as error:
    print(error)
# -----------------------------------------------------
# 5. Common beginner mistakes (DO NOT DO THIS)
# -----------------------------------------------------
# ❌ except without specifying error
# ❌ swallowing errors silently
# ❌ using exceptions instead of validation

# Bad example:
# try:
#     x = 1 / 0
# except:
#     pass


# -----------------------------------------------------
# 6. Practice Task — Safe division
# -----------------------------------------------------
# Requirements:
# - Take two numbers from user
# - Handle non-numeric input
# - Handle division by zero
# - Always execute cleanup message

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

finally:
    print("Execution completed")



# -----------------------------------------------------
# 7. Practice Task (Advanced) — Custom age validation
# -----------------------------------------------------
# Enforcing strict data rules using custom exceptions
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age <= 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")

    print("Valid age entered:", age)

except ValueError:
    print("Age must be a number")

except InvalidAgeError as error:
    print(error)


# =====================================================
# Day 8 Summary — New Keywords & Concepts
# =====================================================
# try        → risky code block
# except     → catches specific exceptions
# else       → runs if no exception occurs
# finally    → always runs
# raise      → manually trigger an exception
# Exception  → base class for all errors
# class      → used to create custom exceptions
# pass       → empty placeholder
#
# SECURITY NOTES:
# - Never trust user input
# - Fail safely, not silently
# - Use specific exceptions
# - Exceptions = controlled failure
# =====================================================