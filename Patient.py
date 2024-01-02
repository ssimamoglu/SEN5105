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

    def set_date(self):
        return self.date
    
    def set_practitioner(self):
        return self.practitioner

    def set_charge(self):
        return self.charge

    def printProc(self):
            print("Procedure Name:", self.procname)
            print("Date: " , self.date)
            print("Charge: ", self.charge)


class Patient:
   
    def __init__(self, firstname, middlename, lastname, address, city, state, zipcode, phoneNumber, emergencyContactName, emergencyContactPhoneNumber, procedure):
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
        self.procedure = procedure
    
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

    def set_procedure(self, procedure):
        self.procedure = procedure

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

    def get_procedure(self):
        return self.procedure
    
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


def printPatient(patient, order):
    print("__Patient__", order+1, ":")
    patient.printPatient()
    print("__Emergency Contact__:")
    patient.printEmergencyContact()
    print("__Procedure__:")
    patient.procedure.printProc()

def main():

    ps = []
    prc1 = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 250)
    patient1 = Patient("Ali", "Mete", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332323", "Ayşe Yılmaz", "05322332324", prc1)
    ps.append(patient1)
    prc2 = Procedure("X-Ray", datetime.date.today(), "Dr. Irvine", 500)
    patient2 = Patient("Ayşe", "Fatma", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332324", "Ali Yılmaz", "05322332323", prc2)
    patient2.procedure= prc2
    ps.append(patient2)
    prc3 = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 200)
    patient3 = Patient("Ahmet", "Nuri", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332325", "Mehmet Yılmaz", "05322332326", prc3)
    ps.append(patient3)
    totalCharge = 0
    for p in ps:
        totalCharge += p.procedure.charge
        printPatient(p, ps.index(p))

    print("Total Charge:", totalCharge)

main()