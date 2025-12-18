import streamlit as st
import pandas as pd

st.title("Multipoly Excel Data App")

# 1️⃣ File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    # 2️⃣ Read Excel file
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
    else:
        # 3️⃣ Show data preview
        st.subheader("Preview of your data")
        st.dataframe(df)

        # 4️⃣ Show columns
        st.write("Columns in your file:", df.columns.tolist())

        # 5️⃣ Basic statistics
        st.subheader("Basic Statistics")
        st.write(df.describe())

        # 6️⃣ Example: Select a column to analyze
        column_to_view = st.selectbox("Select column to view", df.columns)
        st.write(f"Values in {column_to_view}:")
        st.write(df[column_to_view])

else:
    st.info("Please upload an Excel file to continue.")
