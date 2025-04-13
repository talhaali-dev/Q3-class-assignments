"""
Practice Code for:
- Modules & Functions
- Exception Handling
- File Handling
- Math, Date Time, and Calendar
"""

# ===============================
# Section 1: Modules & Functions
# ===============================
import math
import datetime
import calendar

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def factorial(n):
    """Return the factorial of n using the math module."""
    return math.factorial(n)

def is_even(n):
    """Return True if n is an even number, otherwise False."""
    return n % 2 == 0

print("=== Modules & Functions ===")
print("Addition of 5 and 3:", add(5, 3))
print("Factorial of 5:", factorial(5))
print("Is 4 even?", is_even(4))


# ============================
# Section 2: Exception Handling
# ============================
print("\n=== Exception Handling ===")
def safe_divide(a, b):
    """Divide a by b and handle division errors."""
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error:", e)
        result = None
    except Exception as e:
        print("Unexpected error:", e)
        result = None
    finally:
        print("Division attempted between", a, "and", b)
    return result

print("10 divided by 2:", safe_divide(10, 2))
print("10 divided by 0:", safe_divide(10, 0))


# =======================
# Section 3: File Handling
# =======================
print("\n=== File Handling ===")
filename = "practice_file.txt"

# Write text to a file
with open(filename, "w") as file:
    file.write("Hello, this is a practice file for Python File Handling.\n")
    file.write("This line demonstrates writing to a file.")

# Read and display the contents of the file
with open(filename, "r") as file:
    content = file.read()
    print("File Contents:")
    print(content)


# =============================================
# Section 4: Math, Date Time, and Calendar
# =============================================
print("\n=== Math, Date Time, & Calendar ===")

# Math operations
number = 16
print("Square root of", number, ":", math.sqrt(number))
print("Value of pi:", math.pi)

# Date and time operations
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Calendar operations
year = now.year
month = now.month
print("\nCalendar for {}/{}:".format(month, year))
print(calendar.month(year, month))
