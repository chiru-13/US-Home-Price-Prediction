# US Home Price Prediction

## Project Overview

This project provides a web application for predicting US home prices using multiple regression models. The application leverages Linear Regression, Ridge Regression, Lasso Regression, and Random Forest models. The final prediction is a combined result from all models, offering a comprehensive estimate based on user inputs.

### Features

- User-friendly web interface built with Streamlit.
- Predicts home prices based on various economic indicators and user input.
- Utilizes multiple regression models and combines their predictions for accuracy.

## Project Structure
- **`US_home_prices_models.py`**: Script for data preprocessing, feature engineering, model training, and saving models.
- **`app.py`**: Streamlit application for user interaction and prediction.
- **`models/`**: Directory containing saved model files and scaler.
  - `lr_model.pkl`
  - `ridge_model.pkl`
  - `lasso_model.pkl`
  - `rf_model.pkl`
  - `scaler.pkl`

## Installation

### Prerequisites

- Python 3.7 or later
- `pip`

### Clone the Repository

```bash
git clone https://github.com/yourusername/us-home-price-prediction.git
cd us-home-price-prediction
```

### Install Required Packages

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```



## Usage

### Run the Streamlit App

Start the Streamlit application to interact with the model and make predictions:

```bash
streamlit run app.py
```

### Using the Web App

1. **Open the Streamlit app**: After running the above command, the Streamlit app will open in your default web browser or provide a local URL.

2. **Input Data**: Enter the values for various economic indicators in the provided fields.

3. **Get Prediction**: The app will display predictions from each individual model and the combined prediction based on your inputs.

## Model Training

The models used in this application were trained on historical US home price data and various economic indicators. The training involved:

- **Feature Engineering**: Creating lagged features, rolling statistics, and interaction features.
- **Model Training**: Using Linear Regression, Ridge Regression, Lasso Regression, and Random Forest to predict home prices.
- **Model Evaluation**: Evaluating models using metrics like Mean Squared Error (MSE) and R-squared (R2).

The trained models and scaler are saved in the `models/` directory and are used by the Streamlit app to make predictions.

## Data

The data used for training includes the following economic indicators:

- Home Price Index
- S&P 500 Index
- Dow Jones Index
- Interest Rate
- Consumer Price Index
- Unemployment Rate
- GDP
- Median Household Income
- Housing Starts
- Mortgage Rate
