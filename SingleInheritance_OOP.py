# Base class, it shouldn't have init function
class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to",self.contactWebsite)

# Derived class, should have init function
class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This MacBook was manufactured in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))

# Object should create only for derived class
macbook = MacBook()
macbook.manufactureDetails()
macbook.contactDetails()


