"""
================================================================
DAY 5 — LISTS, STRINGS, TUPLES & SETS (MERGED + EXPLAINED)
================================================================

This file keeps:
- ALL important examples from both source files
- NO concept duplication (examples may differ)
- Inline notes explaining WHAT each method/keyword does

Think of this as:
📘 Learning notes + 🧪 runnable examples
"""

# ==============================================================
# PART 1 — LISTS (Ordered + Mutable)
# ==============================================================

# [] → list literal
# A list stores ordered items and CAN be modified
courses = ["History", "Math", "Physics", "Computer Science"]
ports = [21, 22, 80, 443]

print(courses)
print(ports)

# len() → returns number of elements in a sequence
print(len(courses))


# --------------------------------------------------------------
# INDEXING
# --------------------------------------------------------------
# Index starts from 0

print(courses[0])     # First item
print(courses[-1])    # Last item (negative index = from end)


# --------------------------------------------------------------
# SLICING
# list[start:end] → end index NOT included
# --------------------------------------------------------------

print(courses[:2])    # From start to index 2 (excluded)
print(courses[2:])    # From index 2 to end


# ==============================================================
# PART 2 — MODIFYING LISTS
# ==============================================================

# append(value) → adds ONE item to the end
ports.append(8080)

# insert(index, value) → inserts without overwriting
ports.insert(1, 25)

# remove(value) → removes first matching value
ports.remove(80)

# del → deletes item by index
del ports[2]

print("Modified ports:", ports)


# --------------------------------------------------------------
# append() vs extend()
# --------------------------------------------------------------

courses_2 = ["Biology", "Chemistry"]

# append(list) → adds the LIST as a single element
courses.append(courses_2)
print("After append:", courses)

# pop() → removes last item AND returns it
courses.pop()

# extend(iterable) → adds each element individually
courses.extend(courses_2)
print("After extend:", courses)


# ==============================================================
# PART 3 — LOOPING & MEMBERSHIP
# ==============================================================

# for → loop keyword
# port → loop variable (name chosen by programmer)
# in → iteration / membership operator
for port in ports:
    print("Scanning port:", port)

# Membership check using `in`
if 22 in ports:
    print("SSH service detected")


# ==============================================================
# PART 4 — STRINGS (Immutable Sequences)
# ==============================================================

# Strings cannot be modified in place
username = "admin"

# Indexing strings (same rules as lists)
print(username[0])
print(username[-1])

# Slicing strings
print(username[1:4])   # 'dmi'

text = "   Admin Login Page   "

# lower() → converts to lowercase
print(text.lower())

# upper() → converts to uppercase
print(text.upper())

# strip() → removes leading/trailing whitespace
print(text.strip())

# replace(old, new) → replaces substring
print(text.replace("Login", "Access"))

# startswith(prefix) → checks beginning of string
if username.startswith("ad"):
    print("Likely admin user")


# ==============================================================
# PART 5 — STRINGS ↔ LISTS
# ==============================================================

data = "admin, root, user"

# split(delimiter) → string → list
raw_users = data.split(",")

# List comprehension:
# u → loop variable
# strip() → cleans whitespace
users = [u.strip() for u in raw_users]

print(users)

# join(separator) → list → string
print("-".join(users))


# ==============================================================
# PART 6 — SORTING & BUILT-IN FUNCTIONS
# ==============================================================

nums = [1, 5, 2, 4, 3]

# min() → smallest value
print("Min:", min(nums))

# max() → largest value
print("Max:", max(nums))

# sum() → total of elements
print("Sum:", sum(nums))

# sort() → modifies list in place
nums.sort()
print("Sorted nums:", nums)

# sorted() → returns new sorted list
sorted_desc = sorted(nums, reverse=True)
print("Sorted copy:", sorted_desc)


# ==============================================================
# PART 7 — FINDING VALUES
# ==============================================================

# index(value) → returns index (ValueError if not found)
print(courses.index("History"))

# in → returns True/False
print("Physics" in courses)
print("Math" in courses)


# ==============================================================
# PART 8 — ENUMERATE (Index + Value)
# ==============================================================

# enumerate(iterable) → returns (index, value)
for index, course in enumerate(courses):
    print(index, course)

