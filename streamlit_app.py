import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ----------------- Sidebar Menu -----------------
page = st.sidebar.radio(
    "Navigation",
    ["Home","Taxi Model","Credit Model"]
)
page_bg = """
<style>
    /* الخلفية الرئيسية للنص */
    .stApp {
        background-color: #FFF8E7;  /* خلفية الصفحة */
        color: #333333;             /* لون النص */
    }

    /* لون الشريط الجانبي */
    .css-1d391kg {                
        background-color: #000000;  /* أسود */
        color: #FFFFFF;             /* نص أبيض في sidebar */
    }

    /* أزرار التطبيق */
    .stButton>button {
        background-color: #FF8C42;
        color: white;
        border-radius: 8px;
        height: 40px;
        width: 100%;
    }

    /* العناوين */
    h1, h2, h3, .css-1v0mbdj-StreamlitMarkdown {
        color: #1E3A8A;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

if page == "Home":
    st.title("The Survivors ⚡")
    st.info('Welcome to Survivors Team App')
    st.header("Our Team :-")
    st.subheader("   Heba Hassan")
    st.subheader("   Bassant Mohammed")
# 🚕 Taxi Model Page

elif page == "Taxi Model":
    st.header("🚕 Pick up Trip")
    st.subheader("⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛")
 
    
    model1 = joblib.load("taxi_model.pkl")
    

# 💳 Credit Model Page

elif page == "Credit Model":
    st.header("💳 Cre.")
    model2 = joblib.load("best_random_forest_model.pkl")



