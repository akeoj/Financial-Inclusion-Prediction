import streamlit as st
from mode import *

st.title("Financial Inclusion Prediction")
st.write("Enter customer details to predict if they have a bank account")

# User Inputs
year = st.number_input("Year", min_value=1900, max_value=2100, value=2018)
uniqueid = st.text_input("Unique ID", "uniqueid_1")
location_type = st.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
household_size = st.number_input("Household Size", min_value=1, max_value=20, value=5)
age_of_respondent = st.number_input("Age of Respondent", min_value=18, max_value=100, value=30)
gender_of_respondent = st.selectbox("Gender", ["Male", "Female"])
relationship_with_head = st.selectbox("Relationship with Head", ["Head of Household", "Spouse", "Child", "Other relative", "Parent", "Other"])
marital_status = st.selectbox("Marital Status", ["Married/Living together", "Single/Never Married", "Divorced/Separated", "Widowed"])
education_level = st.selectbox("Education Level", ["No formal education", "Primary education", "Secondary education", "Vocational/Specialised training", "Tertiary education"])
job_type = st.selectbox("Job Type", ["Self employed", "Formally employed Government", "Formally employed Private", "Informally employed", "Other employment"])

# Make prediction
if st.button("Predict"):
    data = [year, uniqueid, location_type, cellphone_access, household_size, age_of_respondent, 
            gender_of_respondent, relationship_with_head, marital_status, education_level, job_type]
    result = prediction(data)
    st.success(result)
