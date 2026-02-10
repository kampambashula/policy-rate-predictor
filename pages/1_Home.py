import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Central Bank Forecast Tool",
    layout="wide",
)

# -----------------------------
# Header
# -----------------------------
st.title("🏦 Central Bank Policy Rate Forecast Tool")
st.markdown(
    """
Welcome to the **Central Bank Policy Rate Forecast Tool**!  
This interactive platform allows you to explore macroeconomic variable trends and forecast the **Bank of Zambia policy rate** using machine learning models.
"""
)

# -----------------------------
# Features Section
# -----------------------------
st.markdown("## 🔹 Features & Highlights")
st.markdown("""
- **Policy Rate Forecasting:** Generates **Hold / Raise / Lower** signals with predicted rates.
- **IMF / Central Bank-Grade Commentary:** Dynamic insights based on inflation, liquidity, lending rates, exchange rates, and monetary aggregates.
- **Macro Trends:** Visualize key indicators such as inflation, liquidity ratio, lending rates, exchange rates, and broad money (M2) over time.
- **Scenario Analysis:** Simulate different macro conditions in the sidebar and see how predictions change.
- **Multiple ML Models:** Compare Random Forest, Linear Regression, and XGBoost performance on time-based evaluation.
""")

# -----------------------------
# How to Use
# -----------------------------
st.markdown("## 📝 How to Use")
st.markdown("""
1. Use the **'Macro Trends' page** to explore historical data on key economic indicators.  
2. Go to the **'Policy Prediction' page** to generate forecasts and detailed IMF-style commentary.  
3. Adjust macroeconomic inputs in the sidebar to perform **scenario analysis**.  
4. Use the **'ML Model Evaluation' page** to compare model performance and residuals over time.
""")

# -----------------------------
# Credits & Author Info
# -----------------------------
st.markdown("## 👤 About / Credits")
st.markdown("""
- **Author:** Kampamba Shula 
- **Expertise:** Economics, Machine Learning, Software Development  
- **Purpose:** Provide an interactive, policy-grade tool for forecasting the Bank of Zambia policy rate.  
- **Disclaimer:** This tool is for **educational and policy simulation purposes** only. It does not constitute official advice.
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("© 2026 Central Bank Forecast Tool. Built with ❤️ using Python, Streamlit, and ML models.")
