from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
import streamlit as st
import pandas as pd
import pickle
import base64

st.markdown(
    """
    <style>
    body {
        background-color:  #ff0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Load the pre-trained machine learning model
# Replace with your actual path to the pre-trained model
model = pickle.load(open('svm1.pkl', 'rb'))

# Function to calculate BMI
def calculate_bmi(height, weight):
    height_m = height / 100  # Convert height from cm to m
    bmi = weight / (height_m ** 2)
    return bmi

# Function to predict diabetes
def predict_diabetes(features):
    prediction = model.predict(features)
    return prediction

# Function to generate diabetes report in PDF
def generate_diabetes_report(patient_name, age, BMI, Insulin, Glucose, Pregnancies, BloodPressure,features, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    c.saveState()
    c.setFillColorRGB(0.8, 0.9, 1)  # Gradient from light blue
    c.rect(0, 0, 612, 792, fill=True)
    c.restoreState()

    
    logo_path = "C:\\Users\\Paras Sharma\\OneDrive\\Desktop\\project\\diab.jpg"  # Replace with your logo's file path
    c.drawImage(logo_path, 490, 740, width=70, height=50)

    c.setFont("Helvetica-Bold", 25)
    st.header('')
    c.drawString(200, 759, "PATIENT REPORT")
   
    #c.line(100, 700, 500, 740)
    y_coordinate = 700
  

    content = f"Patient Name: {patient_name} \n" 
    content += f"Age: {age} \n"
    content += f"BMI: {BMI} \n"
    content += f"Insulin: {Insulin} \n"
    content += f"Glucose: {Glucose} \n"
    content += f"Pregnancies: {Pregnancies} \n"
    content += f"Blood Pressure: {BloodPressure} \n"

    input_data = pd.DataFrame([features])
    prediction = predict_diabetes(input_data)[0]
    if prediction == 1:
        diabetes_result = "The individual is likely to have diabetes."
    else:
        diabetes_result = "The individual is likely not to have diabetes."

    content += f"Diabetes Prediction: {diabetes_result}\n"

    c.setFont("Helvetica", 10)
    for line in content.split('\n'):
        c.drawString(100, y_coordinate, line)
        y_coordinate -= 20  # Move to the next line
   # c.drawString(100, 700, content)

    c.save()

# Streamlit app
def main():
    st.header("Diabetes Prediction and Report Generation", divider = 'rainbow')
    st.write("Enter the following details to predict diabetes and generate a report:")

    # Input features
    patient_name = st.text_input("Enter your name")
    gender = st.radio("Select your gender", ["Male", "Female", "Other"])

    age = st.slider("Age", 1, 120, 25)
    height = st.slider("Height (in cm)", 50, 250, 170)
    weight = st.slider("Weight (in kg)", 30, 200, 70)

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    st.markdown("<h3 style='text-align: left; color: white;'>Glucose Level Type</h3>", unsafe_allow_html=True)
    glucose_type = st.radio("", ["Before having food", "After having food"])
    if glucose_type == "Before having food":
        glucose_range = (70, 200)
        normal_glucose_value = 135
    else:
        glucose_range = (70, 400)
        normal_glucose_value = 170

    st.header(' ')
    st.markdown("<h3 style='text-align: left; color: white;'>Glucose Level</h3>", unsafe_allow_html=True)
    glu = st.slider("", glucose_range[0], glucose_range[1], normal_glucose_value)
    st.markdown(f"- Normal Range For Glucose: Between {glucose_range[0]} mg/dL and {glucose_range[1]}mg/dL")

    st.markdown("<h3 style='text-align: left; color: white;'>Insulin</h3>", unsafe_allow_html=True)
    insulin = st.slider("", 0, 846, 79)
    st.markdown("- Normal Range For Insulin: Between 5 and 15μU/mL")
    




    st.markdown("<h3 style='text-align: left; color: white;'>Blood Pressure</h3>", unsafe_allow_html=True)
    bp = st.slider("", 0, 350, 72)
    st.markdown("- Normal Range For BP: Between 90/60mmHg and 120/80mmHg")

    if gender == "Female":
        st.markdown("<h3 style='text-align: left; color: white;'>Number of Pregnancies</h3>", unsafe_allow_html=True)
        preg = st.slider("", 0, 17, 1)
    else:
        preg = 0

    # Create a feature dictionary
    features = {
        'Pregnancies': preg,
        'Glucose': glu,
        'BloodPressure': bp,
        'Insulin': insulin,
        'BMI': bmi,
        'Age': age
    }

    # Create a DataFrame from the features
    input_data = pd.DataFrame([features])

    if st.button("Predict"):
        prediction = predict_diabetes(input_data)
        st.write("### Prediction:")
        if prediction[0] == 1:
            st.write("The individual is likely to have diabetes.")
            st.markdown('<a href="http://localhost:8501/doctors">Contact Doctors</a>', unsafe_allow_html=True)

        else:
            st.write("The individual is likely not to have diabetes.")

    if st.button("Generate Report"):
        if patient_name:
            pdf_filename = "diabetes_report.pdf"
            generate_diabetes_report(patient_name, age, bmi, insulin, glu, preg, bp,features, pdf_filename)
            st.success("Diabetes report generated successfully!")

            # Provide download link for the report
            st.write("Download your report:")
            with open(pdf_filename, "rb") as f:
                bytes = f.read()
                b64 = base64.b64encode(bytes).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="{pdf_filename}">Click here to download the report</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Please enter your name to generate the report.")

if __name__ == "__main__":
    main()


# Create a link to another page within the app
#st.markdown('<a href="http://localhost:8501/doctors">Go to the next page</a>', unsafe_allow_html=True)
