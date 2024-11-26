import pandas as pd
import streamlit as st

st.title("Motor Selection App")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsm", "xlsx"])

if uploaded_file:
    try:
        # Read the uploaded file
        motor_df = pd.read_excel(uploaded_file, sheet_name="Motor Type", engine="openpyxl")
        gearbox_df = pd.read_excel(uploaded_file, sheet_name="Gearboxes", engine="openpyxl")
        remark_table_df = pd.read_excel(uploaded_file, sheet_name="Remarks", engine="openpyxl")
        
        # Select motor
        motor_types = motor_df['Motor Type'].unique()
        selected_motor = st.selectbox("Select Motor", motor_types)
        st.write(f"You selected: {selected_motor}")
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("Please upload an Excel file.")
