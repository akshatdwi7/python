import asyncio
import ccxt
import numpy as np
from numba import njit

@njit
def calculate_signal(prices):
    # Example: Simple moving average crossover
    short_window = np.mean(prices[-5:])
    long_window = np.mean(prices[-20:])
    return short_window > long_window

async def fetch_market_data(exchange, symbol):
    return await exchange.fetch_ticker(symbol)

async def trade_logic():
    exchange = ccxt.binance({'enableRateLimit': True})
    symbol = 'BTC/USDT'
    prices = []

    while True:
        ticker = await fetch_market_data(exchange, symbol)
        prices.append(ticker['last'])
        if len(prices) > 20:
            signal = calculate_signal(np.array(prices))
            if signal:
                print(f"Buy Signal for {symbol} at {ticker['last']}")
            prices.pop(0)
        await asyncio.sleep(0.01)  # Adjust based on API rate limits

asyncio.run(trade_logic())
