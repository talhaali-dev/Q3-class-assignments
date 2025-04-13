# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 2. Assignment Operators
print("\n=== Assignment Operators ===")
x = 5
print("Initial value of x:", x)

x += 2
print("After x += 2:", x)

x *= 3
print("After x *= 3:", x)

x -= 4
print("After x -= 4:", x)

x /= 2
print("After x /= 2:", x)

# 3. Comparison Operators
print("\n=== Comparison Operators ===")
a = 7
b = 10

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 4. Logical Operators
print("\n=== Logical Operators ===")
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# 5. Identity Operators
print("\n=== Identity Operators ===")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

# 6. Membership Operators
print("\n=== Membership Operators ===")
numbers = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)
print("6 not in numbers:", 6 not in numbers)

string = "python"
print("'t' in string:", 't' in string)
print("'z' not in string:", 'z' not in string)

# 7. Bitwise Operators
print("\n=== Bitwise Operators ===")
a = 5       # 0101 in binary
b = 3       # 0011 in binary

print("a & b (AND):", a & b)     # 0001 = 1
print("a | b (OR):", a | b)      # 0111 = 7
print("a ^ b (XOR):", a ^ b)     # 0110 = 6
print("~a (NOT):", ~a)           # Inverts all bits
print("a << 1 (LEFT SHIFT):", a << 1)  # 1010 = 10
print("b >> 1 (RIGHT SHIFT):", b >> 1) # 0001 = 1
