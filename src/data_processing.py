import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df = df.sort_values('Date')
    df['Profit Margin'] = (df['Gross Profit'] / df['Total Revenue']) * 100
    df['Premium Share'] = (df['Premium Revenue'] / df['Total Revenue']) * 100
    df['Ad Share'] = (df['Ad Revenue'] / df['Total Revenue']) * 100
    df['QoQ Revenue Growth'] = df['Total Revenue'].pct_change() * 100
    df['Gross Margin'] = (df['Gross Profit'] / df['Total Revenue']) * 100
    df = df.fillna(0)
    return df
