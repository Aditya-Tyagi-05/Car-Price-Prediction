import streamlit as st
import pandas as pd
import pickle
import numpy as np
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

# Cache model and data loading to improve performance
@st.cache_resource
def load_model():
    return pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@st.cache_data
def load_car_data():
    df = pd.read_csv('cleaned.csv')
    return (sorted(df['company'].unique()),
            sorted(df['name'].unique()),
            sorted(df['year'].unique(), reverse=True),
            df['fuel_type'].unique())

# Initialize model and data
model = load_model()
companies, car_models, years, fuel_types = load_car_data()

# Streamlit app
st.title("Car Price Predictor")

# Use columns for better layout
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Company", companies, index=1)
    model_name = st.selectbox("Model", car_models)
    year = st.selectbox("Year", years)

with col2:
    fuel = st.selectbox("Fuel Type", fuel_types)
    driven = st.number_input("Kilometers Driven", min_value=0.0, step=100.0, format="%.0f")

# Predict button and result
if st.button("Predict Price"):
    with st.spinner("Calculating..."):
        # Create prediction DataFrame more efficiently
        input_data = pd.DataFrame({
            'name': [model_name],
            'company': [company],
            'year': [year],
            'kms_driven': [driven],
            'fuel_type': [fuel]
        })
        
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Price: Rs.{np.round(prediction, 2):,.2f}")