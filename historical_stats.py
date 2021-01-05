import pandas as pd

historical_data = pd.read_csv('historical.csv')
historical_data['begins_at'] = pd.to_datetime(historical_data['begins_at'])


symbol = 'MSFT'
start_date = pd.to_datetime('2020-12-1 00:00:00+00:00')
end_date = pd.to_datetime('2020-12-31 00:00:00+00:00')
selected_data = historical_data.loc[(historical_data['symbol'] == symbol) & (historical_data['begins_at'] >= start_date) & (historical_data['begins_at'] <= end_date)]
print(selected_data.describe())