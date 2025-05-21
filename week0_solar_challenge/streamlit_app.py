# streamlit_app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    sierra = pd.read_csv("data/sierra_leone_clean.csv")

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierra["Country"] = "Sierra Leone"

    return pd.concat([benin, togo, sierra], ignore_index=True)

df = load_data()

# --- Sidebar ---
st.sidebar.title("🌍 Solar Data Filter")
selected_countries = st.sidebar.multiselect("Select Countries", df["Country"].unique(), default=df["Country"].unique())
selected_feature = st.sidebar.selectbox("Select Feature", ["GHI", "DNI", "DHI", "Tamb", "RH", "WS"])

# --- Filtered Data ---
filtered_df = df[df["Country"].isin(selected_countries)]

# --- Header ---
st.title("☀️ Solar Data Discovery Dashboard")
st.markdown("Analyze and compare solar energy potential across **Benin**, **Togo**, and **Sierra Leone**.")

# --- Line Chart (Time Series Placeholder) ---
st.subheader(f"📈 {selected_feature} Distribution by Country")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Country", y=selected_feature, ax=ax)
st.pyplot(fig)

# --- Summary Statistics ---
st.subheader("📋 Summary Statistics")
summary = filtered_df.groupby("Country")[[selected_feature]].agg(["mean", "median", "std"]).round(2)
st.dataframe(summary)

# --- Average GHI Bar Chart ---
st.subheader("🔋 Average GHI by Country")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(data=filtered_df, x="Country", y="GHI", estimator="mean", errorbar=None, ax=ax2)
ax2.set_ylabel("GHI (W/m²)")
st.pyplot(fig2)

# --- Scatter Plot: Tamb vs GHI ---
st.subheader("🌡️ Ambient Temp vs GHI (Bubble Size = RH)")
fig3, ax3 = plt.subplots(figsize=(8, 5))
scatter = ax3.scatter(
    filtered_df["Tamb"], filtered_df["GHI"],
    s=filtered_df["RH"], alpha=0.5, c=filtered_df["RH"], cmap="coolwarm"
)
ax3.set_xlabel("Ambient Temperature (°C)")
ax3.set_ylabel("GHI (W/m²)")
st.pyplot(fig3)
