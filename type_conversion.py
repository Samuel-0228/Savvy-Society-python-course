# type_conversion.py
# Shows how to convert between data types using int(), float(), and str()
# Students can run this to see type conversion in action

# Converting string input to numbers
user_input = "6"  # Imagine this is user input
items = int(user_input)  # Convert to integer
cost_per_item = 2.5
total = items * cost_per_item

# Print the result
print("You bought", items, "items")
print("Total cost: $", total)

# Converting numbers to strings for messages
score = 85
message = "Your score is " + str(score) + " points!"
print(message)

# Converting float to integer
temperature = 36.6
temp_int = int(temperature)  # Drops decimal part
print("Temperature (rounded):", temp_int, "degrees")