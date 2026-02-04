import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load saved models
model = joblib.load("models/nutriclass_model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoder = joblib.load("models/food_encoder.pkl")

st.set_page_config(page_title="NutriClass App", layout="centered")

st.title("🥗 NutriClass – Food Classification App")
st.write("Enter nutritional values to predict the food name")

# Input fields
calories = st.number_input("Calories")
protein = st.number_input("Protein")
fat = st.number_input("Fat")
carbs = st.number_input("Carbs")
sugar = st.number_input("Sugar")
fiber = st.number_input("Fiber")
sodium = st.number_input("Sodium")
cholesterol = st.number_input("Cholesterol")
glycemic = st.number_input("Glycemic Index")
water = st.number_input("Water Content")
serving = st.number_input("Serving Size")

meal_type = st.selectbox("Meal Type", ["Breakfast","Lunch","Dinner","Snack"])
prep_method = st.selectbox("Preparation Method", ["Raw","Boiled","Fried","Grilled"])

is_vegan = st.selectbox("Is Vegan", [0,1])
is_gluten_free = st.selectbox("Is Gluten Free", [0,1])

# Simple encoding for demo
meal_map = {"Breakfast":0,"Lunch":1,"Dinner":2,"Snack":3}
prep_map = {"Raw":0,"Boiled":1,"Fried":2,"Grilled":3}

meal_encoded = meal_map[meal_type]
prep_encoded = prep_map[prep_method]

# Predict button
if st.button("Predict Food"):
    input_data = np.array([[calories, protein, fat, carbs, sugar, fiber, sodium,
                            cholesterol, glycemic, water, serving,
                            meal_encoded, prep_encoded, is_vegan, is_gluten_free]])

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)
    food_name = encoder.inverse_transform(prediction)

    st.success(f"Predicted Food: {food_name[0]}")
