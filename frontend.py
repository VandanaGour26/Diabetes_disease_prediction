import streamlit as st
import pickle
import numpy as np


#  Load the model
model_path = "diabetes_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)


# Streamlit Page Configuration
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# Add custom CSS for styling
page_element="""
<style>
 
[data-testid="stAppViewContainer"]{
  background-image:url("https://images.pexels.com/photos/6941878/pexels-photo-6941878.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
  text-color:white;
  background-size:cover;
}
div[data-testid="stTextInput"],div[data-testid="stNumberInput"]{
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); 
  border-radius: 8px;
  padding: 8px;
  transition:0.3s;
  font-size:30px;
}
  div[data-testid="stMarkdownContainer"] {
        font-size: 18px ;
        font-weight: bold;
        color: white;    
    }
   div[data-testid="stButton"] > button {
        background-color: red !important;   
        color: white !important;   
        border-radius: 8px;   
        padding: 10px 20px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
    }
   div[data-testid="stButton"] > button:hover {
        background-color: darkred !important;   
        box-shadow: 3px 3px 12px rgba(255, 0, 0, 0.5);  
    }

   *{
        font-family:'Pacifico';
        color: white;
        
    }
 .fancy-heading {
            background-color:white;  
            padding: 10px;
            border-radius: 10px;
            font-size: 32px;
            text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);
            text-align: center;
            color: darkblue;
            font-weight: bold;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            margin: 8px;
        }
</style>
<div class="fancy-heading"> Diabetes prediction</div>
"""

st.markdown(page_element,unsafe_allow_html=True)

#  Create a form for user input
# st.title("Diabetes Prediction")
st.write("Enter your health details below and predict whether you have diabetes or not.")

# Create input fields
pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose Level", 0, 200, 100)
blood_pressure = st.number_input("Blood Pressure", 0, 150, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 500, 79)
bmi = st.number_input("BMI", 0.0, 50.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.number_input("Age", 1, 120, 25)

# Create a button for prediction
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

    # Make prediction
    prediction = model.predict(input_data)


    # Display Result
    if prediction[0] == 1:
        st.error("⚠️ You are likely to have diabetes. Please consult a doctor.")
    else:
        st.success("✅ You are not likely to have diabetes. Keep maintaining a healthy lifestyle!")



