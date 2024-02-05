class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self._email = email
        self.phone = phone
        self.address = address
        self.orders = []  # We will store orders placed by this customer

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Invalid email address format.")
        self._email = value

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.first_name, self.last_name)
        print("Email:", self._email)
        print("Phone:", self.phone)
        print("Address:", self.address)
        print("Total Orders:", self.calculate_total_orders())

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        print("Customer information updated successfully.")


customer1 = Customer(1, "Asutosh", "Mishra", "asu@example.com", "1234567890", "123 Main St")
customer1.get_customer_details()
customer1.update_customer_info(email="asutosh@example.com")
customer1.get_customer_details()
