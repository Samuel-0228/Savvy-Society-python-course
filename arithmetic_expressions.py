# arithmetic_expressions.py
# Demonstrates arithmetic operators and order of operations
# Students can run this to practice math operations in Python

# Define variables for a grocery bill
apples = 4
price_per_apple = 0.75
oranges = 3
price_per_orange = 1.25

# Calculate total cost using arithmetic operators
total_cost = (apples * price_per_apple) + (oranges * price_per_orange)
discount = total_cost * 0.1  # 10% discount
final_cost = total_cost - discount

# Print the results
print("Grocery Bill Calculator")
print("Apples:", apples, "x $", price_per_apple, "=", apples * price_per_apple)
print("Oranges:", oranges, "x $", price_per_orange, "=", oranges * price_per_orange)
print("Total before discount: $", total_cost)
print("Discount (10%): $", discount)
print("Final cost: $", final_cost)

# Example of order of operations
area = (5 + 3) * 2 ** 2 / 4  # (5 + 3) * 4 / 4 = 8
print("\nRectangle area with adjustment:", area)