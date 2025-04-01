import streamlit as st
import joblib

model = joblib.load('House_price_pred.pkl')

st.title('House Price Prediction tool')
st.write('Predict the price of your dream house')

Square_Feet = st.number_input('enter desired square footage:')
Num_Bedrooms = st.number_input('enter desired number of bedrooms:')
Num_Bathrooms = st.number_input('enter desired number of bathrooms:')
Num_Floors = st.number_input('enter desired number of floors:')
Year_Built = st.number_input('enter desired year of build:')
Has_Garden = st.number_input('Has a garden: (Enter 1 if you need, else input 0)')
Has_Pool = st.number_input('Has a pool:(Enter 1 if you need, else input 0)')
Garage_Size = st.number_input('desired garage size:')
Location_Score = st.number_input('Desired location score:')
Distance_to_Center = st.number_input('Distance to square:')

if st.button('Predict Price'):
    features =[
    Square_Feet,
    Num_Bedrooms,
    Num_Bathrooms,
    Num_Floors,
    Year_Built,
    Has_Garden,
    Has_Pool,
    Garage_Size,
    Location_Score,
    Distance_to_Center
    ]

    prediction = model.predict([features])[0]          # when you are calling the features list if you don't use the 0 the array will be off by 1
    st.write(f'your predicted price is: ${prediction}')  # in streamlit we use $ to call the function in our for loop 
