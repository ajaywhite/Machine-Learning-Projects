import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from sklearn.preprocessing import MinMaxScaler

st.title("📈 Apple Stock Price Predictor")
st.markdown("Enter the **last 30 closing prices** (comma-separated) to predict the next closing price using LSTM + EMA20.")

# Safe model loading
try:
    model = load_model("applestockprice_model.h5", custom_objects={'mse': MeanSquaredError()})
    st.write("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# EMA calculation
def calculate_ema(data):
    return pd.Series(data).ewm(span=20, adjust=False).mean()

# Prediction function
def predict_price(last_30_days_data):
    df = pd.DataFrame(last_30_days_data, columns=['Close'])
    df['EMA20'] = calculate_ema(df['Close'])
    features = df[['Close', 'EMA20']].values

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    sequence = np.array(scaled_data[-20:])
    sequence = sequence.reshape(1, 20, 2)

    pred = model.predict(sequence)
    if pred.shape != (1, 1):
        raise ValueError(f"Unexpected prediction shape: {pred.shape}")

    pred_zero = np.array([[pred[0][0], 0]])
    actual_pred = scaler.inverse_transform(pred_zero)
    return actual_pred[0][0]

# UI input
user_input = st.text_area("🔢 Enter last 30 close prices (comma-separated):", placeholder="e.g. 150.25, 151.30, ..., 155.45")

if st.button("Predict"):
    try:
        prices = [float(p.strip()) for p in user_input.split(',')]
        if len(prices) < 30:
            st.warning("⚠️ Please enter at least 30 prices.")
        else:
            predicted = predict_price(prices)
            st.success(f"📊 Predicted Next Closing Price: **${predicted:.2f}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

st.write("👆 Paste your closing prices above and hit Predict.")
