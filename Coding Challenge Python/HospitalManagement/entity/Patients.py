class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    def get_patientId(self):
        return self.__patientId

    def set_patientId(self, patientId):
        self.__patientId = patientId

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contactNumber(self):
        return self.__contactNumber

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Patient ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, Date of Birth: {self.__dateOfBirth}, Gender: {self.__gender}, Contact Number: {self.__contactNumber}, Address: {self.__address}"

    def print_details(self):
        print("Patient ID:", self.__patientId)
        print("First Name:", self.__firstName)
        print("Last Name:", self.__lastName)
        print("Date of Birth:", self.__dateOfBirth)
        print("Gender:", self.__gender)
        print("Contact Number:", self.__contactNumber)
        print("Address:", self.__address)