# 🔁 Loops in Python

# What are loops?
# Loops are a way to repeat actions without writing the same code many times.
# Instead of telling the computer "do this, do this, do this" over and over,
# you tell it once, and the loop takes care of the repetition.

# Real-life example:
# If you have 5 bottles to wash, you don't say "wash bottle 1,
# wash bottle 2..." manually. You just say "keep washing bottles until all are clean."
# That’s exactly what a loop does!

# Example 1: Using a for loop
for i in range(5):  # repeat 5 times
    print("Hello World!")

# Example 2: Printing numbers 1 to 5
for number in range(1, 6):
    print("Number:", number)

# Example 3: While loop
# A while loop repeats as long as a condition is true
count = 0
while count < 3:
    print("This is loop number:", count)
    count = count + 1  # important: update the counter, or it loops forever!
