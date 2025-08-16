# 📜 Lists and Dictionaries with Loops

# 👉 Lists
# A list is like a container that stores multiple items in order.
# Example: a shopping list, a playlist, or a todo list.

fruits = ["apple", "banana", "mango", "orange"]

# Looping through a list
print("Here are the fruits in the list:")
for fruit in fruits:
    print(fruit)

# 👉 Dictionaries
# A dictionary stores data in key-value pairs.
# Think of it like a real dictionary: a word (key) and its meaning (value).
# Example: a person's information

person = {
    "name": "Jerwin",
    "age": 20,
    "student": True
}

# Looping through a dictionary
print("\nHere are the details of the person:")
for key, value in person.items():
    print(key, ":", value)
