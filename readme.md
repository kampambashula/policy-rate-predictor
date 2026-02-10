# Central Bank Policy Rate Forecast Tool

Author: Kampamba Shula
Year: 2026

## Overview

The Central Bank Policy Rate Forecast Tool is an interactive, IMF / Central Bank-grade dashboard designed to:

- Forecast the Bank of Zambia policy rate using machine learning models.

- Generate Hold / Raise / Lower signals with dynamic, BoZ-targeted commentary.

- Explore macroeconomic trends such as inflation, liquidity, lending rates, exchange rates, and broad money (M2).

- Support scenario analysis by adjusting macroeconomic inputs.

This tool combines time-based ML evaluation with interactive visualization to provide policy insights in a professional, central bank-style format.

## Features

Policy Forecasting

Predicts the next Bank of Zambia policy rate and generates actionable signals.

IMF-Style Commentary

Provides detailed insights based on BoZ targets (inflation 6–8%) and key macro indicators.

Multiple ML Models

Includes Random Forest, Linear Regression, and XGBoost with time-based evaluation.

Interactive Scenario Analysis

Adjust macroeconomic variables in the sidebar to test alternative policy outcomes.

Macro Trends Visualization

View historical trends for inflation, liquidity, lending rates, exchange rates, and broad money.

Residuals & Model Accuracy

Evaluate ML model performance over time, including residuals and actual vs predicted charts.

## Pages in the App

Home: Introduction, features, author credits, and instructions.

Macro Trends: Interactive charts of historical macroeconomic indicators.

Policy Prediction: Forecast the policy rate with IMF-style commentary and key indicators table.

ML Model Evaluation: Compare ML model performance (R² scores, residuals, actual vs predicted).

## How It Works

Load the preprocessed dataset (final.csv) containing historical macro indicators and BoZ policy rates.

Train ML models on an 80:20 time-based split to prevent leakage.

Evaluate models and display R² performance, residuals, and prediction accuracy.

Generate policy rate predictions using the selected ML model.

Produce IMF/BoZ-style commentary considering:

Inflation relative to BoZ target (6–8%)

Liquidity ratio

Lending rates

Exchange rate trends

Broad money growth

Display interactive charts and key indicators in a structured, policy brief format.

Author

Kampamba Shula – Economist, Software Developer, ML Enthusiast

This project is for educational and policy simulation purposes only. It does not constitute official advice.

## License

MIT License
