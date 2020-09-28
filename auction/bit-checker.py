import requests as r
import math
import time

# SLOTHPIXEL API https://docs.slothpixel.me/

# with open('api-key','r') as f:
#     key = f.read()

items = {
    'God Potion': [[], 2000],
    'Kat Flower': [[], 500],
    'Heat Core': [[], 3000],
    'Hyper Catalyst Upgrade': [[], 300],
    'Ultimate Carrot Candy Upgrade': [[], 8000],
    'Colossal Experience Bottle Upgrade': [[], 1200],
    'Jumbo Backpack Upgrade': [[], 4000],
    'Hologram': [[], 2000]
}

ac = r.get('https://api.hypixel.net/skyblock/auctions').json()  # Auction Pg 0
pages = ac['totalPages']

# print(next(iter(items)))
# print(items)

for pg in range(0, pages):
    a = r.get(f'https://api.hypixel.net/skyblock/auctions?page={pg}').json()
    # auctions = [{}, {}, ...]
    auctions = a['auctions']

# auc = {item_name: xxx, bin: true}
    for auc in auctions:
        if 'bin' in auc:
            if auc['item_name'] in items:
                items[auc['item_name']][0].append(auc['starting_bid'])
        else:
            continue
    print('{}/{}'.format(pg, pages))
    time.sleep(0.75)

for i in items:
    if len(items[i][0]) == 0:
        print(f'{i} has empty value.')
        continue
    else:
        items[i][0].sort()
        print(f'Lowest BIN for {i} is {items[i][0][0]}, resulting in {items[i][0][0]/items[i][1]} per bit.')


# print(items)
