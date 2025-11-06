import pandas as pd

def kpi_summary(df):
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    return {
        "Total Revenue": latest["Total Revenue"],
        "Gross Profit": latest["Gross Profit"],
        "Profit Margin": latest["Profit Margin"],
        "Premium Share": latest["Premium Share"],
        "Ad Share": latest["Ad Share"],
        "MAUs": latest["MAUs"],
        "QoQ Growth": latest["QoQ Revenue Growth"],
        "Sales Cost": latest["Sales and Marketing Cost"],
        "R&D Cost": latest["Research and Development Cost"],
        "Admin Cost": latest["Genreal and Adminstraive Cost"],
        "Revenue Change": latest["Total Revenue"] - prev["Total Revenue"]
    }
