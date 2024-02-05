from sortedcontainers import SortedList
class InventoryItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.inventory_list = SortedList()

    def add_to_inventory(self, product_id, quantity):
        def add_product(self, product, quantity):
            inventory_item = InventoryItem(product, quantity)
            self.inventory_items.append(inventory_item)

        self.inventory_list.add([product_id, quantity])

    def remove_from_inventory(self, product_id, quantity):
        for item in self.inventory_list:
            if item[0] == product_id:
                if item[1] >= quantity:
                    item[1] -= quantity
                    if item[1] == 0:
                        self.inventory_list.remove(item)
                    return
                else:
                    print("Error: Insufficient quantity in stock.")
                    return
        print("Error: Product not found in inventory.")

    def update_stock_quantity(self, product_id, new_quantity):
        for item in self.inventory_list:
            if item[0] == product_id:
                item[1] = new_quantity
                return
        print("Error: Product not found in inventory.")

    def is_product_available(self, product_id, quantity_to_check):
        for item in self.inventory_list:
            if item[0] == product_id:
                return item[1] >= quantity_to_check
        return False

    def get_inventory_value(self):
        total_value = sum(item[1] * self.get_product_price(item[0]) for item in self.inventory_list)
        return total_value

    def list_low_stock_products(self, threshold):
        low_stock_products = [item for item in self.inventory_list if item[1] < threshold]
        return low_stock_products

    def list_out_of_stock_products(self):
        out_of_stock_products = [item for item in self.inventory_list if item[1] == 0]
        return out_of_stock_products

    def list_all_products(self):
        return self.inventory_list

    def get_product_price(self, product_id):
        # Dummy method to retrieve product price from database or elsewhere
        return 0  # Replace with actual implementation

def main():
    inventory = Inventory()
    # Adding products to inventory
    inventory.add_to_inventory(1, 10)
    inventory.add_to_inventory(2, 5)

    # Removing products from inventory
    inventory.remove_from_inventory(1, 3)

    # Updating stock quantity
    inventory.update_stock_quantity(2, 7)

    # Checking product availability
    print("Product 1 available:", inventory.is_product_available(1, 5))
    print("Product 2 available:", inventory.is_product_available(2, 10))

    # Getting inventory value
    print("Inventory value:", inventory.get_inventory_value())

    # Listing low stock products
    print("Low stock products:", inventory.list_low_stock_products(5))

    # Listing out of stock products
    print("Out of stock products:", inventory.list_out_of_stock_products())

    # Listing all products
    print("All products:", inventory.list_all_products())

if __name__ == "__main__":
    main()
