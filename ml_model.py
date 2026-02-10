import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from utils import generate_commentary

# -----------------------------
# 1. Load Data
# -----------------------------
def load_data(csv_path="data/final.csv"):
    """
    Load dataset and ensure Month column is datetime.
    """
    df = pd.read_csv(csv_path)
    df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
    df = df.sort_values('Month').dropna()
    return df

# -----------------------------
# 2. Preprocess Features
# -----------------------------
def preprocess_features(df, target='BoZ_Policy_Rate'):
    """
    Exclude Month and target columns.
    Returns scaled features, target, scaler, and feature names.
    """
    X = df.drop(columns=['Month', target])
    y = df[target]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler, X.columns.tolist()

# -----------------------------
# 3. Define ML Models
# -----------------------------
def get_models():
    """
    Returns dictionary of models for evaluation.
    """
    return {
        "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
        "Linear Regression": LinearRegression(),
        "XGBoost": XGBRegressor(n_estimators=200, random_state=42, objective='reg:squarederror')
    }

# -----------------------------
# 4. Evaluate Models
# -----------------------------
def evaluate_models(df, target='BoZ_Policy_Rate'):
    """
    Trains multiple models on a time-based split and evaluates performance.
    Returns:
        - results_df: R² scores
        - trained_models: dictionary of trained models in memory
        - scaler: StandardScaler fitted on features
        - feature_cols: list of feature names
    """
    X_scaled, y, scaler, feature_cols = preprocess_features(df, target)

    # Time-based 80:20 split
    split_index = int(len(df) * 0.8)
    X_train, X_test = X_scaled[:split_index], X_scaled[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    models = get_models()
    results = []
    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        results.append({"Model": name, "R2 Score": r2})
        trained_models[name] = model  # store trained model in memory

    results_df = pd.DataFrame(results)
    return results_df, trained_models, scaler, feature_cols

# -----------------------------
# 5. Predict Policy Rate
# -----------------------------
def predict_policy_rate(input_df, model, scaler, feature_cols):
    """
    Predicts numeric policy rate and generates Hold/Raise/Lower signal with BoZ-style commentary.
    Args:
        input_df: DataFrame with feature columns + current BoZ_Policy_Rate
        model: trained ML model
        scaler: StandardScaler fitted on training features
        feature_cols: list of features used in training
    Returns:
        numeric_prediction: float
        signal: str ('Hold', 'Raise', 'Lower')
        commentary: str (IMF/BoZ-style)
    """
    # Scale input features
    X_input = scaler.transform(input_df[feature_cols])
    numeric_prediction = model.predict(X_input)[0]

    # Determine policy signal
    current_rate = input_df['BoZ_Policy_Rate'].values[0]
    if numeric_prediction > current_rate + 0.05:
        signal = "Raise"
    elif numeric_prediction < current_rate - 0.05:
        signal = "Lower"
    else:
        signal = "Hold"

    # Generate commentary
    commentary = generate_commentary(numeric_prediction, signal, input_df)
    return numeric_prediction, signal, commentary
