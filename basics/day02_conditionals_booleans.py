"""
========================================================
DAY 2 — CONDITIONALS & BOOLEANS IN PYTHON (CODE + NOTES)
========================================================

Conditionals control which code runs based on
whether expressions evaluate to True or False.

True / False values are called BOOLEANS.
"""

# ======================================================
# 1. BASIC IF STATEMENT
# ======================================================

# if → conditional keyword
# True → boolean literal

if True:
    print("Condition was True")

# This line runs ONLY if the condition is True


# ======================================================
# 2. IF WITH FALSE
# ======================================================

if False:
    print("This will NOT print")

# Nothing happens because condition is False


# ======================================================
# 3. REAL CONDITION (VARIABLE COMPARISON)
# ======================================================

language = "Python"

# == → equality operator (comparison)
# =  → assignment operator (DO NOT confuse)

if language == "Python":
    print("Language is Python")


# ======================================================
# 4. COMPARISON OPERATORS (REFERENCE)
# ======================================================

"""
==  → equal to
!=  → not equal to
>   → greater than
<   → less than
>=  → greater than or equal to
<=  → less than or equal to
is  → object identity (same memory)
"""

# NOTE:
# == checks VALUE equality
# is checks OBJECT identity (memory location)


# ======================================================
# 5. IF–ELSE STATEMENT
# ======================================================

language = "Java"

if language == "Python":
    print("Language is Python")
else:
    print("No match")

# else runs ONLY if if-condition is False


# ======================================================
# 6. IF–ELIF–ELSE (MULTIPLE CONDITIONS)
# ======================================================

language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")

# Python does NOT have switch-case
# if / elif / else replaces it cleanly


# ======================================================
# 7. BOOLEAN OPERATORS: and / or / not
# ======================================================

user = "admin"
logged_in = True

# and → ALL conditions must be True
if user == "admin" and logged_in:
    print("Admin page")
else:
    print("Bad credentials")


# ======================================================
# 8. OR OPERATOR
# ======================================================

logged_in = False

# or → ANY ONE condition must be True
if user == "admin" or logged_in:
    print("Admin page")
else:
    print("Access denied")


# ======================================================
# 9. NOT OPERATOR
# ======================================================

# not → flips boolean value
# not True  → False
# not False → True

if not logged_in:
    print("Please log in")
else:
    print("Welcome")


# ======================================================
# 10. OBJECT IDENTITY: is vs ==
# ======================================================

a = [1, 2, 3]
b = [1, 2, 3]

# == → values are equal
print(a == b)   # True

# is → same object in memory?
print(a is b)   # False


# ------------------------------------------------------
# Checking memory identity
# ------------------------------------------------------

print(id(a))
print(id(b))


# ======================================================
# 11. SAME OBJECT REFERENCE
# ======================================================

b = a

print(a is b)    # True
print(a == b)    # True

# is basically checks:
# id(a) == id(b)


# ======================================================
# 12. TRUTHY & FALSY VALUES
# ======================================================

"""
Python evaluates ONLY these as False:

False
None
0
0.0
''          (empty string)
[]          (empty list)
()          (empty tuple)
{}          (empty dictionary)
set()       (empty set)

EVERYTHING else is True
"""

# Generic test template
condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")


# ======================================================
# 13. NONE IS FALSE
# ======================================================

condition = None

if condition:
    print("True")
else:
    print("False")


# ======================================================
# 14. NUMBERS IN CONDITIONS
# ======================================================

condition = 0

if condition:
    print("True")
else:
    print("False")   # 0 is False

condition = 10

if condition:
    print("True")    # Any non-zero number is True


# ======================================================
# 15. EMPTY SEQUENCES
# ======================================================

condition = []

if condition:
    print("True")
else:
    print("False")   # Empty list is False

condition = ""

if condition:
    print("True")
else:
    print("False")   # Empty string is False


# ======================================================
# 16. EMPTY DICTIONARY
# ======================================================

condition = {}

if condition:
    print("True")
else:
    print("False")   # Empty dict is False


# ======================================================
# 17. NON-EMPTY STRING
# ======================================================

condition = "test"

if condition:
    print("True")    # Non-empty string is True
else:
    print("False")


# ======================================================
# WHY THIS MATTERS (IMPORTANT)
# ======================================================

"""
You can directly check:
- if list:
- if dict:
- if string:

No need for len() or extra checks.

This is VERY common in:
- input validation
- authentication logic
- API responses
- configuration checks
"""


# ======================================================
# DAY 7 — FINAL SUMMARY
# ======================================================

"""
WHAT WE LEARNED:
----------------
1. if executes code only when condition is True
2. else runs when if condition is False
3. elif allows multiple condition checks
4. == compares VALUES
5. is compares MEMORY ID
6. and → all must be True
7. or  → any one True
8. not → flips boolean
9. Empty values evaluate to False
10. Non-empty values evaluate to True
11. Conditionals rely on truthy / falsy logic

SECURITY / REAL-WORLD NOTES:
----------------------------
- Never assume truthiness blindly
- 0, None, empty values can break logic
- Use explicit checks when logic is critical
- is should NOT be used for value comparison
"""

# ===================== END OF DAY 7 =====================
