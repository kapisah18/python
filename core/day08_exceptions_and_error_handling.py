# =====================================================
# Day 8 — Exceptions & Error Handling (FIXED VERSION)
# =====================================================


# -----------------------------------------------------
# 1. Basic exception handling
# -----------------------------------------------------
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
# 2. Catching multiple exceptions
# -----------------------------------------------------
try:
    data = int("abc") / 0
except (ValueError, ZeroDivisionError) as error:
    print("Error occurred:", error)


# -----------------------------------------------------
# 3. Raising exceptions SAFELY (FIXED)
# -----------------------------------------------------
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as error:
    print(error)


# -----------------------------------------------------
# 4. Custom exception
# -----------------------------------------------------
class WeakPasswordError(Exception):
    pass

password = "123"

try:
    if len(password) < 6:
        raise WeakPasswordError("Password too short")
except WeakPasswordError as error:
    print(error)


# -----------------------------------------------------
# 5. Practice Task — Safe division
# -----------------------------------------------------
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
# 6. Practice Task (Advanced) — Custom age validation
# -----------------------------------------------------
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")

    print("Valid age entered:", age)

except ValueError:
    print("Age must be a number")

except InvalidAgeError as error:
    print(error)


# =====================================================
# End of Day 8 — Program runs fully
# =====================================================
