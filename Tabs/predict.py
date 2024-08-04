"""This module contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Stress Level Prediction")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                Gather the following information using a smartwatch or other health monitoring device:
            </p>
        """, unsafe_allow_html=True)
    
    # Add a subheader
    st.subheader("Input Your Health Metrics:")

    # Take input of features from the user with explanations
    sr = st.slider("Snoring Rate (times per hour)", int(df["sr"].min()), int(df["sr"].max()), help="The average number of times you snore per hour.")
    rr = st.slider("Respiration Rate (breaths per minute)", int(df["rr"].min()), int(df["rr"].max()), help="The number of breaths you take per minute.")
    bt = st.slider("Body Temperature (°F)", int(df["bt"].min()), int(df["bt"].max()), help="Your body temperature in Fahrenheit.")
    lm = st.slider("Limb Movement (times per night)", float(df["lm"].min()), float(df["lm"].max()), help="The number of times your limbs move during sleep.")
    bo = st.slider("Blood Oxygen (%)", float(df["bo"].min()), float(df["bo"].max()), help="The percentage of oxygen in your blood.")
    rem = st.slider("Rapid Eye Movement (hours)", float(df["rem"].min()), float(df["rem"].max()), help="The amount of time you spend in the REM sleep phase.")
    sh = st.slider("Sleeping Hours (hours)", float(df["sh"].min()), float(df["sh"].max()), help="The total number of hours you sleep.")
    hr = st.slider("Heart Rate (beats per minute)", float(df["hr"].min()), float(df["hr"].max()), help="Your average heart rate in beats per minute.")

    # Create a list to store all the features
    features = [sr, rr, bt, lm, bo, rem, sh, hr]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Analyzing stress level...")

        # Print the output according to the prediction
        if prediction == 1:
            st.success("The person has a low stress level 🙂")
            st.markdown("### Tips for maintaining low stress levels:\n- Continue with regular exercise.\n- Maintain a balanced diet.\n- Practice mindfulness and relaxation techniques.")
        elif prediction == 2:
            st.warning("The person has a medium stress level 😐")
            st.markdown("### Tips for managing medium stress levels:\n- Consider incorporating stress-reducing activities like yoga or meditation.\n- Ensure you're getting enough sleep.\n- Limit caffeine and alcohol intake.")
        elif prediction == 3:
            st.error("The person has a high stress level! 😞")
            st.markdown("### Tips for managing high stress levels:\n- Take breaks during work or study sessions.\n- Seek social support from friends and family.\n- Consider speaking to a professional for stress management.")
        elif prediction == 4:
            st.error("The person has a very high stress level!! 😫")
            st.markdown("### Immediate actions for very high stress levels:\n- Prioritize relaxation and downtime.\n- Avoid stressful situations if possible.\n- Seek professional help if needed.")
        else:
            st.success("The person is stress-free and calm 😄")
            st.markdown("### Great job!\n- Continue with your healthy lifestyle habits to maintain this state.")

        

