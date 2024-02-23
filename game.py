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
FORECAST_CORRECTION = 0.3

SHOW_FORECAST_VALUES = False

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

# util to clamp values
def clamp(x, low, high):
    return max(low, min(high, x))

def display_help():
    with open("help.txt", "r") as file:
        print(file.read())

def display_game():

    # print header
    header = f"money: ${money}\t"
    header += f"day: {day}/20"
    print(header)

    # tabulate items
    table_headers = ["item", "amount", "price", "forecast"]
    if SHOW_FORECAST_VALUES:
        table_headers.append("%")
        table_headers.append("df")

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

        if SHOW_FORECAST_VALUES:
            cur_row.append(round(forecast[item], 2))
            cur_row.append(round(dforecast[item], 2))

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

# main menu code
print()
print("welcome to MEDIEVAL MERCHANT SIMULATOR DELUXE™")
print()
print("type a command:")
print("- start")
print("- help")
print()

while True:
    command = input()
    if command in ["start", "s"]:
        break
    elif command in ["help", "h"]:
        display_help()
    else:
        print("invalid command")
        continue

# game code
while day <= 20:

    while True:

        print()
        display_game()
        print()        

        args = input("")
        args = args.split()
        print()

        if args[0] in ["next", "n"]:
            break
        elif args[0] in ["buy", "b"]:

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
                print(f"invalid item: {item}")
                continue

            # call the actual function
            buy(item, amount)
            break

        elif args[0] in ["sell", "s"]:

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
                print(f"invalid item: {item}")
                continue

            # call the actual function
            sell(item, amount)
            break

        else:
            print("invalid command")

    day += 1

    # update prices based on deltas
    for item in prices:

        max_change = max(1, round(INITIAL_PRICES[item] / 4))
        change = randint(1, max_change)
        if random() < forecast[item]:
            prices[item] += change
        else:
            prices[item] -= change

        prices[item] = max(1, prices[item])

    # update forecast randomly
    for item in forecast:
        forecast[item] += (dforecast[item] - 0.5) * FORECAST_VOLATILITY
        forecast[item] = clamp(forecast[item], 0, 1)
        dforecast[item] = random() + FORECAST_CORRECTION * (0.5 - forecast[item])
        dforecast[item] = clamp(dforecast[item], 0, 1)

sold = 0
for item in stock:
    sold += stock[item] * prices[item]
    stock[item] = 0

money += sold
print(f"sold all your remaining goods for ${sold}")
print(f"wow! you ended with ${money}!")