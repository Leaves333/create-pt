from tabulate import tabulate
from random import randint, random

# initial prices
INITIAL_PRICES = {
    "wood": 5,
    "ore": 5,
    "herbs": 10,
    "weapons": 15,
    "potions": 25
}
FORECAST_VOLATILITY = 0.6

# init variables
day = 1
money = 50
prices = dict(INITIAL_PRICES)
stock = {}
forecast = {}
dforecast = {}

for key in prices:
    stock[key] = 0
    forecast[key] = random()
    dforecast[key] = random()

def display_game():

    # print header
    header = f"money: ${money}\t"
    header += f"day: {day}/20"
    print(header)

    # tabulate items
    table_headers = ["item", "amount", "price", "forecast"]

    data = []
    for item in prices:

        cur_row = []
        cur_row.append(item)
        cur_row.append(stock[item])
        cur_row.append(prices[item])

        # convert change in price to nice graphic
        forecast_text = "-"
        if forecast[item] > 0.6:
            forecast_text = "^"
        elif forecast[item] < 0.4:
            forecast_text = "v"

        if abs(forecast[item] - 0.5) > 0.35:
            forecast_text *= 3
        elif abs(forecast[item] - 0.5) > 0.2:
            forecast_text *= 2
        cur_row.append(forecast_text)

        data.append(cur_row)


    print(tabulate(data, headers=table_headers))

def buy(item, quantity):

    global money

    cost = prices[item] * quantity
    if cost <= money:
        stock[item] += quantity
        money -= cost
        print(f"bought {quantity} {item} for ${cost}")
    else:
        print("not enough money")

def sell(item, quantity):

    global money

    if quantity <= stock[item]:
        stock[item] -= quantity
        money += prices[item] * quantity
        print(f"sold {quantity} {item} for ${prices[item] * quantity}")
    else:
        print("not enough in stock")


while day < 20:

    while True:

        print()
        display_game()
        print()        

        args = input("")
        args = args.split()
        print()

        if args[0] == "next":
            break
        elif args[0] == "buy":

            amount = args[1]
            item = args[2]

            # sanitize input
            try:
                amount = int(amount)
            except Exception as err:
                print(f"invalid number: {err}")
                continue

            if amount <= 0:
                print(f"invalid quantity to buy: {amount}")
                continue

            if item not in prices.keys():
                print(f"invalid item: {amount}")
                continue

            # call the actual function
            buy(item, amount)

        elif args[0] == "sell":

            amount = args[1]
            item = args[2]

            # sanitize input
            try:
                amount = int(amount)
            except Exception as err:
                print(f"invalid number: {err}")
                continue

            if amount <= 0:
                print(f"invalid quantity to sell: {amount}")
                continue

            if item not in prices.keys():
                print(f"invalid item: {amount}")
                continue

            # call the actual function
            sell(item, amount)

        else:
            print("invalid command")

    day += 1

    # update prices based on deltas
    for item in prices:

        dx = round(prices[item] / 4)
        if random() < forecast[item]:
            prices[item] += randint(0, dx)
        else:
            prices[item] -= randint(0, dx)

        prices[item] = max(1, prices[item])

    # update forecast randomly
    for item in forecast:
        forecast[item] += (dforecast[item] - 0.5) * FORECAST_VOLATILITY
        forecast[item] = max(0, min(1, forecast[item]))
        dforecast[item] = random()

sold = 0
for item in stock:
    sold += stock[item] * prices[item]
    stock[item] = 0

money += sold
print(f"sold all your remaining goods for ${sold}")
print(f"wow! you ended with ${money}!")