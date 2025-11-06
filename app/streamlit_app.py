import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
from src.data_processing import load_data
from src.analysis import kpi_summary
from src.visualizations import revenue_and_profit_chart, user_growth_chart, cost_breakdown_chart

st.set_page_config(page_title="Spotify Dashboard", page_icon="🎧", layout="wide")

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/Spotify Quarterly.csv'))
if not os.path.exists(DATA_PATH):
    st.error("Data file not found")
    st.stop()

df = load_data(DATA_PATH)
kpis = kpi_summary(df)

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

col_a, col_b = st.columns([0.85, 0.15])
with col_a:
    st.title("🎧 Spotify Performance Dashboard")
    st.markdown("Financial & user growth analytics from 2016–2023")
with col_b:
    choice = st.radio("Theme", ["Dark", "Spotify"], index=["Dark", "Spotify"].index(st.session_state.theme))
    st.session_state.theme = choice

theme = st.session_state.theme

# --- Theme setup ---
def apply_theme(theme):
    if theme == "Dark":
        bg_color = "#0E1117"
        text_color = "#FAFAFA"
        accent = "#1DB954"
        plot_theme = "plotly_dark"
    else:  # Spotify
        bg_color = "#121212"
        text_color = "#1DB954"
        accent = "#1DB954"
        plot_theme = {
            "layout": {
                "paper_bgcolor": "#121212",
                "plot_bgcolor": "#121212",
                "font": {"color": "#1DB954"},
                "colorway": ["#1DB954", "#9be7a8", "#f7b267", "#ef476f", "#06d6a0"]
            }
        }
    css = f"""
        <style>
            body {{ background-color: {bg_color}; color: {text_color}; }}
            .stApp {{ background-color: {bg_color}; color: {text_color}; }}
            .stMetric label, .stMetric span {{ color: {text_color} !important; }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    return plot_theme

plot_theme = apply_theme(theme)

cols = st.columns(8)
cols[0].metric("Total Revenue (€M)", f"{kpis['Total Revenue']:.1f}")
cols[1].metric("Gross Profit (€M)", f"{kpis['Gross Profit']:.1f}")
cols[2].metric("Profit Margin (%)", f"{kpis['Profit Margin']:.1f}")
cols[3].metric("QoQ Growth (%)", f"{kpis['QoQ Growth']:.1f}")
cols[4].metric("Premium Share (%)", f"{kpis['Premium Share']:.1f}")
cols[5].metric("Ad Share (%)", f"{kpis['Ad Share']:.1f}")
cols[6].metric("MAUs (M)", f"{kpis['MAUs']:.1f}")
cols[7].metric("Revenue Change (€M)", f"{kpis['Revenue Change']:.1f}")

st.markdown("### 📈 Revenue & Profit")
fig1 = revenue_and_profit_chart(df, theme=theme)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 👥 User Growth")
fig2 = user_growth_chart(df, theme=theme)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 💸 Cost Breakdown")
fig3 = cost_breakdown_chart(df, theme=theme)
if fig3 is not None:
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Developed by Ashkan Ahmadi — netblag")

