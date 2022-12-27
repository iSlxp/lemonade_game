import random as rand
day_count = 1
lemonade_cost = 
def day():
    weather_list = ["hot", "cold", "rainy", "snowy", "cloudy"]
    weather = rand.choice(weather_list)
    print("Welcome to the lemonade game!")
    print(f"Day {day_count}: ")
    print("Weather: {}".format(weather))

    print("How much would you like to charge for a lemonade?")
    lemonade_price = float(input("--> "))
    if lemonade_price <= 1.00:
        customers_percent100 = True
    elif lemonade_price <= 2.00:
        customers_percent80 = True
    elif lemonade_price <= 3.50:
        customers_percent50 = True
    elif lemonade_price <= 5.00:
        customers_percent30 = True
    else:
        customers_percent10 = True

    seen_customers = rand.randint(1,500)

    if customers_percent100:
        purchase_count = seen_customers
        print(f"You saw {seen_customers} people today, and out of them, {purchase_count} of them bought your lemonade!")
        profit = purchase_count * lemonade_price 
    def daily_bill():
        print(f"Day: {day_count}")
        print(f"Seen People: {seen_customers}")
        print(f"Amount of sales made: {purchase_count}")
        print(f"Price of each lemonade: {lemonade_price}")
        print(f"")
        day_count += 1


