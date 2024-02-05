import mysql.connector
from mysql.connector import Error


class DatabaseConnector:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.port = port

    def open_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print("Error connecting to MySQL database:", e)

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection to MySQL database closed")


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    @staticmethod
    def create(customer, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (customer.customer_id, customer.first_name, customer.last_name,
                            customer.email, customer.phone, customer.address))
            db_connector.connection.commit()
            print("Customer created successfully.")
        except Error as e:
            print("Error creating customer:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def read(customer_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
            customer_data = cursor.fetchone()

            if customer_data:
                return Customer(*customer_data)
            else:
                print("Customer not found.")
                return None
        except Error as e:
            print("Error reading customer:", e)
        finally:
            db_connector.close_connection()

    def update(self, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("UPDATE Customers SET FirstName = %s, LastName = %s, "
                           "Email = %s, Phone = %s, Address = %s WHERE CustomerID = %s",
                           (self.first_name, self.last_name, self.email, self.phone,
                            self.address, self.customer_id))
            db_connector.connection.commit()
            print("Customer updated successfully.")
        except Error as e:
            print("Error updating customer:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def delete(customer_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM Customers WHERE CustomerID = %s", (customer_id,))
            db_connector.connection.commit()
            print("Customer deleted successfully.")
        except Error as e:
            print("Error deleting customer:", e)
        finally:
            db_connector.close_connection()


class Product:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    @staticmethod
    def create(product, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("INSERT INTO Products (ProductID, ProductName, Description, Price) "
                           "VALUES (%s, %s, %s, %s)",
                           (product.product_id, product.product_name, product.description, product.price))
            db_connector.connection.commit()
            print("Product created successfully.")
        except Error as e:
            print("Error creating product:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def read(product_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
            product_data = cursor.fetchone()

            if product_data:
                return Product(*product_data)
            else:
                print("Product not found.")
                return None
        except Error as e:
            print("Error reading product:", e)
        finally:
            db_connector.close_connection()

    def update(self, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("UPDATE Products SET ProductName = %s, Description = %s, "
                           "Price = %s WHERE ProductID = %s",
                           (self.product_name, self.description, self.price, self.product_id))
            db_connector.connection.commit()
            print("Product updated successfully.")
        except Error as e:
            print("Error updating product:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def delete(product_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM Products WHERE ProductID = %s", (product_id,))
            db_connector.connection.commit()
            print("Product deleted successfully.")
        except Error as e:
            print("Error deleting product:", e)
        finally:
            db_connector.close_connection()


class Order:
    def __init__(self, order_id, customer_id, order_date, total_amount):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount

    @staticmethod
    def create(order, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) "
                           "VALUES (%s, %s, %s, %s)",
                           (order.order_id, order.customer_id, order.order_date, order.total_amount))
            db_connector.connection.commit()
            print("Order created successfully.")
        except Error as e:
            print("Error creating order:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def read(order_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("SELECT * FROM Orders WHERE OrderID = %s", (order_id,))
            order_data = cursor.fetchone()

            if order_data:
                return Order(*order_data)
            else:
                print("Order not found.")
                return None
        except Error as e:
            print("Error reading order:", e)
        finally:
            db_connector.close_connection()

    def update(self, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("UPDATE Orders SET CustomerID = %s, OrderDate = %s, "
                           "TotalAmount = %s WHERE OrderID = %s",
                           (self.customer_id, self.order_date, self.total_amount, self.order_id))
            db_connector.connection.commit()
            print("Order updated successfully.")
        except Error as e:
            print("Error updating order:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def delete(order_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))
            db_connector.connection.commit()
            print("Order deleted successfully.")
        except Error as e:
            print("Error deleting order:", e)
        finally:
            db_connector.close_connection()


class Inventory:
    def __init__(self, inventory_id, product_id, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product_id = product_id
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    @staticmethod
    def create(inventory, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("INSERT INTO Inventory (InventoryID, ProductID, QuantityInStock, LastStockUpdate) "
                           "VALUES (%s, %s, %s, %s)",
                           (inventory.inventory_id, inventory.product_id, inventory.quantity_in_stock,
                            inventory.last_stock_update))
            db_connector.connection.commit()
            print("Inventory created successfully.")
        except Error as e:
            print("Error creating inventory:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def read(inventory_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("SELECT * FROM Inventory WHERE InventoryID = %s", (inventory_id,))
            inventory_data = cursor.fetchone()

            if inventory_data:
                return Inventory(*inventory_data)
            else:
                print("Inventory not found.")
                return None
        except Error as e:
            print("Error reading inventory:", e)
        finally:
            db_connector.close_connection()

    def update(self, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("UPDATE Inventory SET ProductID = %s, QuantityInStock = %s, "
                           "LastStockUpdate = %s WHERE InventoryID = %s",
                           (self.product_id, self.quantity_in_stock, self.last_stock_update, self.inventory_id))
            db_connector.connection.commit()
            print("Inventory updated successfully.")
        except Error as e:
            print("Error updating inventory:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def delete(inventory_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM Inventory WHERE InventoryID = %s", (inventory_id,))
            db_connector.connection.commit()
            print("Inventory deleted successfully.")
        except Error as e:
            print("Error deleting inventory:", e)
        finally:
            db_connector.close_connection()


class OrderDetail:
    def __init__(self, order_detail_id, order_id, product_id, quantity):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    @staticmethod
    def create(order_detail, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) "
                           "VALUES (%s, %s, %s, %s)",
                           (order_detail.order_detail_id, order_detail.order_id, order_detail.product_id,
                            order_detail.quantity))
            db_connector.connection.commit()
            print("Order detail created successfully.")
        except Error as e:
            print("Error creating order detail:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def read(order_detail_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("SELECT * FROM OrderDetails WHERE OrderDetailID = %s", (order_detail_id,))
            order_detail_data = cursor.fetchone()

            if order_detail_data:
                return OrderDetail(*order_detail_data)
            else:
                print("Order detail not found.")
                return None
        except Error as e:
            print("Error reading order detail:", e)
        finally:
            db_connector.close_connection()

    def update(self, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("UPDATE OrderDetails SET OrderID = %s, ProductID = %s, "
                           "Quantity = %s WHERE OrderDetailID = %s",
                           (self.order_id, self.product_id, self.quantity, self.order_detail_id))
            db_connector.connection.commit()
            print("Order detail updated successfully.")
        except Error as e:
            print("Error updating order detail:", e)
        finally:
            db_connector.close_connection()

    @staticmethod
    def delete(order_detail_id, db_connector):
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM OrderDetails WHERE OrderDetailID = %s", (order_detail_id,))
            db_connector.connection.commit()
            print("Order detail deleted successfully.")
        except Error as e:
            print("Error deleting order detail:", e)
        finally:
            db_connector.close_connection()


def main():
    # Database connection details
    host = 'localhost'
    database = 'techshopdb'
    user = 'root'
    password = 'root'
    port = '3306'

    # Create a DatabaseConnector instance
    db_connector = DatabaseConnector(host, database, user, password, port)

    # Create a new customer
    new_customer = Customer("101", "John", "Doe", "john@example.com", "1234567890", "123 Main St")

    # Create the customer
    Customer.create(new_customer, db_connector)

    # Read the customer
    customer_id_to_read = "101"
    customer_read = Customer.read(customer_id_to_read, db_connector)
    if customer_read:
        print("Customer read:", customer_read.__dict__)

    # Update the customer
    if customer_read:
        customer_read.phone = "9876543210"
        customer_read.update(db_connector)

    # Delete the customer
    customer_id_to_delete = "101"
    Customer.delete(customer_id_to_delete, db_connector)

    # Create a new product
    new_product = Product("P101", "Laptop", "High-performance laptop", 999.99)

    # Create the product
    Product.create(new_product, db_connector)

    # Read the product
    product_id_to_read = "P101"
    product_read = Product.read(product_id_to_read, db_connector)
    if product_read:
        print("Product read:", product_read.__dict__)

    # Update the product
    if product_read:
        product_read.price = 1099.99
        product_read.update(db_connector)

    # Delete the product
    product_id_to_delete = "P101"
    Product.delete(product_id_to_delete, db_connector)

    # Create a new order
    new_order = Order("O101", "C101", "2023-01-15", 499.99)

    # Create the order
    Order.create(new_order, db_connector)

    # Read the order
    order_id_to_read = "O101"
    order_read = Order.read(order_id_to_read, db_connector)
    if order_read:
        print("Order read:", order_read.__dict__)

    # Update the order
    if order_read:
        order_read.total_amount = 599.99
        order_read.update(db_connector)

    # Delete the order
    order_id_to_delete = "O101"
    Order.delete(order_id_to_delete, db_connector)

    # Create a new inventory
    new_inventory = Inventory("I101", "P101", 100, "2023-01-15")

    # Create the inventory
    Inventory.create(new_inventory, db_connector)

    # Read the inventory
    inventory_id_to_read = "I101"
    inventory_read = Inventory.read(inventory_id_to_read, db_connector)
    if inventory_read:
        print("Inventory read:", inventory_read.__dict__)

    # Update the inventory
    if inventory_read:
        inventory_read.quantity_in_stock = 200
        inventory_read.update(db_connector)

    # Delete the inventory
    inventory_id_to_delete = "I101"
    Inventory.delete(inventory_id_to_delete, db_connector)

    # Create a new order detail
    new_order_detail = OrderDetail("OD101", "O101", "P101", 5)

    # Create the order detail
    OrderDetail.create(new_order_detail, db_connector)

    # Read the order detail
    order_detail_id_to_read = "OD101"
    order_detail_read = OrderDetail.read(order_detail_id_to_read, db_connector)
    if order_detail_read:
        print("Order detail read:", order_detail_read.__dict__)

    # Update the order detail
    if order_detail_read:
        order_detail_read.quantity = 10
        order_detail_read.update(db_connector)

    # Delete the order detail
    order_detail_id_to_delete = "OD101"
    OrderDetail.delete(order_detail_id_to_delete, db_connector)


if __name__ == "__main__":
    main()
