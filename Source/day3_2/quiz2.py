class Purchase:
    def __init__(self, description="", price=0, quantity=0):
        self._description = description
        self._price = price
        self._quantity = quantity
        
    def setDescription(self, description):
        self._description = description
        
    def getDescription(self):
        return self._description
    
    def setPrice(self, price):
        self._price = price
        
    def getPrice(self):
        return self._price
    
    def setQuantity(self, quantity):
        self._quantity = quantity
        
    def getQuantity(self):
        return self._quantity


class Cart:
    def __init__(self, items=[]):
        self._items = items
        
    def addItemToCart(self, item):
        self._items.append(item)
        
    def getItems(self):
        return self._items
    
    def calculateTotal(self):
        amount = 0
        for item in self._items:
            amount += item.getPrice() * item.getQuantity()
        return amount

def printReceipt(myPurchases):
    print("\n{0:12} {1:<s} {2:<12}".format("ARTICLE","PRICE", "QUANTITY"))

    for purchase in myPurchases.getItems():
        print("{0:12s} ${1:,.2f} {2:5}".format(purchase.getDescription(),
        purchase.getPrice(), purchase.getQuantity()))

    print("\nTOTAL COST: ${0:,.2f}".format(myPurchases.calculateTotal()))

myPurchases = Cart()
carryOn = 'Y'

while carryOn.upper() == 'Y':
    description = input("Enter description of article: ")
    price = float(input("Enter price of article: "))
    quantity = int(input("Enter quantity of article: "))
    article = Purchase(description, price, quantity)
    myPurchases.addItemToCart(article)
    carryOn = input("Do you want to enter more articles (Y/N)? ")

printReceipt(myPurchases)

