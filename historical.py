import robin_stocks as rs
import numpy as np
import pandas as pd

import auth  # Runs our auth file so we are authenticated with Robinhood
from symbols import symbols  # Import the 'symbols' list from symbols.py


interval, span = 'day', 'year'
historical_data = {}
failed_symbols = []

COLOR_GREEN, COLOR_RED, COLOR_CYAN, COLOR_END = '\033[92m', '\033[91m', '\033[96m', '\033[0m'
for symbol in symbols:
    try:
        historical_data[symbol] = rs.stocks.get_stock_historicals(symbol, interval=interval, span=span)
        print(f'{COLOR_GREEN}✓ {symbol}{COLOR_END}')
    except KeyboardInterrupt:
        exit()
    except:
        print(f'{COLOR_RED}✕ {symbol}{COLOR_END}')
        failed_symbols.append(symbol)

print(f'Results: {COLOR_GREEN}{len(symbols)-len(failed_symbols)} succeeded{COLOR_END} {COLOR_RED}{len(failed_symbols)} failed{COLOR_END}')


dataframe_file = 'historical.csv'

historical_formatted = {}
for symbol in  historical_data.keys():
    symbol_data = historical_data[symbol]

    for symbol_entry in symbol_data:
        for symbol_entry_key in symbol_entry.keys():
            if not symbol_entry_key in historical_formatted:
                historical_formatted[symbol_entry_key] = []
            historical_formatted[symbol_entry_key].append(symbol_entry[symbol_entry_key])
    
historical_df = pd.DataFrame(historical_formatted, columns=list(historical_formatted.keys()))
historical_df.to_csv(dataframe_file)
print(f'Saved to {COLOR_CYAN}{dataframe_file}{COLOR_END}')
