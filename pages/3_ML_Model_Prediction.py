import streamlit as st
import pandas as pd
from ml_model import load_data, evaluate_models, predict_policy_rate
from utils import generate_commentary
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Policy Rate Prediction", layout="wide")
st.title("Bank of Zambia Policy Rate Forecast - Policy Brief")

# -----------------------------
# Load Data
# -----------------------------
df = load_data()
latest_row = df.iloc[[-1]]  # use last month as default

# -----------------------------
# Sidebar: Input Macro Indicators
# -----------------------------
st.sidebar.header("Input Macro Indicators (Scenario Analysis)")
input_dict = {}
for col in ['Inflation_Annual', 'Broad_Money_M2', 'USDZMW',
            'Lending_Margin', 'Average_Lending_Rate', 
            'Weighted_Interbank_Rate', 'Actual_Ratio_%', 
            'BoZ_Policy_Rate']:
    input_dict[col] = st.sidebar.number_input(col, value=float(latest_row[col]))

input_df = pd.DataFrame(input_dict, index=[0])

# -----------------------------
# Train/Evaluate Models
# -----------------------------
results_df, trained_models, scaler, feature_cols = evaluate_models(df)

# -----------------------------
# Model Selection
# -----------------------------
default_model = results_df.sort_values('R2 Score', ascending=False).iloc[0]['Model']
selected_model_name = st.selectbox("Select ML Model", results_df['Model'].tolist(),
                                   index=list(results_df['Model']).index(default_model))
selected_model = trained_models[selected_model_name]

# -----------------------------
# Make Prediction & Generate Commentary
# -----------------------------
numeric_pred, signal, commentary = predict_policy_rate(input_df, selected_model, scaler, feature_cols)

# -----------------------------
# Policy Brief Layout
# -----------------------------

# Headline: Policy Signal
st.markdown(f"## Monetary Policy Recommendation: **{signal.upper()}**")
st.markdown(f"### Predicted Policy Rate: **{numeric_pred:.2f}%**")

# Key Indicators Table
key_indicators = {
    "Inflation (Annual %)": input_df['Inflation_Annual'].values[0],
    "BoZ Policy Rate (%)": input_df['BoZ_Policy_Rate'].values[0],
    "Average Lending Rate (%)": input_df['Average_Lending_Rate'].values[0],
    "Liquidity Ratio (%)": input_df['Actual_Ratio_%'].values[0],
    "USD/ZMW": input_df['USDZMW'].values[0],
    "Broad Money (M2)": input_df['Broad_Money_M2'].values[0]
}



# Commentary Section
st.markdown("### Commentary & Insights")
st.markdown(commentary)

# -----------------------------
# Trend Charts Section
# -----------------------------
st.markdown("### Trends of Key Indicators")

# Inflation Trend
fig_infl = px.line(df, x='Month', y='BoZ_Policy_Rate', title="BoZ_Policy_Rate (%)")
st.plotly_chart(fig_infl, use_container_width=True)


