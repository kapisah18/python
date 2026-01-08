# =================================================
# Day 2 — if / else (Decision Making & Control Flow)
# =================================================

# -----------------------------
# Basic decision making
# -----------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# -----------------------------
# Multiple conditions using elif
# -----------------------------
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")


# -----------------------------
# Logical operators (authentication example)
# -----------------------------
username = input("Username: ")
password = input("Password: ")

if not password:
    print("Password cannot be empty")
elif username == "admin" and password == "root":
    print("Access Granted")
else:
    print("Invalid credentials")


# -----------------------------
# Nested if (age-based access)
# -----------------------------
if age >= 18:
    if age >= 21:
        print("Can drink legally")
    else:
        print("Adult but cannot drink legally")
else:
    print("Minor")
