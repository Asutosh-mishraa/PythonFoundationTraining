class Orders:
    def __init__(self, order_id, customer, order_date, total_amount, status, order_details):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status
        self.order_details = order_details

    def CalculateTotalAmount(self):
        total_amount = sum(detail.product.price * detail.quantity for detail in self.order_details)
        self.total_amount = total_amount
        return total_amount

    def GetOrderDetails(self):
        details = f"Order ID: {self.order_id}\nCustomer: {self.customer}\nOrder Date: {self.order_date}\nStatus: {self.status}\n\nOrder Details:\n"
        for detail in self.order_details:
            details += f"- Product: {detail.product.product_name}, Quantity: {detail.quantity}\n"
        return details

    def UpdateOrderStatus(self, new_status):
        self.status = new_status

    def CancelOrder(self, inventory_manager):
        for detail in self.order_details:
            inventory_manager.add_to_inventory(detail.product, detail.quantity)
        self.status = "Canceled"
        print("Order canceled successfully.")


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print("Order added successfully.")

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.UpdateOrderStatus(new_status)
                print(f"Order {order_id} status updated to {new_status}.")
                return
        print(f"Order with ID {order_id} not found.")

    def cancel_order(self, order_id, inventory_manager):
        for order in self.orders:
            if order.order_id == order_id:
                order.CancelOrder(inventory_manager)
                self.orders.remove(order)
                print(f"Order {order_id} canceled.")
                return
        print(f"Order with ID {order_id} not found.")


def main():
    # Create an instance of OrderManager
    order_manager = OrderManager()

    # Create some dummy orders
    order1 = Orders(1, "John Doe", "2024-01-30", 0, "Pending", [])
    order2 = Orders(2, "Jane Doe", "2024-01-31", 0, "Pending", [])

    # Add orders to the OrderManager
    order_manager.add_order(order1)
    order_manager.add_order(order2)

    # Update the status of an order
    order_manager.update_order_status(1, "Shipped")

    # Cancel an order
    # Dummy InventoryManager passed for demonstration purposes
    inventory_manager = InventoryManager()
    order_manager.cancel_order(2, inventory_manager)


class InventoryManager:
    def add_to_inventory(self, product, quantity):
        pass


if __name__ == "__main__":
    main()
