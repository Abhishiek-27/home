import streamlit as st
import pandas as pd


expected_columns = {
    "Disbursement": {"no", "amount", "date"},
    "Invoice": {"no", "name"},
}


st.title(" File Upload and Validation Tool")


uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])


file_type = st.selectbox("Select File Type", options=["Disbursement", "Invoice"])


if st.button("Upload File"):
    if uploaded_file is None:
        st.warning("Please upload a file before clicking upload.")
    else:
        try:

            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)


            df.columns = [col.strip().lower() for col in df.columns]


            required_cols = expected_columns[file_type]


            actual_cols = set(df.columns)

            if actual_cols == required_cols:
                st.success(" Uploaded Successfully")
                st.dataframe(df)
            else:
                st.error(" Incorrect Columns Found.")
                st.markdown(f"**Expected Columns:** `{', '.join(sorted(required_cols))}`")
                st.markdown(f"**Found Columns:** `{', '.join(sorted(actual_cols))}`")

        except Exception as e:
            st.error(f" Error reading file: {str(e)}")
