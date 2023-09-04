import datetime


class Naftizinum:

    def __init__(self, in_stock, price):
        self.in_stock = in_stock
        self.price = price

    def get_in_stock(self):
        return self.in_stock

    def set_in_stock(self, amount):
        self.in_stock = self.in_stock - amount


class Cocainum:
    def __init__(self, in_stock, price):
        self.in_stock = in_stock
        self.price = price

    def get_in_stock(self):
        return self.in_stock

    def set_in_stock(self, amount):
        self.in_stock = self.in_stock - amount


class Askorbinum:
    def __init__(self, in_stock, price):
        self.in_stock = in_stock
        self.price = price

    def get_in_stock(self):
        return self.in_stock

    def set_in_stock(self, amount):
        self.in_stock = self.in_stock - amount


class Customer:
    def __init__(self, wallet):
        self.wallet = wallet


naftizinum = Naftizinum(20, 5)
cocainum = Cocainum(50, 7)
askorbinum = Askorbinum(80, 8)
customer = Customer(500)


class Shop:
    def __init__(self, item_profit1, item_profit2, item_profit3):
        self.item_profit1 = item_profit1
        self.item_profit2 = item_profit2
        self.item_profit3 = item_profit3
        self.naftizinum = naftizinum
        self.cocainum = cocainum
        self.askorbinum = askorbinum
        self.customer = customer

    def sell_smth(self):
        tobuy = int(input("Choose an item to buy from 1 to 3: "))
        if tobuy != 1 and tobuy != 2 and tobuy != 3:
            print("Invalid input, try again")
            self.sell_smth()
        elif tobuy == 1:
            amount = int(input("How many items do you need? "))
            if amount >= 1 and amount <= self.naftizinum.in_stock:
                payment = amount * self.naftizinum.price
                if payment > self.customer.wallet:
                    print("You have not enough money. Try to order a little bit less")
                    self.sell_smth()
                else:
                    print("Prykhod ische")
                    self.customer.wallet -= payment
                    self.item_profit1 += payment
                    self.naftizinum.set_in_stock(amount)
            elif amount > self.naftizinum.in_stock:
                print(f'Sorry, we can not sell you {amount} pcs. Its only {naftizinum.in_stock} pcs avaliable')
                self.sell_smth()
            else:
                print("Stop joking, Wasia")
                self.sell_smth()
        elif tobuy == 2:
            amount = int(input("How many items do you need? "))
            if amount >= 1 and amount <= self.cocainum.in_stock:
                payment = amount * shop.cocainum.price
                if payment > self.customer.wallet:
                    print("You have not enough money. Try to order a little bit less")
                    self.sell_smth()
                else:
                    print("Prykhod ische")
                    self.customer.wallet -= payment
                    self.item_profit2 += payment
                    self.cocainum.set_in_stock(amount)
            elif amount > self.cocainum.in_stock:
                print(f'Sorry, we can not sell you {amount} pcs. Its only {cocainum.in_stock} pcs avaliable')
                self.sell_smth()
            else:
                print("Stop joking, Wasia")
                self.sell_smth()
        else:
            amount = int(input("How many items do you need? "))
            if amount >= 1 and amount <= self.askorbinum.in_stock:
                payment = amount * shop.askorbinum.price
                if payment > self.customer.wallet:
                    print("You have not enough money. Try to order a little bit less")
                    self.sell_smth()
                else:
                    print("Prykhod ische")
                    self.customer.wallet -= payment
                    self.item_profit3 += payment
                    self.askorbinum.set_in_stock(amount)
            elif amount > self.askorbinum.in_stock:
                print(
                    f'Sorry, we can not sell you {amount} pcs. Its only {askorbinum.in_stock} pcs avaliable')
                self.sell_smth()
            else:
                print("Stop joking, Wasia")
                self.sell_smth()
        # Here I have already tired to add validation
        vin_ische_ne_pishov = int(input("Are you wish something else? (1 - Yes; any other input - No) "))
        if vin_ische_ne_pishov == 1:
            self.sell_smth()
        else:
            print("Good bye")


shop = Shop(0, 0, 0)


class CashRegister:

    @staticmethod
    def cash_report_write():
        with open("file.txt", "a") as file:
            file.write(str(f'{datetime.datetime.now()}\n'))
            file.write(str(f'Current profit by item Naftizinum: ${shop.item_profit1}\n'))
            file.write(str(f'Remained amount of Naftizinum: {shop.naftizinum.in_stock} pcs.\n'))
            file.write(str(f'Current profit by item Cocainum: ${shop.item_profit2}\n'))
            file.write(str(f'Remained amount of Cocainum: {shop.cocainum.in_stock} pcs.\n'))
            file.write(str(f'Current profit by item Askorbinum: ${shop.item_profit3}\n'))
            file.write(str(f'Remained amount of Askorbinum: {shop.askorbinum.in_stock} pcs.\n'))
            file.write(str(f'Total profit: ${shop.item_profit1 + shop.item_profit2 + shop.item_profit3}\n\n'))

    @staticmethod
    def cash_report_read():
        with open("file.txt", "r") as file1:
            file_read = file1.read().splitlines()
        return file_read


shop.sell_smth()
CashRegister.cash_report_write()

