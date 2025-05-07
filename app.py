import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from sklearn.preprocessing import MinMaxScaler
import traceback

# Title
st.title("📈 Apple Stock Price Predictor")
st.markdown("Enter the **last 30 closing prices** (comma-separated) to predict the next closing price using LSTM + EMA20.")

# Try loading the model
try:
    model = load_model(
        "E:/Apple Stock Price prediction project/applestockprice_model.h5",
        custom_objects={'mse': MeanSquaredError()}
    )
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.text(traceback.format_exc())  # Show full traceback for debugging
    st.stop()

# EMA calculation
def calculate_ema(data):
    data_series = pd.Series(data)
    ema = data_series.ewm(span=20, adjust=False).mean()
    return ema

# Prediction function
def predict_price(last_30_days_data):
    df = pd.DataFrame(last_30_days_data, columns=['Close'])
    df['EMA20'] = calculate_ema(df['Close'])
    features = df[['Close', 'EMA20']].values

    # Normalize data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)

    # Prepare input sequence (last 20 data points)
    sequence = np.array(scaled_data[-20:])
    sequence = sequence.reshape(1, 20, 2)

    # Make prediction
    pred = model.predict(sequence)

    # Validate prediction shape
    if pred.shape != (1, 1):
        raise ValueError(f"Unexpected prediction shape: {pred.shape}")

    # Inverse transform prediction
    pred_zero = np.array([[pred[0][0], 0]])  # only inverse 'Close'
    actual_pred = scaler.inverse_transform(pred_zero)
    return actual_pred[0][0]

# Input UI
user_input = st.text_area(
    "🔢 Enter last 30 close prices (comma-separated):",
    placeholder="e.g. 150.25, 151.30, ..., 155.45"
)

# Predict button
if st.button("Predict"):
    try:
        # Parse and validate input
        prices = [float(p.strip()) for p in user_input.split(',') if p.strip()]
        if len(prices) < 30:
            st.warning("⚠️ Please enter at least 30 closing prices.")
        else:
            predicted = predict_price(prices)
            st.success(f"📊 Predicted Next Closing Price: **${predicted:.2f}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.text(traceback.format_exc())

st.write("👆 Paste your closing prices above and hit Predict.")

if 'prices' in locals() and 'predicted' in locals():
    st.subheader("📉 Price Trend")
    fig, ax = plt.subplots()
    ax.plot(prices, label='Last 30 Prices', marker='o')
    ax.axhline(y=predicted, color='green', linestyle='--', label='Predicted Price')
    ax.legend()
    st.pyplot(fig)
