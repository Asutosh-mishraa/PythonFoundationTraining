from DBconnector import *


def registerCustomer(dbConnector):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    customer = Customer(None, first_name, last_name, email, phone, address)
    Customer.create(customer, dbConnector)


def updateAccountDetails(dbConnector):
    c_id = input("Enter your customer id: ")
    ch = int(input("what do you want to update: 1.Email\n2.phone number"))
    if ch == 1:
        email = input("enter the new email: ")
        Customer.update(dbConnector, c_id, email)
    elif ch == 2:
        phone = input("Enter phone number: ")
        Customer.update(dbConnector, c_id, phone)


def updateProductInfo(dbConnector):
    p_id = input("Enter the product id: ")
    prod_read = Product.read(p_id, dbConnector)
    if prod_read:
        ch = int(input("Enter what to update: 1.Price\n2.Description"))
        if ch == 1:
            price = input("Enter the price: ")
            prod_read.price = price
            prod_read.update(dbConnector)
        elif ch == 2:
            desc = input("Enter the new description: ")
            prod_read.description = desc
            prod_read.update(dbConnector)

    else:
        print("No such Product Found.")


def product_search(db_connector):
    p_name = input("Enter the product name: ")
    try:
        db_connector.open_connection()
        cursor = db_connector.connection.cursor()
        cursor.execute("SELECT * FROM Products WHERE product_name = %s", (p_name,))
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


def track_order_status(db_connector):
    o_id = input("Enter your order id: ")
    db_connector.open_connection()
    cursor = db_connector.connection.cursor()
    cursor.execute("SELECT OrderID,CASE WHEN DATEDIFF(CURDATE(), OrderDate) = 0 THEN 'Pending' WHEN DATEDIFF(CURDATE("
                   "), OrderDate) >= 3 THEN 'Processing' WHEN DATEDIFF(CURDATE(), OrderDate) >= 7 THEN 'Delivered' "
                   "ELSE 'Completed' END AS Status FROM Orders where orderid = %s", (o_id,))
    res = cursor.fetchall()
    for i in res:
        print(i)


def inventory_management(dbConnector):
    ch = input("Enter what you want to do: 1.Add new Product\n2.Update quantities\n3.Delete a product")
    if ch == 1:
        prod_id = input("Enter the product id: ")
        quantity = input("Enter the quantity: ")
        last_stock_update = input("Enter the date of last stock update: ")
        new_inventory = Inventory("I101", prod_id, quantity, last_stock_update)
        Inventory.create(new_inventory, db_connector)
    elif ch == 2:
        p_id = input("Enter the product id: ")
        quantity = input("Enter the new quantity:")
        db_connector.open_connection()
        cursor = db_connector.connection.cursor()
        cursor.execute("SELECT * FROM Inventory WHERE product_id = %s", (p_id,))
        inventory_data = cursor.fetchone()
        if inventory_data:
            inventory_data.quantity_in_stock = 200
            inventory_data.update(db_connector)
    elif ch == 3:
        i_id = input("Enter the inventory id: ")
        try:
            db_connector.open_connection()
            cursor = db_connector.connection.cursor()
            cursor.execute("DELETE FROM Inventory WHERE InventoryID = %s", (i_id,))
            db_connector.connection.commit()
            print("Inventory deleted successfully.")
        except Error as e:
            print("Error deleting inventory:", e)
        finally:
            db_connector.close_connection()


host = 'localhost'
database = 'techshopdb'
user = 'root'
password = 'root'
port = '3306'

# Create a DatabaseConnector instance
db_connector = DatabaseConnector(host, database, user, password, port)
registerCustomer(db_connector)
updateAccountDetails(db_connector)
updateProductInfo(db_connector)
product_search(db_connector)
track_order_status(db_connector)
inventory_management(db_connector)
