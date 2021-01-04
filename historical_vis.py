import pandas as pd

historical_data = pd.read_csv('historical.csv')
historical_data['begins_at'] = pd.to_datetime(historical_data['begins_at'])
historical_data.set_index('begins_at', inplace=True)


import mplfinance as mpf
from symbols import symbols
import os

if not os.path.isdir('historical_plots'):
    os.mkdir('historical_plots')

from colors import COLOR_GREEN, COLOR_RED, COLOR_CYAN, COLOR_END
s = 1
for symbol in symbols:
    progress_str = f'{COLOR_CYAN}{s}/{len(symbols)}{COLOR_END}\t'
    try:
        mpf.plot(historical_data.loc[historical_data['symbol'] == symbol],
            title=symbol,
            type='candle',
            volume=True,
            mav=(5, 10, 15),
            savefig=f'{os.path.abspath(os.getcwd())}/historical_plots/{symbol}.png')
        print(f'{progress_str}{COLOR_GREEN}✓ Plotted {symbol}{COLOR_END}')
    except:
        print(f'{progress_str}{COLOR_RED}✕ Plot failed for {symbol}{COLOR_END}')
    s += 1
