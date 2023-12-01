import streamlit as st
import datetime
import pickle
import mysql.connector
from PIL import Image
import io
import re



st.set_page_config(
    page_title="Login",
    page_icon="	:closed_lock_with_key:",)



image = Image.open("C:\\Users\\Paras Sharma\\OneDrive\\Desktop\\project\\diafit.jpg")
new_image = image.resize((110,110))
st.image(new_image,  output_format='JPEG')

st.markdown(
    """
    <style>
    .centered-image {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white ;'>DIAFIT </h1>", unsafe_allow_html=True)

if "NAME" not in st.session_state:
    st.session_state["NAME"]=""
if "GENDER" not in st.session_state:
    st.session_state["GENDER"]=""
if "EMAIL" not in st.session_state:
    st.session_state["EMAIL"]=""




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="db"


)
mycursor=mydb.cursor()
print("Connection Established")
def validate_name(input_name):
    if input_name.isalpha():
        return True
    else:
        st.warning("Please enter valid characters for the name (only letters).")
        return False

def validate_phone(phone):
    # Check if the phone number contains only digits and has a length of 10
    if re.match(r"^[0-9]{10}$", phone):
        return True
    else:
        st.warning("Please enter a valid 10-digit phone number.")
        return False

def validate_email(email):
    # Regular expression pattern for a valid email
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    if re.match(email_pattern, email):
        return True
    else:
        st.warning("Please enter a valid email.")
        return False

# Create Streamlit App

def main():
   
    st.subheader("Enter the patient's details.." , divider = 'rainbow')
    NAME =st.text_input('Name: ', st.session_state["NAME"])
    if not validate_name(NAME):
        return

    
    min_year = 1970
    max_year = 2023

    current_date = datetime.date.today()  # Get the current system date
    DOB = st.date_input("DOB", current_date, min_value=datetime.date(min_year, 1, 1), max_value=datetime.date(max_year, 12, 31))

    
    PHONE = st.text_input('Contact Number(+91): ', max_chars=10)
    PHONE = PHONE.strip()  # Remove any leading/trailing spaces
    if PHONE and (not PHONE.isdigit() or len(PHONE) != 10):
        st.warning("Please enter a valid 10-digit phone number.")
        return

    PHONE = validate_phone(PHONE)
    if PHONE is None:
        return

    
    EMAIL=st.text_input('Email: ', st.session_state["EMAIL"])
    if not validate_email(EMAIL):  # Validate email using validate_email
        return

    
    GENDER = st.selectbox(
    'Enter gender',
    ('F', 'M', 'other'))
    if st.button("Submit"):
        sql= "insert into login(NAME,DOB,PHONE,EMAIL,GENDER) values(%s,%s,%s,%s,%s)"
        val= (NAME,DOB,PHONE,EMAIL,GENDER)
        mycursor.execute(sql,val)
        mydb.commit()
        st.success("Success!!")
    
if __name__ == "__main__":
    main()
    
     
