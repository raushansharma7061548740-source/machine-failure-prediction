# Machine Failure Prediction System

An AI-powered machine learning application that predicts whether an industrial machine is likely to fail based on its operating conditions. The model is built using **XGBoost Classifier** and deployed with **Streamlit** for real-time predictions.

---

## Features

- Predicts machine failure using sensor data
- Interactive Streamlit web application
- Real-time prediction with failure probability
- Displays machine health status and risk level
- Fast and user-friendly interface

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**.

### Input Features

- Product Type
- Air Temperature (K)
- Process Temperature (K)
- Rotational Speed (RPM)
- Torque (Nm)
- Tool Wear (Minutes)

### Target Variable

- **Machine Failure**
  - 0 → No Failure
  - 1 → Failure

---

## Machine Learning Workflow

- Data Cleaning
- Label Encoding
- Train-Test Split
- Model Training using XGBoost
- Model Evaluation
- Model Saving
- Streamlit Deployment

---

## Project Structure

```
Machine-Failure-Prediction-System/
│
├── app.py
├── xgboost_model.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/Machine-Failure-Prediction-System.git
```

Navigate to the project directory

```bash
cd Machine-Failure-Prediction-System
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## How to Use

1. Launch the Streamlit application.
2. Enter machine operating parameters.
3. Click **Predict Machine Failure**.
4. View the prediction result, failure probability, and risk level.

---

## Model

The application uses **XGBoost Classifier**, a powerful gradient boosting algorithm that performs well on structured datasets. It was selected because of its high accuracy, robustness, and ability to model complex relationships in machine sensor data.

---

## Future Improvements

- Live IoT sensor integration
- SHAP-based model explainability
- Remaining Useful Life (RUL) prediction
- Maintenance scheduling recommendations
- Docker and cloud deployment

---

## Screenshots

_Add screenshots of the Streamlit application here._

---

## Author

**Raushan Kumar**

B.Tech in Artificial Intelligence & Robotics
