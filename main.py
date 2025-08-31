import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from py_vollib.black_scholes import black_scholes
from py_vollib.black_scholes.greeks.analytical import delta


# Configuration Area
Ticker = "SPY"
OPTION_TYPE = "C"  # use C for call and P for put
Time_To_Expiration = 30  # in days
Risk_Free_Rate = 0.05  # annual


def get_options(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    expirations = stock.options

    target_expiration = datetime.now() + timedelta(days=Time_To_Expiration)
    closest_expiration = min(expirations, key=lambda d: abs(
        datetime.strptime(d, '%Y-%m-%d') - target_expiration))

    print(f"Selected expiration date: {closest_expiration}")
    chain = stock.option_chain(closest_expiration)
    return chain.calls, chain.puts, closest_expiration
