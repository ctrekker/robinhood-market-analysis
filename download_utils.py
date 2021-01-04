import pandas as ps


# Converts a robin stocks API response into a DataFrame
def rh_dict_to_df(res):
    formatted = {}
    for symbol in  res.keys():
        symbol_data = res[symbol]

        for symbol_entry in symbol_data:
            for symbol_entry_key in symbol_entry.keys():
                if not symbol_entry_key in formatted:
                    formatted[symbol_entry_key] = []
                formatted[symbol_entry_key].append(symbol_entry[symbol_entry_key])
    return formatted