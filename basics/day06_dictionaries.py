"""
========================================================
DAY 6 — DICTIONARIES IN PYTHON (PRIMARY: TRANSCRIPT)
========================================================

Dictionaries store data as KEY : VALUE pairs.
Also known as:
- HashMaps
- Associative Arrays

MENTAL MODEL:
-------------
Like a real dictionary:
word  -> definition
(key) -> (value)

RULES:
------
- Keys are UNIQUE
- Keys must be IMMUTABLE
- Values can be ANY data type
"""

# ======================================================
# 1. CREATING A DICTIONARY (PRIMARY)
# ======================================================

# {} → dictionary literal
student = {
    "name": "John",                     # str value
    "age": 25,                          # int value
    "courses": ["Math", "Computer Science"]  # list value
}

print(student)


# ======================================================
# 2. ACCESSING VALUES USING KEYS (PRIMARY)
# ======================================================

# dict[key] → direct access
print(student["name"])
print(student["courses"])

# NOTE:
# Values can be string, int, list, dict, etc.


# ======================================================
# 3. KEYS CAN BE OTHER IMMUTABLE TYPES (PRIMARY)
# ======================================================

student_alt = {
    1: "John",      # integer key
    "age": 25
}

print(student_alt[1])

# BEST PRACTICE:
# Use strings for keys for clarity and readability


# ======================================================
# 4. ACCESSING A NON-EXISTING KEY (PRIMARY)
# ======================================================

# ❌ Raises KeyError (program crashes)
# print(student["phone"])


# ======================================================
# 5. SAFE ACCESS USING get() (PRIMARY)
# ======================================================

# get(key) → returns value or None
print(student.get("name"))
print(student.get("phone"))

# get(key, default) → custom fallback value
print(student.get("phone", "Not Found"))

# WHY THIS MATTERS:
# -----------------
# dict[key] → crash if missing
# get()     → safe, controlled behavior


# ======================================================
# 6. ADDING NEW KEY-VALUE PAIRS (PRIMARY)
# ======================================================

student["phone"] = "5555555"
print(student)

# If key exists → value is UPDATED
student["name"] = "Jane"
print(student)


# ======================================================
# 7. UPDATING MULTIPLE VALUES USING update() (PRIMARY)
# ======================================================

student.update({
    "name": "Jane",
    "age": 26,
    "phone": "5555555"
})

print(student)


# ======================================================
# 8. DELETING KEYS (PRIMARY)
# ======================================================

# del → removes key-value pair
del student["age"]
print(student)


# ======================================================
# 9. pop() — REMOVE + RETURN (PRIMARY)
# ======================================================

# pop(key) → removes AND returns value
phone = student.pop("phone")
print("Popped phone:", phone)
print(student)


# ======================================================
# 10. DICTIONARY SIZE (PRIMARY)
# ======================================================

# len() → number of keys
print(len(student))


# ======================================================
# 11. KEYS, VALUES, ITEMS (PRIMARY)
# ======================================================

print(student.keys())    # all keys
print(student.values())  # all values
print(student.items())   # (key, value) pairs


# ======================================================
# 12. LOOPING THROUGH DICTIONARIES (PRIMARY)
# ======================================================

# Looping directly → keys only
for key in student:
    print("Key:", key)

# Looping using items() → key + value
for key, value in student.items():
    print(key, ":", value)


# ======================================================
# SECONDARY — PRACTICAL / SECURITY EXAMPLES
# (Supportive, NOT primary teaching)
# ======================================================

user = {
    "username": "admin",
    "role": "root",
    "active": True
}

# Safe key check
if "role" in user:
    print("Role exists")

# Nested dictionary (real-world structure)
users_info = {
    "admin": {"role": "root", "active": True},
    "guest": {"role": "user", "active": False}
}

print(users_info["admin"]["role"])


# ======================================================
# AUTHENTICATION EXAMPLE (SECONDARY BUT IMPORTANT)
# ======================================================

users = {
    "admin": "root",
    "user": "1234",
    "guest": "guest"
}

username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

# Exact key-value pairing check
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid login")


# WHY THIS IS CORRECT:
# -------------------
# - username must exist as a KEY
# - password is fetched ONLY for that key
# - prevents credential mixing


# ======================================================
# ADVANCED — NESTED LOGIN STRUCTURE (SECONDARY)
# ======================================================

players = {
    "player1": {"username": "player_1", "password": "root123"},
    "player2": {"username": "player_2", "password": "root456"}
}

username = input("Enter player username: ").strip()
password = input("Enter player password: ").strip()

login_success = False

for player in players.values():
    if player["username"] == username and player["password"] == password:
        login_success = True
        break

print("Login successful" if login_success else "Invalid login")


# ======================================================
# DAY 6 — FINAL SUMMARY
# ======================================================

"""
WHAT WE LEARNED (TRANSCRIPT-ALIGNED):
------------------------------------
1. Dictionaries store KEY → VALUE pairs
2. Keys are unique and immutable
3. Values can be any data type
4. dict[key] → direct access (unsafe if missing)
5. get() → safe access with default
6. Assigning to a key adds or updates data
7. update() → modify multiple entries at once
8. del → delete key-value pair
9. pop() → delete and return value
10. len() → number of keys
11. keys(), values(), items() → dictionary views
12. Looping directly gives keys
13. items() is best for key-value loops
14. Nested dictionaries model real-world data

SECURITY MINDSET:
----------------
- Never assume a key exists
- Always validate before access
- Authentication depends on EXACT key-value pairing
"""

# ===================== END OF DAY 6 =====================
