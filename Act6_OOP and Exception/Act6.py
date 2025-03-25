class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.item_id:<10} | {self.name:<20} | {self.description:<30} | {self.price:.2f}"


class SariSariStore:
    def __init__(self):
        self.items = {}

    def add_item(self):
        try:
            item_id = input("Enter item ID: ")
            if not item_id.isdigit():
                raise ValueError("Item ID must be a number.")
            item_id = int(item_id)
            if item_id in self.items:
                raise ValueError("Item ID already exists.")

            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            print("=" * 75)
            print("\t\t\t\tItems List")
            print("-" * 75)
            print(f"{'ID':<10} | {'Name':<20} | {'Description':<30} | {'Price':<10}")
            print("=" * 75)
            for item in self.items.values():
                print(item)
            print("=" * 75)

    def update_item(self):
        try:
            item_id = input("Enter item ID to update: ")
            if not item_id.isdigit():
                raise ValueError("Item ID must be a number.")
            item_id = int(item_id)
            if item_id not in self.items:
                raise ValueError("Item ID not found.")

            name = input("Enter new name: ")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self):
        try:
            item_id = input("Enter item ID to delete: ")
            if not item_id.isdigit():
                raise ValueError("Item ID must be a number.")
            item_id = int(item_id)
            if item_id not in self.items:
                raise ValueError("Item ID not found.")
            
            del self.items[item_id]
            print("Item deleted successfully!")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    store = SariSariStore()
    while True:
        print("=" * 75)
        print("\t\t\tSari-Sari Store Item Management\n")
        print("\t\t\t\t1. Add Item")
        print("\t\t\t\t2. View Items")
        print("\t\t\t\t3. Update Item")
        print("\t\t\t\t4. Delete Item")
        print("\t\t\t\t5. Exit\n")
        print("=" * 75)
        
        choice = input("Enter your choice: ")
        if choice == "1":
            store.add_item()
        elif choice == "2":
            store.view_items()
        elif choice == "3":
            store.update_item()
        elif choice == "4":
            store.delete_item()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()