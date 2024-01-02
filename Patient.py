class Patient:
   
    def __init__(self, firstname, middlename, lastname, address, city, state, zipcode, phoneNumber, emergencyContactName, emergencyContactPhoneNumber):
        self.firstname = firstname,
        self.middlename = middlename,
        self.lastname = lastname,
        self.address = address,
        self.city = city,
        self.state = state,
        self.zipcode = zipcode,
        self.phoneNumber = phoneNumber,
        self.emergencyContactName = emergencyContactName,
        self.emergencyContactPhoneNumber = emergencyContactPhoneNumber
    
    def set_firstname(self, value):
        self.firstname = value
    
    def set_middlename(self, value):
        self.middlename = value

    def set_lastname(self, value):
        self.lastname = value
    
    def set_address(self, value):
        self.address = value

    def set_city(self, value):
        self.city = value

    def set_state(self, value):
        self.state = value
    
    def set_zipcode(self, value):
        self.zipcode = value

    def set_phoneNumber(self, value):
        self.phoneNumber = value

    def set_emergencyContactName(self, value):
        self.emergencyContactName = value
    def set_emergencyContactPhoneNumber(self, value):
        self.emergencyContactPhoneNumber = value
        
