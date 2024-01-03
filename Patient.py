import datetime

class Procedure:

    def __init__(self, procname, date, practitioner, charge):
        self.procname = procname
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    def set_procname(self, procname):
        self.procname = procname

    def set_date(self, date):
        self.date = date
    
    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def set_charge(self, charge):
        self.charge = charge

    def get_procname(self):
        return self.procname

    def get_date(self):
        return self.date
    
    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge

    def printProc(self):
            print("Procedure Name:", self.procname)
            print("Date: " , self.date)
            print("Charge: ", self.charge)


class Patient:
   
    def __init__(self, firstname, middlename, lastname, address, city, state, zipcode, phoneNumber, emergencyContactName, emergencyContactPhoneNumber, procedures):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phoneNumber = phoneNumber
        self.emergencyContactName = emergencyContactName
        self.emergencyContactPhoneNumber = emergencyContactPhoneNumber
        self.procedures = procedures
    
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

    def set_procedure(self, procedures):
        self.procedures = procedures

    def get_firstname(self):
        return self.firstname
    
    def get_middlename(self):
        return self.middlename

    def get_lastname(self):
        return self.lastname
    
    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state
    
    def get_zipcode(self):
        return self.zipcode

    def get_phoneNumber(self):
        return self.phoneNumber

    def get_emergencyContactName(self):
        return self.emergencyContactName

    def get_emergencyContactPhoneNumber(self):
        return self.emergencyContactPhoneNumber

    def get_procedures(self):
        return self.procedures
    
    def printPatient(self):
        print("Name :", self.firstname)
        print("Middle Name :", self.middlename)
        print("LastName :", self.lastname)
        print("Address: " , self.address)
        print("City: ", self.city)
        print("State: ", self.state)
        print("Zipcode: ", self.zipcode)
        print("Phone Number: ", self.phoneNumber)

    def printEmergencyContact(self):
        print("Name: ", self.emergencyContactName)
        print("Phone Number: ", self.emergencyContactPhoneNumber)


def printPatient(patient):
    print("__Patient__:")
    patient.printPatient()
    print("__Emergency Contact__:")
    patient.printEmergencyContact()
    print("__Procedures__:")
    totalCharge = 0
    for pc in patient.procedures:
        print("Procedure #", patient.procedures.index(pc)+1)
        totalCharge += pc.charge
        pc.printProc()
    print("Total Charge:", totalCharge)
    

def main():
    prcs = []
    prc = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 250)
    prcs.append(prc)
    prc = Procedure("X-Ray", datetime.date.today(), "Dr. Irvine", 500)
    prcs.append(prc)
    prc = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 200)
    prcs.append(prc)

    patient = Patient("Ali", "Mete", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332323", "Ayşe Yılmaz", "05322332324", prcs)
    printPatient(patient)

main()