import datetime
import string

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

def printPatient(patient):
    print("__Patient__:")
    print("Name:", patient.firstname , " " , patient.middlename.strip() , " " , patient.lastname)
    print("Address:", patient.address , " " , patient.city , " " , patient.zipcode)
    print("Phone Number:", patient.phoneNumber)
    print("__Emergency Contact__:")
    print("Name: ", patient.emergencyContactName , " Phone Number: " , patient.emergencyContactPhoneNumber)
    print("__Procedure__:")
    print("Procedure Name:", patient.procedure.procname , " Date: " , patient.procedure.date, " Charge: ", patient.procedure.charge)

def main():

    prc1 = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 250)
    patient1 = Patient("Ali", "Mete", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332323", "Ayşe Yılmaz", "05322332324", prc1)
    prc2 = Procedure("X-Ray", datetime.date.today(), "Dr. Irvine", 500)
    patient2 = Patient("Ayşe", "Fatma", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332324", "Ali Yılmaz", "05322332323", prc2)
    patient2.procedure= prc2
    prc3 = Procedure("Pysical Exam", datetime.date.today(), "Dr. Irvine", 200)
    patient3 = Patient("Ahmet", "Nuri", "Yılmaz", "Örnek Mah. Buket sok", "İstanbul", "", "34696", "05322332325", "Mehmet Yılmaz", "05322332326", prc3)
    printPatient(patient1)
    printPatient(patient2)
    printPatient(patient3)

    print("Total Charge:", patient1.procedure.charge + patient2.procedure.charge + patient3.procedure.charge)

main()