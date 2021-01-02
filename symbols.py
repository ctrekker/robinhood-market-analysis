import re

with open('symbols.csv', 'r') as symbols_io:
    symbols = re.split(r',\s*', symbols_io.read())