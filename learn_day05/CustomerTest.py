class Customer:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Customer created ", self.firstname, self.lastname)

    def discount(self):
        print("Normal Customer has NO Discount")

    def test_parent_method(self):
        print("Test Parent Method", self.firstname)

    def test_multiple(self):
        print("Customer Method for Multiple Inheritance")


class Validation:

    def __init__(self, address):
        self.address = address
        print("Validation CLass Init", self.address)


    def validation(self):
        print(self.address, "Validation")


    def test_multiple(self):
        print("Validation Method for Multiple Inheritance")


class PreferredCustomer(Customer, Validation):

    def __init__(self, fname, lname, email, address):
        Customer.__init__(self, fname, lname)
        Validation.__init__(self, address)
        self.email = email
        print("PreferredCustomer email", email)

    #Overriding - exact method from Parent class
    def discount(self):
        print("Preferred Customer has 5% Discount")

    def test_child_method(self):
        print("Test Child Method", self.firstname)


pCust = PreferredCustomer("Neil", "ArmStrong", "neil@nasa.com", "Some address")
pCust.discount()
pCust.test_parent_method()
pCust.test_child_method()
pCust.validation()
pCust.test_multiple()