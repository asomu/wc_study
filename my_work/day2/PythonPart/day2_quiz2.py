class Purchase:
    def __init__(self, des, price, quantity):
        self.description = des
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.purchase = []

    def add_purchase(self, purchase):
        self.purchase.append(purchase)

    def print_puchase(self):
        print("{:>10}{:>10}{:>10}".format("ARTICLE", "PRICE", "QUANTITY"))
        total_price = 0
        for item in self.purchase:
            print("{:>10}{:>10.2f}{:>10}".format(item.description, int(item.price), item.quantity))
            total_price += int(item.price)*int(item.quantity)
        print(f"TOTAL COST: ${total_price:7.2f}")

def ask_puchase():
    print("Enter description of article :")
    des = input()
    print("Enter price of article:")
    price = input()
    print("Enter quantity of article")
    quantity = input()
    return Purchase(des, price, quantity)

if __name__ == '__main__':
    my_cart = Cart()
    flag = True
    while flag:
        my_cart.add_purchase(ask_puchase())
        print("Do you want to enter more articles(Y / N)?")
        result = input()
        if result.upper() == 'N':
            flag = False

    my_cart.print_puchase()