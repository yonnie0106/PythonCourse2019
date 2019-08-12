import random

class Portfolio(): # self = portfolio
    def __init__(self):
        self.cash = 0
        self.stock = {}
        self.fund = {}
        self.transactions = []

    def __str__(self):
        stock_list = [ str(k) + " " + str(v) for (k, v) in self.stock.items()]
        sl = '\n'.join(stock_list)
        fund_list = [str(k)+ " " + str(v) for (k, v) in self.fund.items()]
        fl = '\n'.join(fund_list)
        return f"Cash: \n{self.cash} \nStock: \n{sl} \nFund: \n{fl}"

    def addCash(self, amount):
        self.cash += amount
        self.transactions.append(f"Added {amount} dollars")


    def buyStock(self, shares, name):
        if self.cash >= name.stock_price*shares:
            self.cash -= name.stock_price*shares
            self.transactions.append(f"Bought {shares} shares of {name.stock_symbol}")
            if name.stock_symbol in self.stock.keys():
                self.stock[name.stock_symbol] += shares
            else:
                self.stock[name.stock_symbol] = shares
        else:
            return "Can not buy stocks: insufficient cash"


    def buyMutualFund(self, shares, name):
        if self.cash >= 1*shares:
            self.cash -= 1*shares
            self.transactions.append(f"Bought {shares} shares of {name.fund_symbol}")
            if name.fund_symbol in self.fund.keys():
                self.fund[name.fund_symbol] += shares # symbol of the fund that is bought
            else:
                self.fund[name.fund_symbol] = shares
        else:
            return "Can not buy funds: insufficient cash"


    def withdrawCash(self, amount):
        if self.cash < amount:
            return "Can not withdraw : insufficient cash"
        else:
            self.cash -= amount
            self.transactions.append(f"Withdrew {amount} dollars")


    def sellMutualFund(self, symbol, shares):
        if symbol in self.fund.keys():
            if self.fund[symbol] >= shares:
                self.fund[symbol] -= shares
                self.cash += random.uniform(0.9, 1.2)*1*shares
                self.transactions.append(f"Sold {shares} shares of {symbol}")
            else:
                return f"Can not sell funds: insufficient shares of {symbol}"
        else:
            return f"{symbol} does not exist"

    def sellStock(self, name, shares):
        if name.stock_symbol in self.stock.keys():
            if self.stock[name.stock_symbol] >= shares:
                self.stock[name.stock_symbol] -= shares
                self.cash += random.uniform(0.5, 1.5)*name.stock_price*shares
                self.transactions.append(f"Sold {shares} shares of {name.stock_symbol}")
            else:
                return f"Can not sell stocks: insufficient shares of {name.stock_symbol}"
        else:
            return f"{name.stock_symbol} does not exist"

    def history(self):
        for transaction in self.transactions:
            print(transaction)

class Stock():

    def __init__(self, price, symbol):
        self.stock_price = price
        self.stock_symbol = symbol

class MutualFund():

    def __init__(self, symbol):
        self.fund_symbol = symbol




portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)

portfolio.sellMutualFund("BRT", 1)
portfolio.sellStock(s, 1)
portfolio.withdrawCash(50)
portfolio.history()
