# List of items on the menu
menu = ["coffee", "tea", "sandwich", "cake"]

# Dictionary for stock values of each item
stock = {
    "coffee": 20,
    "tea": 15,
    "sandwich": 10,
    "cake": 5
}

# Dictionary for price of each item
price = {
    "coffee": 2.5,
    "tea": 1.8,
    "sandwich": 4.0,
    "cake": 3.5
}

# Calculate the total stock value
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# Print the total stock value
print(f"The total stock value of the cafe is: ${total_stock:.2f}")
