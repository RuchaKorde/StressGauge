"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
         This app can be used to keep in check your stress levels!!
        </p>
    """, unsafe_allow_html=True)

    st.markdown(""" <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
     </style> """, unsafe_allow_html=True)