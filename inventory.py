class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# List to store shoe objects
shoes_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    shoe = Shoe(data[0], data[1], data[2], data[3], data[4])
                    shoes_list.append(shoe)
    except FileNotFoundError:
        print("Error: The file 'inventory.txt' was not found.")
    except Exception as e:
        print(f"Error: {e}")

def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe added successfully!")

def view_all():
    for shoe in shoes_list:
        print(shoe)

def re_stock():
    if not shoes_list:
        print("No shoes available in the inventory.")
        return

    lowest_stock_shoe = min(shoes_list, key=lambda x: x.get_quantity())
    print(f"Shoe with lowest stock: {lowest_stock_shoe}")
    add_quantity = int(input("Enter the quantity to add: "))
    lowest_stock_shoe.quantity += add_quantity
    print("Stock updated successfully!")

def search_shoe():
    code = input("Enter the shoe code to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")

def value_per_item():
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Shoe: {shoe.product}, Total Value: {value}")

def highest_qty():
    if not shoes_list:
        print("No shoes available in the inventory.")
        return

    highest_stock_shoe = max(shoes_list, key=lambda x: x.get_quantity())
    print(f"Shoe with highest quantity for sale: {highest_stock_shoe}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Restock Shoes")
        print("5. Search Shoe")
        print("6. Calculate Value per Item")
        print("7. Find Highest Quantity Shoe")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu function
if __name__ == "__main__":
    menu()
