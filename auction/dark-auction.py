import requests as r
import math
import time, datetime

items = {
    'ender': [],
    'wither': [],
    'parrot_epic': [],
    'parrot_leg': [],
    'turtle_epic': [],
    'turtle_leg': [],
    'jelly_epic': [],
    'jelly_leg': [],
    'sharp_6': [],
    'giant_6': [],
    'power_6': [],
    'growth_6': [],
    'prot_6': [],
    'scroll': [],
    'counter_5': [],
    'bundle': [],
    'plasma': [],
    'hegemony': [],
    'vicious_5': [],
    'sharp_7': [],
    'giant_7': [],
    'power_7': [],
    'growth_7': [],
    'prot_7': [],
}

ac = r.get('https://api.hypixel.net/skyblock/auctions').json()  # Auction Pg 0
pages = ac['totalPages']
lu = ac['lastUpdated']

print('===== DARK AUCTION CHECKER =====')
print('Last Update:', datetime.datetime.fromtimestamp(math.floor(lu/1000)))

for pg in range(0, 4):
    a = r.get(f'https://api.hypixel.net/skyblock/auctions?page={pg}').json()
    # auctions = [{}, {}, ...]
    auctions = a['auctions']
    time.sleep(0.5)

    for auc in auctions:
        if 'bin' in auc:
            aun = auc['item_name']
            aul = auc['item_lore']
            if 'Ender Artifact' in aun:
                items['ender'].append(auc['starting_bid'])
            if 'Wither Artifact' in aun:
                items['wither'].append(auc['starting_bid'])
            if 'Parrot' in aun:
                if auc['tier'] == 'EPIC':
                    items['parrot_epic'].append(auc['starting_bid'])
                elif auc['tier'] == 'LEGENDARY':
                    items['parrot_leg'].append(auc['starting_bid'])
            if 'Turtle' in aun:
                if auc['tier'] == 'EPIC':
                    items['turtle_epic'].append(auc['starting_bid'])
                elif auc['tier'] == 'LEGENDARY':
                    items['turtle_leg'].append(auc['starting_bid'])
            if 'Jellyfish' in aun:
                if auc['tier'] == 'EPIC':
                    items['jelly_epic'].append(auc['starting_bid'])
                elif auc['tier'] == 'LEGENDARY':
                    items['jelly_leg'].append(auc['starting_bid'])
            if 'Dark Auction' in aun:
                items['scroll'].append(auc['starting_bid'])
            if 'Enchanted Book Bundle' in aun:
                items['bundle'].append(auc['starting_bid'])
            if 'Plasma Nucleus' in aun:
                items['plasma'].append(auc['starting_bid'])
            if 'Hegemony' in aun:
                items['hegemony'].append(auc['starting_bid'])
            if 'Enchanted Book' in aun:
                if auc['tier'] == 'UNCOMMON':
                    if 'Counter-Strike V' in aul:
                        items['counter_5'].append(auc['starting_bid'])
                if auc['tier'] == 'RARE':
                    if 'Sharpness VI' in aul:
                        items['sharp_6'].append(auc['starting_bid'])
                    if 'Power VI' in aul:
                        items['power_6'].append(auc['starting_bid'])
                    if 'Giant Killer VI' in aul:
                        items['giant_6'].append(auc['starting_bid'])
                    if 'Growth VI' in aul:
                        items['growth_6'].append(auc['starting_bid'])
                    if 'Protection VI' in aul:
                        items['prot_6'].append(auc['starting_bid'])
                    if 'Vicious V' in aul:
                        items['vicious_5'].append(auc['starting_bid'])
                if auc['tier'] == 'EPIC':       
                    if 'Sharpness VII' in aul:
                        items['sharp_7'].append(auc['starting_bid'])
                    if 'Power VII' in aul:
                        items['power_7'].append(auc['starting_bid'])
                    if 'Giant Killer VII' in aul:
                        items['giant_7'].append(auc['starting_bid'])
                    if 'Growth VII' in aul:
                        items['growth_7'].append(auc['starting_bid'])
                    if 'Protection VII' in aul:
                        items['prot_7'].append(auc['starting_bid'])

for i in items:
    if len(items[i]) == 0:
        print('no data {}'.format(i))
    else:
        items[i].sort()
        print('{} -> {}'.format(i, items[i][0]))
