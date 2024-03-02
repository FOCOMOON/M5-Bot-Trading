import orders
import time
import MetaTrader5 as mt5

#login_result = mt5.initialize(login=102942782, server='Exness-MT5Real15',password='Ii23_focus') #real
login_result = mt5.initialize(login=********, server='Exness-MT5Trial7',password='*********') #Demo

if login_result:
    print("Login to MT5 successful!")
else:
    print("Failed to login to MT5!")
    mt5.shutdown()
    exit(1)

print("1 : EURUSDm")
print("2 : AUDUSDm")
symbol = int(input("Choose currency pair : "))

if symbol == 1:
    real_symbol = "EURUSDm"
elif symbol == 2:
    real_symbol = "AUDUSDm"

orders.STOPLOSS = 100
orders.TAKEPROFIT = 10

x = True

while x == True:
    timeframe = mt5.TIMEFRAME_H1

# Request historical data
    data = mt5.copy_rates_from_pos(real_symbol, timeframe, 0, 100)  # Adjust the number of bars as needed

# Calculate the moving averages
    sma_fast = sum(data[i][4] for i in range(20)) / 20
    sma_slow = sum(data[i][4] for i in range(50)) / 50

# Print the moving averages
    print("SMA(20):", sma_fast)
    print("SMA(50):", sma_slow)

# Decide whether to buy or sell
    if sma_fast > sma_slow:
        orders.open_position(real_symbol, 0.01, "sell")
        print("sell signal")
        time.sleep(500)

    elif sma_fast < sma_slow:
        orders.open_position(real_symbol, 0.01, "buy")
        print("buy signal")
        time.sleep(500)
    
    else:
        print("No signal")

