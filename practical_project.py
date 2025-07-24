# practical_project.py
# A mini-project combining variables, data types, expressions, and type conversion
# Students can run this to simulate a simple store transaction

# Store item details
item_name = "Notebook"  # String
quantity = 3  # Integer
price_per_item = 4.99  # Float
in_stock = True  # Boolean

# Calculate total cost
subtotal = quantity * price_per_item
tax_rate = 0.08  # 8% tax
tax = subtotal * tax_rate
total = subtotal + tax

# Convert total to string for display
total_str = str(round(total, 2))  # Round to 2 decimal places

# Print receipt
print("=== Store Receipt ===")
print("Item:", item_name)
print("Quantity:", quantity)
print("Price per item: $", price_per_item)
print("Subtotal: $", subtotal)
print("Tax (8%): $", tax)
print("Total: $", total_str)
print("Item in stock?", in_stock)