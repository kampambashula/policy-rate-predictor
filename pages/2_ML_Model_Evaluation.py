import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from ml_model import load_data, evaluate_models

st.set_page_config(page_title="ML Model Evaluation")
st.title("ML Model Evaluation - Policy Rate Forecasting")

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

# -----------------------------
# Evaluate Models (no data leakage)
# -----------------------------
results_df, trained_models, scaler, feature_cols = evaluate_models(df)

st.subheader("Model Performance (R² on time-based test set)")
st.dataframe(results_df)

best_model_name = results_df.sort_values('R2 Score', ascending=False).iloc[0]['Model']
st.success(f"Top-performing model: {best_model_name}")

# -----------------------------
# Time-based test set
# -----------------------------
split_index = int(len(df)*0.8)
df_test = df.iloc[split_index:].copy()
df_test['Month'] = pd.to_datetime(df_test['Month'], errors='coerce')

# Generate predictions and residuals for each model
for model_name, model in trained_models.items():
    X_test = scaler.transform(df_test[feature_cols])
    df_test[model_name] = model.predict(X_test)
    df_test[f"{model_name}_Residual"] = df_test[model_name] - df_test['BoZ_Policy_Rate']

# -----------------------------
# Actual vs Predicted Plot
# -----------------------------
st.subheader("Actual vs Predicted Policy Rate")

models_to_plot = st.multiselect(
    "Select models to plot", 
    results_df['Model'].tolist(), 
    default=[best_model_name]
)

# Melt for Plotly
plot_df = df_test.melt(
    id_vars=['Month', 'BoZ_Policy_Rate'], 
    value_vars=models_to_plot, 
    var_name='Model', 
    value_name='Predicted'
)

fig = px.line(
    plot_df,
    x='Month',
    y='Predicted',
    color='Model',
    markers=True,
    title="Actual vs Predicted Policy Rate"
)

# Add actual line
fig.add_scatter(
    x=df_test['Month'],
    y=df_test['BoZ_Policy_Rate'],
    mode='lines+markers',
    name='Actual Policy Rate',
    line=dict(color='black', width=3, dash='dash')
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Policy Rate (%)",
    legend_title="Model",
    hovermode="x unified"
)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Residual Plot
# -----------------------------
st.subheader("Prediction Residuals (Predicted - Actual)")

residual_cols = [f"{model}_Residual" for model in models_to_plot]
residual_df = df_test[['Month'] + residual_cols]

# Melt for Plotly
residual_melted = residual_df.melt(id_vars='Month', var_name='Model', value_name='Residual')

fig_resid = px.line(
    residual_melted,
    x='Month',
    y='Residual',
    color='Model',
    markers=True,
    title="Prediction Residuals Over Time"
)
fig_resid.update_layout(
    xaxis_title="Month",
    yaxis_title="Residual (%)",
    legend_title="Model",
    hovermode="x unified"
)
st.plotly_chart(fig_resid, use_container_width=True)
