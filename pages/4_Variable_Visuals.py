import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Macro Variable Trends")
st.title("Macro Variable Trends")

# Load data
df = pd.read_csv("data/final.csv")
df['Month'] = pd.to_datetime(df['Month'], errors='coerce')

# Select variable to plot
variables = df.columns.tolist()
variables.remove("Month")

selected_var = st.selectbox("Select variable to visualize", variables)

fig = px.line(df, x='Month', y=selected_var, title=f"{selected_var} over time")
fig.update_layout(xaxis_title="Month", yaxis_title=selected_var)
st.plotly_chart(fig, use_container_width=True)

# Optional: show table
if st.checkbox("Show data table"):
    st.dataframe(df[['Month', selected_var]])
