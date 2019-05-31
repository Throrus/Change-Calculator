import random
import decimal

def main():

    print("\n***********************************************************************************************************")
    print("\n\nThis program will generate a random price for an item. \nYou will be prompted to enter the cash needed to pay for the item. \n\nThe program will calculate the change due and generate a list of the bills and coins needed to most efficiently make up that change. \n\nHave fun! \n\n")
    def calculator():
        listing = decimal.Decimal(random.uniform(1,5))
        price = listing.quantize(decimal.Decimal('00.00'))
        print("\n\n\nThe price of the item is: ${} ".format(price))
        def cashola(price):
            cash_input = decimal.Decimal(input("Enter the cash tendered: "))
            cash = cash_input.quantize(decimal.Decimal('00.00'))
            if cash < price:
                print("\nThat isn't enough to pay for the item! ")
                cashola(price)
            else:
                print("You paid: ${}" .format(cash))
            change = decimal.Decimal(cash - price)
            print("\n\nChange Due: ${}".format(change))
            def denom(change):
                bills = {100.00:"One Hundred", 50.00:"Fifty", 20.00:"Twenty", 10.00:"Ten", 5.00:"Five", 1.00:"One"}
                coins = {0.25:"Quarter", 0.10:"Dime", 0.05:"Nickel", 0.01:"Penny"}
                def add_bills(change, bills, coins):
                    tender = []
                    while change >= decimal.Decimal('0.01'):
                        if change >= (decimal.Decimal('100.00')):
                            change -= (decimal.Decimal('100.00'))
                            tender.append(bills[100])
                        elif change >= (decimal.Decimal('50.00')):
                            change -= (decimal.Decimal('50.00'))
                            tender.append(bills[50])
                        elif change >= (decimal.Decimal('20.00')):
                            change -= (decimal.Decimal('20.00'))
                            tender.append(bills[20])
                        elif change >= (decimal.Decimal('10.00')):
                            change -= (decimal.Decimal('10.00'))
                            tender.append(bills[10])
                        elif change >= (decimal.Decimal('5.00')):
                            change -= (decimal.Decimal('5.00'))
                            tender.append(bills[5])
                        elif change >= (decimal.Decimal('1.00')):
                            change -= (decimal.Decimal('1.00'))
                            tender.append(bills[1])
                        elif change >= (decimal.Decimal('0.25')):
                            change -= (decimal.Decimal('0.25'))
                            tender.append(coins[0.25])
                        elif change >= (decimal.Decimal('0.10')):
                            change -= (decimal.Decimal('0.10'))
                            tender.append(coins[0.10])
                        elif change >= (decimal.Decimal('0.05')):
                            change -= (decimal.Decimal('0.05'))
                            tender.append(coins[0.05])
                        elif change >= (decimal.Decimal('0.01')):
                            change -= (decimal.Decimal('0.01'))
                            tender.append(coins[0.01])

                    def count(tender):
                        result = []

                        #Make a change so that it will print a different message if the value is one. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        if tender.count('One Hundred') == 1:
                            result.append("1 One Hundred")
                        elif tender.count('One Hundred') > 1:
                            result.append("{} One Hundreds".format(tender.count("One Hundred")))

                        if tender.count('Fifty') == 1:
                            result.append("1 Fifty")
                        elif tender.count('Fifty') > 1:
                            result.append("{} Fifties".format(tender.count("Fifty")))

                        if tender.count('Twenty') == 1:
                            result.append("1 Twenty")
                        elif tender.count('Twenty') > 1:
                            result.append("{} Twenties".format(tender.count("Twenty")))

                        if tender.count('Ten') == 1:
                            result.append("1 Ten")
                        elif tender.count('Ten') > 1:
                            result.append("{} Tens".format(tender.count("Ten")))

                        if tender.count('Five') == 1:
                            result.append("1 Five")
                        elif tender.count('Five') > 1:
                            result.append("{} Fives".format(tender.count("Five")))

                        if tender.count('One') == 1:
                            result.append("1 One")
                        elif tender.count('One') > 1:
                            result.append("{} Ones".format(tender.count("One")))

                        if tender.count('Quarter') == 1:
                            result.append("1 Quarter")
                        elif tender.count('Quarter') > 1:
                            result.append("{} Quarters".format(tender.count("Quarter")))

                        if tender.count('Dime') == 1:
                            result.append("1 Dime")
                        elif tender.count('Dime') > 1:
                            result.append("{} Dimes".format(tender.count("Dime")))

                        if tender.count('Nickel') == 1:
                            result.append("1 Nickel")
                        elif tender.count('Nickel') > 1:
                            result.append("{} Nickels".format(tender.count("Nickel")))

                        if tender.count('Penny') == 1:
                            result.append("1 Penny")
                        elif tender.count('Penny') > 1:
                            result.append("{} Pennies".format(tender.count("Penny")))

                        print(result)
                    count(tender)
                add_bills(change, bills, coins)
            denom(change)
        cashola(price)
    while True:
        calculator()

if __name__ == "__main__":
    main()
