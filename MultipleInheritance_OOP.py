# Base class
class OperatingSystem:
    multitasking = True
    name = "Mac OS"

# Base class
class Apple:
    website ="www.apple.com"
    name = "Apple"

# Derived class from Operating system and Apple
class MacBook(OperatingSystem,Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.website))
            # when both base class have same name, it picks the order given in derived class
            print("Name :",self.name)

macbook = MacBook()