# enumerate(start=1) → custom starting index
for index, course in enumerate(courses, start=1):
    print(index, course)


# ==============================================================
# PART 9 — TUPLES (Ordered + Immutable)
# ==============================================================

# () → tuple literal
tuple_1 = ("History", "Math", "Physics")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# ❌ Not allowed — tuples cannot be modified
# tuple_1[0] = "Art"


# --------------------------------------------------------------
# MUTABILITY COMPARISON
# --------------------------------------------------------------

list_1 = ["A", "B", "C"]
list_2 = list_1

list_1[0] = "Z"

# Both change because lists are mutable
print(list_1)
print(list_2)


# ==============================================================
# PART 10 — SETS (Unordered + Unique)
# ==============================================================

# {} with values → set literal
cs_courses = {"History", "Math", "Physics", "Computer Science"}

print(cs_courses)  # Order not guaranteed

# add(value) → adds item (duplicates ignored)
cs_courses.add("Math")

# in → fast membership test
print("Math" in cs_courses)


# --------------------------------------------------------------
# SET OPERATIONS
# --------------------------------------------------------------

art_courses = {"History", "Math", "Art", "Design"}

# intersection() → common values
print("Common:", cs_courses.intersection(art_courses))

# difference() → values in cs_courses but not in art_courses
print("Only CS:", cs_courses.difference(art_courses))

# union() → combines both sets
print("All courses:", cs_courses.union(art_courses))


# ==============================================================
# PART 11 — EMPTY COLLECTIONS (IMPORTANT GOTCHA)
# ==============================================================

empty_list = []        # or list()
empty_tuple = ()      # or tuple()

# {} → creates DICTIONARY, not set
empty_set = set()     # correct way

print(type(empty_list))
print(type(empty_tuple))
print(type(empty_set))


# ==============================================================
# PART 12 — MINI SECURITY-STYLE TASK
# ==============================================================

valid_users = ["admin", "root", "user", "hash", "guest"]

# input() → always returns string
# lower() → normalize case for safe comparison
input_user = input("Enter username: ").lower()

if input_user in valid_users:
    print("User found")
else:
    print("User not found")


"""
FINAL TAKEAWAYS:
----------------
- Lists → mutable, ordered
- Tuples → immutable, ordered
- Sets → unordered, unique, fastest lookup
- append vs extend is CRITICAL
- sort() modifies, sorted() does not
- split + strip + lower = safe input handling
- {} ≠ empty set
"""
"""
==============================================================
SUMMARY — WHAT WE LEARNED IN DAY 5
==============================================================

1. LISTS
- Ordered and mutable (can change after creation)
- Created using []
- Support indexing, slicing, looping
- Common methods:
  - append()  → add ONE item at end
  - insert()  → add item at specific index
  - extend()  → add multiple items from another iterable
  - remove()  → remove by value
  - pop()     → remove & return last item
  - sort()    → sort list in place
- sorted() returns a NEW sorted list (does not modify original)

2. STRINGS
- Ordered but IMMUTABLE (cannot change in place)
- Support indexing and slicing like lists
- Important methods:
  - lower(), upper()  → case normalization
  - strip()          → remove extra whitespace
  - replace()        → substitute text
  - startswith()     → prefix checking
- split() converts string → list
- join() converts list → string

3. LIST + STRING COMBINATION
- split + strip + lower = clean & safe input handling
- List comprehension = compact, readable data processing

4. TUPLES
- Ordered and IMMUTABLE
- Created using ()
- Cannot be modified after creation
- Useful when data must not change

5. SETS
- Unordered collections with NO duplicates
- Created using {} (with values) or set()
- Extremely fast membership checks using `in`
- Useful operations:
  - intersection() → common values
  - difference()   → unique values
  - union()        → combine sets

6. KEY GOTCHAS
- append() ≠ extend()
- sort() ≠ sorted()
- {} creates a DICTIONARY, not a set
- input() always returns string
- Lists are mutable, tuples are not

7. SECURITY MINDSET TAKEAWAYS
- Always normalize input (lower, strip)
- Use sets for fast membership checks
- Be careful with mutable objects sharing references
- Clean data before comparison or validation

==============================================================
END OF DAY 5
==============================================================
"""
