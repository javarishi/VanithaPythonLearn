from learn_day05.CustomerTest import PreferredCustomer, Customer


class CreditCardCustomer(PreferredCustomer):

    def __init__(self, fname, lname, email, address):
        self.address = address
        PreferredCustomer.__init__(self, fname, lname, email)
        print("Credit Card sent to ", address)

    def discount(self):
        print("Credit Card Customers have 7% Discount")

    def validate_address(self):
        print(self.address, " Google Maps validation")


ccCust = CreditCardCustomer("Buzz", "Aldrine", "buzz@nasa.com", "8106 Hillsborrow Ave, Tampa, FL")
ccCust.discount()
ccCust.validate_address()

print("Check PreferredCustomer Instance", isinstance(ccCust, PreferredCustomer))
print("Check Customer Instance", isinstance(ccCust, Customer))
print("Check Object Instance", isinstance(ccCust, object))
print("Is CreditCardCustomer is Subclass of Customer" , issubclass(CreditCardCustomer, Customer))
print("Is CreditCardCustomer is Subclass of Object" , issubclass(CreditCardCustomer, object))