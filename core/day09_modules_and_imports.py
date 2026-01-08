# =====================================================
# Day 09 — Modules & Imports (Clean + Structured)
# =====================================================
# Goal:
# Learn how Python uses modules to organize real programs,
# reuse code, and access built-in tools safely.
# =====================================================


# =====================================================
# TOPIC 1: What is a Module?
# =====================================================
# Definition:
# A module is a Python file (.py) that contains reusable code
# such as functions, variables, or classes.
#
# Real-time examples:
# - auth.py      → login logic
# - scanner.py   → port scanning logic
# - utils.py     → helper functions
#
# Why it matters:
# - Large programs are split into files
# - Reuse code without copy-paste
# - Cleaner and safer structure
# =====================================================


# =====================================================
# TOPIC 2: Importing a Custom Module (Same Folder)
# =====================================================
# Assume this file exists in the SAME directory:
#
# my_module.py
# -----------------------------
# test = "Test String"
#
# def find_index(sequence, target):
#     """Return index of target or -1 if not found"""
#     for i, value in enumerate(sequence):
#         if value == target:
#             return i
#     return -1
# -----------------------------

import my_module
# IMPORTANT:
# - Python runs ALL top-level code in my_module ONCE
# - Functions/variables become available after import

courses = ["History", "Math", "Physics", "CompSci"]

index = my_module.find_index(courses, "Math")
print(index)   # Output: 1


# =====================================================
# TOPIC 3: import as (Alias)
# =====================================================
# Definition:
# import module as alias
#
# Why it matters:
# - Shorter names
# - Improves readability
#
# Real-time examples:
# import numpy as np
# import pandas as pd
# =====================================================

import my_module as mm

print(mm.find_index(courses, "Physics"))  # Output: 2


# =====================================================
# TOPIC 4: from module import specific items
# =====================================================
# Definition:
# Import ONLY what you need from a module
#
# Why it matters:
# - Cleaner namespace
# - Easier debugging
# =====================================================

from my_module import find_index, test

print(find_index(courses, "CompSci"))  # Output: 3
print(test)                            # Output: Test String


# =====================================================
# TOPIC 5: Why NOT to use import *
# =====================================================
# from my_module import *
#
# Problems:
# - You don’t know where names came from
# - Debugging becomes hard
# - Can overwrite existing variables
#
# Rule:
# ❌ Avoid in real projects
# =====================================================


# =====================================================
# TOPIC 6: How Python Finds Modules (sys.path)
# =====================================================
# Definition:
# sys.path is a list of directories Python searches for modules
#
# Search order:
# 1. Current script directory
# 2. PYTHONPATH environment variable
# 3. Standard Library
# 4. site-packages (installed libraries)
#
# Why it matters:
# - Explains "ModuleNotFoundError"
# - Critical for multi-file projects
# =====================================================

import sys

print(sys.path)   # Shows search locations


# =====================================================
# TOPIC 7: Standard Library (Real Tools)
# =====================================================
# Definition:
# Standard library = built-in modules shipped with Python
#
# Why it matters:
# - No installation required
# - Secure and optimized
# - Used in production everywhere
# =====================================================

# ---------- random ----------
import random
print(random.choice(courses))  # Random item from list


# ---------- math ----------
import math
radians = math.radians(90)
print(radians)                 # 1.5707...
print(math.sin(radians))       # 1.0


# ---------- datetime ----------
from datetime import date
print(date.today())            # Today's date


# ---------- calendar ----------
import calendar
print(calendar.isleap(2020))   # True
print(calendar.isleap(2017))   # False


# ---------- os ----------
import os
print(os.getcwd())             # Current working directory


# =====================================================
# TOPIC 8: __name__ == "__main__"
# =====================================================
# Definition:
# Prevents code from running automatically on import
#
# Why it matters:
# - Safe imports
# - Required for real applications
# =====================================================

def main():
    print("Main program running")

if __name__ == "__main__":
    main()



# =====================================================
# FINAL SUMMARY — Day 09
# =====================================================
# module             → reusable file
# import             → load module
# import as          → alias
# from x import y    → selective import
# sys.path           → module search path
# standard library   → built-in tools
# __name__ check     → safe execution
# os                 → OS interaction
#
# INDUSTRY TRUTH:
# - Bad imports cause bugs
# - Structure = security
# - Clean modules scale
# =====================================================
