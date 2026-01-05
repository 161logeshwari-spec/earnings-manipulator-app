import streamlit as st
import pandas as pd
import joblib

st.title("Earnings Manipulation Detection App")

# Load trained model
model = joblib.load("model.pkl")

uploaded_file = st.file_uploader(
    "Upload Excel file", type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Remove target column if present
    df = df.drop(columns=["Manipulator"], errors="ignore")

    predictions = model.predict(df)

    df["Prediction"] = predictions

    st.subheader("Prediction Results")
    st.dataframe(df)
