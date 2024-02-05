from tabulate import tabulate
from random import randint

# initial prices
INITIAL_PRICES = {
    "a": 5,
    "b": 5,
    "c": 10,
    "d": 10,
    "e": 25
}

# init variables
day = 1
money = 50
prices = dict(INITIAL_PRICES)
stock = {}
delta = {}

for key in prices:
    stock[key] = 0
    dx = prices[key] // 5
    delta[key] = randint(dx * -1, dx)

def display_game():

    # print header
    header = f"money: ${money}\t"
    header += f"day: {day}/20"
    print(header)

    # tabulate items
    table_headers = ["item", "amount", "price", "delta"]

    data = []
    for item in prices:

        cur_row = []
        cur_row.append(item)
        cur_row.append(stock[item])
        cur_row.append(prices[item])

        # convert change in price to nice graphic
        delta_text = "-"
        if delta[item] > 0:
            delta_text = "^"
        elif delta[item] < 0:
            delta_text = "v"

        if abs(delta[item]) > min(2 * INITIAL_PRICES[item] / 5, 10):
            delta_text *= 3
        elif abs(delta[item]) > min(INITIAL_PRICES[item] / 5, 5):
            delta_text *= 2
        cur_row.append(delta_text)

        data.append(cur_row)


    print(tabulate(data, headers=table_headers))

while day < 20:
    display_game()
    input("enter something: ")