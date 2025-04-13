# 1. If, Elif, Else Statements
temperature = 30
if temperature > 35:
    print("It's a hot day.")
elif temperature > 25:
    print("It's a warm day.")
else:
    print("It's a cool day.")
# 2. For Loops
# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Using range
for i in range(3):
    print(f"Iteration {i}")
# 3. While Loops
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
# 4. Break and Continue
# Break example
for number in range(5):
    if number == 3:
        break
    print(number)

# Continue example
for number in range(5):
    if number == 3:
        continue
    print(number)
# 📦 Lesson 6: Lists, Tuples & Dictionaries
# 1. Lists
# Creating and modifying a list
colors = ['red', 'green', 'blue']
colors.append('yellow')
print(colors)

# Accessing elements
print(colors[1])
# 2. Tuples
# Creating a tuple
dimensions = (1920, 1080)
print(f"Width: {dimensions[0]}, Height: {dimensions[1]}")
# 3. Dictionaries
# Creating and accessing a dictionary
person = {'name': 'Alice', 'age': 30}
print(person['name'])

# Adding a new key-value pair
person['city'] = 'New York'
print(person)
# 🧮 Lesson 7: Sets and Frozensets
# 1. Sets
# Creating a set and performing operations
numbers = {1, 2, 3, 4}
numbers.add(5)
print(numbers)

# Set operations
evens = {2, 4, 6}
print(numbers.union(evens))
print(numbers.intersection(evens))
# 2. Frozensets
# Creating a frozenset
immutable_set = frozenset([1, 2, 3])
print(immutable_set)

# Attempting to add to a frozenset will raise an error
# immutable_set.add(4)  # Uncommenting this line will cause an AttributeError