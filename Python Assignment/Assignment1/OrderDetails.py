from Customers import Customer
from Orders import Orders
from Products import Product


class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity, discount=0):
        self.order_detail_id = order_detail_id
        self._order = order
        self._product = product
        self.quantity = quantity
        self.discount = discount

    def calculate_subtotal(self):
        return self.quantity * self._product.price * (1 - self.discount)

    def get_order_detail_info(self):
        print("Order Detail ID:", self.order_detail_id)
        print("Product:", self._product.product_name)
        print("Quantity:", self.quantity)
        print("Discount:", self.discount)
        print("Subtotal:", self.calculate_subtotal())

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity updated to:", self.quantity)

    def add_discount(self, discount_amount):
        self.discount += discount_amount
        print("Discount added. New discount:", self.discount)


product1 = Product(1, "Laptop", "High-performance laptop", 999.99)

# Create a customer instance
customer1 = Customer(1, "John", "Doe", "john@example.com", "1234567890", "123 Main St")

# Create an order instance
order1 = Orders(1, customer1, 0)

# Create an order detail instance
order_detail1 = OrderDetails(1, order1, product1, 2)

# Display order detail information
order_detail1.get_order_detail_info()

# Update quantity
order_detail1.update_quantity(3)
order_detail1.get_order_detail_info()

# Add discount
order_detail1.add_discount(0.1)  # 10% discount
order_detail1.get_order_detail_info()
