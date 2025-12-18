import streamlit as st
import pandas as pd

st.title("Multipoly Excel Data App")

# Step 1: File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

# Step 2: Check if file is uploaded
if uploaded_file is not None:
    # Read the uploaded Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)
    
    # Step 3: Display the data
    st.subheader("Preview of Excel Data")
    st.dataframe(df)

    # Step 4: Example: Show column names
    st.write("Columns in your file:", df.columns.tolist())

    # Step 5: Optional – basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

else:
    st.warning("Please upload an Excel file to continue.")
