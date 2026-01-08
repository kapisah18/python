"""
========================================================
DAY 3 — LOOPS & ITERATIONS IN PYTHON
========================================================

Loops allow us to repeat a block of code.

Two main loop types:
1. for loop   → iterate over a sequence (list, string, range)
2. while loop → run until a condition becomes False

IMPORTANT:
----------
Indentation defines what belongs inside a loop.
"""

# ======================================================
# 1. BASIC FOR LOOP (RECAP)
# ======================================================

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

"""
OUTPUT:
1
2
3
4
5

Explanation:
- num takes each value from nums one by one
- Loop runs exactly 5 times (length of list)
"""


# ======================================================
# 2. BREAK STATEMENT
# ======================================================

for num in nums:
    if num == 3:
        print("Found 3")
        break
    print(num)

"""
OUTPUT:
1
2
Found 3

Explanation:
- Loop prints 1 and 2
- When num == 3:
  - prints "Found 3"
  - break exits the loop immediately
- 4 and 5 are never reached
"""


# ======================================================
# 3. CONTINUE STATEMENT
# ======================================================

for num in nums:
    if num == 3:
        print("Found 3")
        continue
    print(num)

"""
OUTPUT:
1
2
Found 3
4
5

Explanation:
- continue skips ONLY the current iteration
- 3 is not printed
- Loop continues normally after that
"""


# ======================================================
# BREAK vs CONTINUE (CORE DIFFERENCE)
# ======================================================

"""
break    → exits the loop completely
continue → skips current iteration only
"""


# ======================================================
# 4. NESTED LOOPS (LOOP INSIDE LOOP)
# ======================================================

for num in nums:
    for letter in "ABC":
        print(num, letter)

"""
OUTPUT:
1 A
1 B
1 C
2 A
2 B
2 C
...
5 C

Explanation:
- Outer loop controls numbers
- Inner loop runs fully for EACH number
- Total iterations = 5 × 3 = 15
"""


# ======================================================
# 5. NESTED LOOP — STRING + STRING
# ======================================================

username = "ab"
digits = "12"

for char in username:
    for d in digits:
        print(char + d)

"""
OUTPUT:
a1
a2
b1
b2

Explanation:
- Generates all possible combinations
- Very common in brute-force / pattern logic
"""


# ======================================================
# 6. LOOPING THROUGH STRINGS
# ======================================================

word = "Python"

for ch in word:
    print(ch)

"""
OUTPUT:
P
y
t
h
o
n

Explanation:
- Strings are iterable
- Loop runs once per character
"""


# ======================================================
# 7. STRING LOOP WITH CONDITION
# ======================================================

password = "p@ssw0rd"

for ch in password:
    if ch.isdigit():
        print("Digit found:", ch)

"""
OUTPUT:
Digit found: 0

Explanation:
- isdigit() checks if character is numeric
- Useful for password validation
"""


# ======================================================
# 8. USING range() WITH FOR LOOPS
# ======================================================

for i in range(10):
    print(i)

"""
OUTPUT:
0
1
2
3
4
5
6
7
8
9

Explanation:
- range(10) → generates 0 to 9
- Total iterations = 10
"""


# ======================================================
# 9. range(start, stop)
# ======================================================

for i in range(1, 11):
    print(i)

"""
OUTPUT:
1
2
3
4
5
6
7
8
9
10

Explanation:
- Starts at 1
- Stops BEFORE 11
"""


# ======================================================
# 10. WHILE LOOP (CONDITION-BASED)
# ======================================================

x = 0

while x < 5:
    print(x)
    x += 1

"""
OUTPUT:
0
1
2
3
4

Explanation:
- Loop runs while condition is True
- x += 1 is REQUIRED
- Without increment → infinite loop
"""


# ======================================================
# 11. BREAK INSIDE WHILE LOOP
# ======================================================

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

"""
OUTPUT:
0
1
2
3
4

Explanation:
- Loop exits when x == 5
"""


# ======================================================
# 12. INFINITE LOOP (CONTROLLED)
# ======================================================

x = 0

while True:
    if x == 3:
        break
    print(x)
    x += 1

"""
OUTPUT:
0
1
2

Explanation:
- while True → infinite loop
- break provides exit condition
"""


# ======================================================
# 13. DANGEROUS INFINITE LOOP (DO NOT RUN)
# ======================================================

"""
while True:
    print("Running forever")
"""

"""
Explanation:
- No condition
- No break
- Loop NEVER ends
- Stop using CTRL + C
"""


# ======================================================
# DAY 3 — FINAL SUMMARY
# ======================================================

"""
WHAT WE LEARNED:
----------------
1. for loop → iterate over sequences
2. while loop → condition-based repetition
3. break → exit loop completely
4. continue → skip current iteration
5. Nested loops → generate combinations
6. Strings are iterable
7. range() → controlled numeric loops
8. while True → infinite loops (dangerous without break)

REAL-WORLD NOTES:
-----------------
- break saves CPU and time
- Nested loops grow exponentially
- String loops are common in validation
- Infinite loops must ALWAYS have exit logic
"""

# ===================== END OF DAY 3 =====================
