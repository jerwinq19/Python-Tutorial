# 🔀 Conditions in Python

# What are conditions?
# Conditions are like decision-making in real life.
# For example: "If it’s raining, bring an umbrella. Otherwise, wear sunglasses."
# In programming, we use conditions to tell the computer what to do
# depending on certain situations.

# The 'if' statement checks if something is true.
# If it is true → the code inside runs.
# If it is false → the code inside 'else' (or other conditions) runs.

# Example:
age = int(input("What is your age? "))  # Ask user for age, convert to number

if age >= 18:
    print("✅ You can access this page!")   # Runs if condition is true
else:
    print("❌ You cannot access this page!") # Runs if condition is false
    
# more example
if age < 13:
    print("You're a kid!")
elif age < 18:
    print("You're a teenager!")
else:
    print("You're an adult!")

