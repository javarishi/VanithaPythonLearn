class Customer:

    def __init__(self, name="David", address="Some Address"):
        print("This is Customer Constructor")
        self.name = name
        self.address = address
        self.cust_discount = 0

    # functions - self - instance on which this function is being called
    def discount(self, disc):
        self.cust_discount = disc
        print(self.name, "has  discount :: ", self.cust_discount, " %")

# customname = CLassName() --> Object of a class
custOne = Customer()
custTwo = Customer("Neil Armstrong", "NASA")

print("custOne " , custOne.name)
print("custOne " ,custOne.address)
custOne.discount(5)
print("custTwo " ,custTwo.name)
print("custTwo " ,custTwo.address)
custTwo.discount(2)