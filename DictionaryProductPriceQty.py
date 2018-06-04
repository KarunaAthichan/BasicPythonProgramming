import pprint

# empty dictionary
prodpriceqty={}

# Get total number of products from user
products = int(input("Enter the total items want to be inserted into dictionary: "))

# Initialise the variables
prod = " "
prc= 0
qty = 0
totalprice = 0

# Iterate the product list
for i in range(products):

    # Get the product, price and quantity list from user
    prod = input("Enter the product to add: ")
    prc = int(input("Enter the price of product: "))
    qty = int(input("Enter the quantity of product: "))

    # Update the empty dictionary with the user entered information
    prodpriceqty.update({prod: {'price': prc, 'quantity': qty}})

    # Finding the total price
    totalprice = totalprice + (prc * qty)
    print("*"*27)

# proper print the dictionary and display total price
pprint.pprint(prodpriceqty)
print("Total Price of products: ",totalprice)