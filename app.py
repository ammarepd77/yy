import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# Load data from Excel file
data = pd.read_excel("data.xlsx")

# Prepare data for training
X = data[['Input1', 'Input2', 'Input3']]
y = data['Output']

# Train machine learning model
model = LinearRegression()
model.fit(X, y)

# Create Streamlit app
st.title("Sum of Three Inputs")
st.write("Enter the values for Input1, Input2, and Input3 to predict the output.")

# Create input fields for user to enter values
input1 = st.number_input("Input1:")
input2 = st.number_input("Input2:")
input3 = st.number_input("Input3:")

# Make prediction using trained machine learning model
prediction = model.predict([[input1, input2, input3]])

# Display predicted output to user
st.write("The predicted output is:", prediction[0])




