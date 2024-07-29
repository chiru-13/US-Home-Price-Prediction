import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load trained models
lr_model = joblib.load('lr_model.pkl')
ridge_model = joblib.load('ridge_model.pkl')
lasso_model = joblib.load('lasso_model.pkl')
rf_model = joblib.load('rf_model.pkl')

# Load the scaler
scaler = joblib.load('scaler.pkl')

# Streamlit app
st.title("US Home Price Prediction")

# User input
consumer_price_index = st.number_input("Consumer Price Index", value=260.0)
gdp = st.number_input("GDP (in billions)", value=21000.0)
median_income = st.number_input("Median Household Income", value=60000.0)
housing_starts = st.number_input("Housing Starts (in thousands)", value=1000.0)
sp500 = st.number_input("S&P 500 Index", value=4000.0)
dow_jones = st.number_input("Dow Jones Index", value=34000.0)
mortgage_rate = st.number_input("Mortgage Rate (%)", value=3.5)

# Creating input DataFrame
input_data = pd.DataFrame({
    'ConsumerPriceIndex': [consumer_price_index],
    'GDP': [gdp],
    'MedianHouseholdIncome': [median_income],
    'S&P500': [sp500],
    'DowJones': [dow_jones],
})

# Adding lagged and interaction features (dummy values for lags)
input_data['HomePriceIndex_Lag1Months'] = 200.0  # Replace with actual values if available
input_data['HomePriceIndex_Lag2Months'] = 195.0  # Replace with actual values if available
input_data['HomePriceIndex_Lag3Months'] = 190.0  # Replace with actual values if available
input_data['S&P500_Lag1Months'] = sp500
input_data['S&P500_Lag2Months'] = sp500
input_data['S&P500_Lag3Months'] = sp500
input_data['DowJones_Lag1Months'] = dow_jones
input_data['DowJones_Lag2Months'] = dow_jones
input_data['DowJones_Lag3Months'] = dow_jones
input_data['HomePriceIndex_RollMean3Months'] = 195.0  # Replace with actual values if available

input_data['CPI_MedianIncome'] = consumer_price_index * median_income
input_data['GDP_HousingStarts'] = gdp * housing_starts
input_data['S&P500_MortgageRate'] = sp500 * mortgage_rate
input_data['DowJones_MortgageRate'] = dow_jones * mortgage_rate

# Scale input data
input_data_scaled = scaler.transform(input_data)

# Predictions
lr_pred = lr_model.predict(input_data_scaled)[0]
ridge_pred = ridge_model.predict(input_data_scaled)[0]
lasso_pred = lasso_model.predict(input_data_scaled)[0]
rf_pred = rf_model.predict(input_data)[0]

# Combined prediction (average)
combined_pred = (lr_pred + ridge_pred + lasso_pred + rf_pred) / 4

# Display result
st.write(f"Final Prediction: ${combined_pred:,.2f}")
