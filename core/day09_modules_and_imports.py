# =====================================================
# Day 9 — Modules & Imports
# =====================================================
# This is a LEARNING + PRACTICE file.
# It demonstrates concepts AND implements given tasks.
# Real tools will later split this into multiple files.
# =====================================================


# -----------------------------------------------------
# Phase 0 — Mental Model
# -----------------------------------------------------
# module  → one .py file
# import  → loading that file into another file
# Real tools are multi-file
# Bad imports cause crashes & side effects


# -----------------------------------------------------
# Phase 1 — Built-in Modules
# -----------------------------------------------------

import math
# math → built-in module for mathematical operations
print(math.sqrt(16))          # sqrt() → square root

from math import sqrt
# selective import
print(sqrt(25))

import random as rnd
# alias import
print(rnd.randint(1, 10))     # random integer


# -----------------------------------------------------
# Phase 2 — Custom Module (utils.py)
# -----------------------------------------------------
# utils.py must exist in same folder and contain:
# def banner():
# def add(a, b):

import utils

utils.banner()
print(utils.add(5, 7))


# -----------------------------------------------------
# Phase 3 — __name__ == "__main__"
# -----------------------------------------------------
# __name__ → built-in variable
# "__main__" → entry point identifier

def demo_main():
    print("Main Logic Running")

if __name__ == "__main__":
    demo_main()


# -----------------------------------------------------
# Phase 4 — sys Module (CLI control)
# -----------------------------------------------------
import sys
# sys.argv → command-line arguments
# argv[0] → script name
# argv[1:] → user input (always strings)

print("CLI arguments:", sys.argv)


# =====================================================
# TASK 1 — CLI TOOL (Addition using utils)
# =====================================================
# Requirements:
# - Use sys.argv
# - Take 2 numbers from CLI
# - Use utils.add()
# - Fail safely

if len(sys.argv) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = utils.add(num1, num2)
        print("TASK 1 RESULT (sum):", result)
    except ValueError:
        print("TASK 1 ERROR: Numbers required")
else:
    print("TASK 1 USAGE: python file.py <num1> <num2>")


# -----------------------------------------------------
# Phase 5 — os Module (OS interaction)
# -----------------------------------------------------
import os
# os → operating system interface

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir())


# =====================================================
# TASK 2 — FILE CHECK TOOL
# =====================================================
# Requirements:
# - Take filename from CLI
# - Check existence
# - Identify file or directory
# - Exit safely

if len(sys.argv) >= 2:
    filename = sys.argv[1]

    if os.path.exists(filename):
        print(f"TASK 2: '{filename}' exists")

        if os.path.isfile(filename):
            print("It is a file")
        elif os.path.isdir(filename):
            print("It is a directory")
    else:
        print(f"TASK 2: '{filename}' does NOT exist")
else:
    print("TASK 2 USAGE: python file.py <filename>")


# =====================================================
# Day 9 Summary — New Keywords & Concepts
# =====================================================
# import             → load module
# from               → selective import
# as                 → alias
# module             → reusable .py file
# __name__           → built-in variable
# "__main__"         → entry-point identifier
# sys                → system interaction
# sys.argv           → CLI arguments
# os                 → OS interaction
# os.getcwd()        → current directory
# os.listdir()       → list directory contents
# os.path.exists()   → existence check
# os.path.isfile()   → file check
# os.path.isdir()    → directory check
#
# SECURITY NOTES:
# - CLI input is untrusted
# - Always validate arguments
# - Never auto-execute imported modules
# - Structure prevents bugs and misuse
# =====================================================
