# boolean_example.py
# Demonstrates boolean data type and comparison operators
# Students can run this to practice boolean expressions

# Define variables
age = 18
has_license = True
minimum_age = 16

# Boolean expressions using comparison operators
can_drive = age >= minimum_age and has_license
is_adult = age >= 18

# Print results
print("Age:", age)
print("Has license?", has_license)
print("Can they drive?", can_drive)
print("Are they an adult?", is_adult)

# Practical example: Check if a score meets a threshold
score = 75
passing_score = 60
passed = score >= passing_score
print("\nScore:", score)
print("Passed the test?", passed)