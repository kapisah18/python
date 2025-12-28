# cli_tool.py
# Adds two numbers passed via CLI using utils.add()

import sys
import utils

def main():
    # CLI validation
    if len(sys.argv) != 3:
        print("Usage: python cli_tool.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Error: both arguments must be numbers")
        sys.exit(1)

    utils.banner()
    result = utils.add(num1, num2)
    print("Result:", result)

# Entry point
if __name__ == "__main__":
    main()

    
"""Why this is production-safe

CLI input validated

Clean exits (sys.exit)

No code runs on import

Logic isolated in main()"""