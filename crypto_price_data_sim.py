import time,random,os
from colorama import Fore as c
coins = {"Bitcoin": 10000.00,"Eutherium": 40000.00,"Solana": 12909.99,"Doge": 3999.99,"PEPE": 4900.00,"Memecoin": 200.00,"TRX": 500934.93,"IDKCoin": 1900000.00}
coinNetWorth = sum(coins.values())
def updateCoins(data):
    for coin in data:
        change = random.uniform(-12000000,12000000)
        data[coin] += change
        data[coin] = round(max(data[coin],0),2)
try:
    os.system('clear')
    print(c.CYAN+'Crypto Price Change Simulator\n'+c.RESET)
    while True:
        updateCoins(coins)
        coinNetChange = sum(coins.values())
        NetChange = coinNetChange-coinNetWorth
        for key, value in coins.items():
            print(c.CYAN+f'{key}'+c.RED+' -> '+c.GREEN+f'$+{value:,.2f}'+c.RESET)
        print(c.GREEN+f'\nNet Change -> $+{NetChange:,.2f}')
        print(f'\033[{len(coins)+3}A')
        time.sleep(0.5)
except KeyboardInterrupt:
    print(c.RED+'Stopped.'+c.RESET)