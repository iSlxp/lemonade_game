import random as rand
lemonade_cost = 2
customers_percentfull = False
customers_percent80 = False
customers_percent50 = False
customers_percent30 = False
customers_percent10 = False
customers_percent01 = False
bank_money = 0

def game():
    weather_list = ["hot", "cold", "rainy", "snowy", "cloudy"]
    weather = rand.choice(weather_list)
    print("Welcome to the lemonade game!")
    print("Weather: {}".format(weather))
    print(f"Bank Money: {bank_money}")

    print("How much would you like to charge for a lemonade?")
    lemonade_price = float(input("--> "))
    if lemonade_price <= 1.00:
        customers_percentfull = True
    elif lemonade_price <= 2.00:
        customers_percent80 = True
    elif lemonade_price <= 3.50:
        customers_percent50 = True
    elif lemonade_price <= 5.00:
        customers_percent30 = True
    elif lemonade_price <= 10:
        customers_percent10 = True
    else:
        customers_percent01 = True

    seen_customers = rand.randint(1,500)

    print(lemonade_cost)
    if customers_percentfull:
        purchase_count = seen_customers
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")

        money_made = purchase_count * lemonade_price 

    elif customers_percent80:
        purchase_count = int(seen_customers * 0.8)
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")

        money_made= purchase_count * lemonade_price

    elif customers_percent50:
        purchase_count = int(seen_customers * 0.5)
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")
        money_made = purchase_count * lemonade_price
    elif customers_percent30:
        purchase_count = int(seen_customers * 0.3)
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")
        money_made = purchase_count * lemonade_price
    elif customers_percent10:
        purchase_count = int(seen_customers * 0.1)
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")
        money_made = purchase_count * lemonade_price
    elif customers_percent01:
        purchase_count = int(seen_customers * 0.01)
        print(f"You saw {seen_customers} people today, and out of them, {int(purchase_count)} of them bought your lemonade!")
        money_made = purchase_count * lemonade_price
    else:
        print("Error.")
    print(lemonade_cost * purchase_count)
    total_expense = lemonade_cost * purchase_count
    total_profit = money_made - total_expense

    print("-----------------")
    print(f"Seen People: {seen_customers}")
    print(f"Amount of sales made: {int(purchase_count)}")
    print(f"Cost of each lemonade: ${lemonade_cost}")
    print(f"Price of each lemonade: {lemonade_price}")
    print(f"Total Money Made: ${int(money_made)}")
    print(f"Total Expense: ${int(total_expense)}")
    print(f"Total Profit: ${int(total_profit)}")
    print("------------------")
    bank_money += total_profit




