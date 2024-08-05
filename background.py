import streamlit as st
import base64


def add_bg_from_local(): 
    image_path = r"C:/Users/alroy/OneDrive/Documents/AIMIT/SEM 4/Background DNP/growth-economy-with-coins-concept.jpg" # Update this path to match your image path
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpeg"};base64,{encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

