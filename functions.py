# ⚙️ Functions in Python

# What are functions?
# A function is like a recipe or a set of instructions.
# You give it a name, write the steps once, and you can "call" it
# whenever you need it — instead of rewriting the same code.

# Basic function example:
def greet(name):
    print("Hello " + name + "!")

# Calling the function
greet("Jerwin")
greet("Ana")

# 👉 Functions with Lists
# Let's say you have a list of fruits and you want to print them neatly.
def show_fruits(fruit_list):
    for fruit in fruit_list:
        print("🍎 Fruit:", fruit)

fruits = ["apple", "banana", "mango"]
show_fruits(fruits)   # Call the function with the list

# 👉 Functions with Dictionaries
# Let's create a function to show info about a person
def show_person_info(person_dict):
    for key, value in person_dict.items():
        print(key.capitalize(), ":", value)

person = {
    "name": "Jerwin",
    "age": 20,
    "student": True
}

show_person_info(person)  # Call the function with the dictionary
