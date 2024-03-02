import MetaTrader5 as mt5

def calculate_moving_average(symbol, timeframe, period):
    # Request historical data
    data = mt5.copy_rates_from_pos(symbol, timeframe, 0, period)

    # Calculate the moving average
    sma = sum(data[i][4] for i in range(period)) / period

    return sma

def generate_signals(symbol, timeframe, period_fast, period_slow):
    # Calculate the moving averages
    sma_fast = calculate_moving_average(symbol, timeframe, period_fast)
    sma_slow = calculate_moving_average(symbol, timeframe, period_slow)

    # Decide whether to buy or sell
    if sma_fast > sma_slow:
        return "Buy signal"
    elif sma_fast < sma_slow:
        return "Sell signal"
    else:
        return "No signal"

# Connect to the MetaTrader 5 terminal
if not mt5.initialize():
    print("Failed to initialize MT5")
    exit(1)

# Set the desired symbol and timeframe
symbol = "EURUSDm"
timeframe = mt5.TIMEFRAME_H1

# Set the periods for the moving averages
period_fast = 20
period_slow = 50

# Generate signals
signal = generate_signals(symbol, timeframe, period_fast, period_slow)
print(signal)

# Disconnect from the MetaTrader 5 terminal
mt5.shutdown()
