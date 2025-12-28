# file_check.py
# Checks file or directory existence using os module

import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python file_check.py <path>")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"'{path}' does not exist")
        sys.exit(0)

    if os.path.isfile(path):
        print(f"'{path}' exists and is a FILE")
    elif os.path.isdir(path):
        print(f"'{path}' exists and is a DIRECTORY")

# Entry point
if __name__ == "__main__":
    main()

    
"""Why this matters

No assumptions about path

Safe for automation

Works on Windows/Linux

No accidental execution on import

Run
python file_check.py auth.log"""