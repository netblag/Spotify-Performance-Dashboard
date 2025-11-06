# Spotify Performance Dashboard

🎧 **Spotify Performance Dashboard** is a professional data analytics dashboard that visualizes Spotify's quarterly financial and user performance from 2016–2023. It is designed to provide insights into revenue, profit, user growth, and cost structure in an interactive and user-friendly interface.

---

## Dataset

The dataset used for this project is publicly available here:  
[Spotify Quarterly Financials & Users](https://www.kaggle.com/datasets/mauryansshivam/spotify-revenue-expenses-and-its-premium-users)  

It includes:
- Quarterly financial data (Revenue, Costs, Gross Profit)
- User data (MAUs, Premium MAUs, Ad MAUs)
- ARPU and other key metrics

---

## Features

- Key Performance Indicators (KPIs):
  - Total Revenue (€M)
  - Gross Profit (€M)
  - Profit Margin (%)
  - QoQ Growth (%)
  - Premium Share (%)
  - Ad Share (%)
  - MAUs (M)
  - Revenue Change (€M)
- Interactive charts:
  - Revenue vs. Profit over time
  - User Growth over time
  - Cost Breakdown (last quarter)
- Theme switcher:
  - Light, Dark, and Spotify custom theme
- Fully responsive layout
- Developed using Streamlit and Plotly

---

## Analysis & Insights

- **Revenue & Profit Trends:** Total revenue steadily increased from 2016–2023, with some seasonal fluctuations. Gross profit shows a similar upward trend, and profit margin stabilized around 25–30% in recent years.
- **User Growth:** MAUs (monthly active users) have grown consistently, driven primarily by Premium subscriptions. Ad-supported users form a smaller, more volatile share.
- **Cost Breakdown:** Marketing and R&D expenses are the largest cost components. Admin costs remain stable.
- **Revenue Drivers:** Premium subscriptions are the main revenue driver (>85%), while ad revenue contributes a smaller portion but shows growth in recent quarters.
- **QoQ Growth:** Some quarters show negative QoQ growth due to seasonality, especially around the end of the year.

---

## Project Structure

Spotify/
│
├─ app/
│ └─ streamlit_app.py # Main Streamlit app
│
├─ src/
│ ├─ data_processing.py # Load and clean CSV data
│ ├─ analysis.py # KPI calculations
│ └─ visualizations.py # Plotly charts functions
│
├─ data/
│ └─ Spotify Quarterly.csv # Dataset
│
└─ README_EN.md # English documentation
└─ README_FA.md # Persian documentation

---


---

## How It Works

1. **Data Loading:** Reads the dataset and cleans numeric columns.
2. **KPI Calculation:** Computes Total Revenue, Gross Profit, Profit Margin, MAUs, Premium & Ad share, QoQ growth, and Revenue Change.
3. **Visualization:** Generates interactive charts using Plotly.
4. **Theme Switching:** Users can select Light, Dark, or Spotify custom theme.

---

## Installation & Usage

```bash
git clone https://github.com/netblag/Spotify-Dashboard.git
cd Spotify-Dashboard
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

<p align="center">
  <a href="https://github.com/netblag">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/github/ccc?viewbox=auto" />
      <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/github?viewbox=auto" />
      <img alt="GitHub" height="90" src="https://cdn.simpleicons.org/github?viewbox=auto" />
    </picture>
  </a>
  
