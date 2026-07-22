import streamlit as st
import pandas as pd
from xgboost import XGBClassifier

# Page settings
st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="⚙️",
    layout="centered"
)

# Load trained XGBoost model
import joblib

model = joblib.load("xgboost_model.pkl")

st.title("⚙️ Predictive Maintenance System")
st.write("Enter machine operating details to predict machine failure.")

# User inputs
machine_type = st.selectbox(
    "Product Type",
    ["L", "M", "H"]
)

air_temperature = st.number_input(
    "Air Temperature (K)",
    min_value=250.0,
    max_value=400.0,
    value=298.0
)

process_temperature = st.number_input(
    "Process Temperature (K)",
    min_value=250.0,
    max_value=450.0,
    value=308.0
)

rotational_speed = st.number_input(
    "Rotational Speed (RPM)",
    min_value=500,
    max_value=4000,
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (Minutes)",
    min_value=0,
    max_value=500,
    value=50
)

# Same encoding used by LabelEncoder:
# H = 0, L = 1, M = 2
type_mapping = {
    "H": 0,
    "L": 1,
    "M": 2
}

if st.button("Predict Machine Failure", use_container_width=True):

    input_data = pd.DataFrame({
        "Type": [type_mapping[machine_type]],
        "Air_temperature_K": [air_temperature],
        "Process_temperature_K": [process_temperature],
        "Rotational_speed_rpm": [rotational_speed],
        "Torque_Nm": [torque],
        "Tool_wear_min": [tool_wear]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Machine Failure Risk Detected")
        st.write("Maintenance inspection is recommended.")
    else:
        st.success("✅ Machine is Operating Normally")

    st.metric(
        "Failure Probability",
        f"{probability * 100:.2f}%"
    )

    if probability >= 0.70:
        st.warning("Risk Level: High")
    elif probability >= 0.40:
        st.warning("Risk Level: Medium")
    else:
        st.info("Risk Level: Low")