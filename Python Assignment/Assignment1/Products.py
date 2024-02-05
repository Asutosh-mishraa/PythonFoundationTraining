class Product:
    def __init__(self, product_id, product_name, description, price, in_stock=True):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.in_stock = in_stock

    def get_product_details(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Description:", self.description)
        print("Price:", self.price)
        print("In Stock:", "Yes" if self.in_stock else "No")

    def update_product_info(self, price=None, description=None, in_stock=None):
        if price:
            self.price = price
        if description:
            self.description = description
        if in_stock is not None:
            self.in_stock = in_stock
        print("Product information updated successfully.")

    def is_product_in_stock(self):
        return self.in_stock


class ProductManager:
    def __init__(self):
        self.products = {}  # Dictionary to store products by their IDs

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product ID already exists. Please use a different ID.")
        self.products[product.product_id] = product
        print(f"Product {product.product_id} added successfully.")

    def update_product(self, product_id, **kwargs):
        if product_id not in self.products:
            raise ValueError("Product ID does not exist.")

        product = self.products[product_id]
        product.update_product_info(**kwargs)
        print(f"Product {product_id} updated successfully.")

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product ID does not exist.")

        del self.products[product_id]
        print(f"Product {product_id} removed successfully.")


product_manager = ProductManager()

# Creating Product objects
laptop = Product(1, "Laptop", "High-performance laptop", 999.99, True)
smartphone = Product(2, "Smartphone", "Latest smartphone model", 799.99, True)
# Adding products to the ProductManager
try:
    product_manager.add_product(laptop)
    product_manager.add_product(smartphone)
except ValueError as e:
    print(f"Error adding product: {e}")
# Updating a product
try:
    product_manager.update_product(1, price=1099.99, description="Updated laptop description", in_stock=False)
except ValueError as e:
    print(f"Error updating product: {e}")
# Removing a product
try:
    product_manager.remove_product(2)
except ValueError as e:
    print(f"Error removing product: {e}")
laptop.get_product_details()
print("Is the product in stock?", laptop.is_product_in_stock())